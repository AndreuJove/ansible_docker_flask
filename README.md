## Package Crawler description:

Flask application using Ansible with Docker.

<br />

## Requirements

Python3 


## VM Machine installation:

1) Download and unzip de `debian10-ssh.img.tar.xz`
2) Download Virtual Machine Manager.
3) Create the VM using the `debian10-ssh.img.tar.xz` file and XML file for the configuration of the VM.
4) Run the VM.
5) Connect to the virtual machine using: ssh -i /path/to/rsa.pub root@192.168.122.188

Interesting commands:
1) Command to view the connections:
  `virsh net-dumpxml default`
2) List ssh keys:
  `ls -al ~/.ssh`

## Package installation:


1) git clone https://github.com/AndreuJove/alpine_docker_flask.git
2) cd alpine_docker_flask
3) chmod +x install.sh
4) install.sh


## Build with:
- [Ansible](https://docs.ansible.com/).
- [Docker](https://www.docker.com/).
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
<br />


## Authors

- Andreu Jové

<br />


## License

- This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/alpine_docker_flask/blob/master/LICENSE.MD) file for details.