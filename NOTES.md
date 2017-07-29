- example of the run ansible playbook for identodock:
    docker run -it --rm -v ${HOME}/.ssh:/root/.ssh:ro \
    -v $(pwd)/hosts:/etc/ansible/hosts \
    -v $(pwd)/identidock.yml:/etc/ansible/identidock.yml \
    ansible/centos7-ansible \
    ansible-playbook /etc/ansible/identidock.yml


- about ELK:
  formatting rsyslog messages to json (/etc/rsyslog.d/25-docker.conf)
  convenient way to check elasticksearch:
    curl -XGET 'localhost:9200/_cat/indices/?pretty'
    curl -XGET 'localhost:9200/logstash-2017.07.29/_search?q=*&pretty'
  time filter (at right top korner) of kibana is important
  log_driver in compose file is very convenient for debugging
