#!/bin/bash

apt-get install ansible
ansible-playbook install_docker.yml
pip3 install ansible
pip3 install docker
ansible-playbook build_run_container.yml