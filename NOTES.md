- example of the run ansible playbook for identodock:
    docker run -it --rm -v ${HOME}/.ssh:/root/.ssh:ro \
    -v $(pwd)/hosts:/etc/ansible/hosts \
    -v $(pwd)/identidock.yml:/etc/ansible/identidock.yml \
    ansible/centos7-ansible \
    ansible-playbook /etc/ansible/identidock.yml

