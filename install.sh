#!/bin/bash

apt-get install ansible
pip3 install ansible
pip3 install docker
ansible-playbook install_docker.yml
ansible-playbook build_run_container.yml