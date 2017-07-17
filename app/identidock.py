import logging
import hashlib
from flask import Flask, Response, request
import requests
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
default_name = 'Joe Bloggs'
salt = 'UNIQUE SALT'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    """todo"""
    name = request.form['name'] if request.method == 'POST' else default_name
    salted_name = salt + name
    hashed_name = hashlib.sha256(salted_name.encode()).hexdigest()
    body = '''<html><head><title>Identidock</title></head><body>
        <form method="POST">
            Hello <input type="text" name="name" value="{0}">
            <input type="submit" value="submit">
        </form>
        <p>You look like a:
        <img src="/monster/{1}"/>
        </body></html>
        '''.format(name, hashed_name)
    return body


@app.route('/monster/<name>')
def get_identicon(name):
    """todo"""
    image = cache.get(name)
    if image is not None:
        return Response(image, mimetype='image/png')

    # print('Cache miss', flush=True)
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content
    cache.set(name, image)
    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, host='0.0.0.0')
