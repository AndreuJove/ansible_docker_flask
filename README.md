## Package Crawler description:
Flask application using Ansible with Docker in a debian-10 Virtual Machine.

## Host Machine Requirements:

- Git (apt install git)
- [Python3] (https://www.python.org/downloads/)
- Pip (apt install python3-pip)
- Ansible python package (pip3 install ansible)


## VM Requirements:

- [Python3](https://www.python.org/downloads/)
- Pip (apt install python3-pip)
- [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10)
- Docker python package (pip3 install docker)


## VM SETUP:

1) Download and unzip de `debian10-ssh.img.tar.xz`
2) Download [Virtual Machine Manager](https://virt-manager.org/download/) or do it via command line.
3) Create the VM using the `debian10-ssh.img.tar.xz` file and XML file for the configuration of the VM.
4) Run the VM using Virtual Machine Manager or other application.
5) Connect to the virtual machine using: 
    ```console
    $ ssh -i /path/to/rsa.pub root@192.168.122.188
    ```
6) Solve dpkg problems using:
```console
$ dpkg --configure -a
```
Choose to install GRUB in the device: /dev/vda

7) Install docker using the next following steps:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10

8) Install python package docker:
```console
pip3 install docker
```



## DEPLOY APP to VM:

8) Clone github repo:
    ```console
    $ git clone https://github.com/AndreuJove/ansible_docker_flask.git
    ```

9) Move to the project directory:
```console
$ cd ansible_docker_flask
```

10) Run the playbook using the deploy.yml:
```console
$ ansible-playbook deploy.yml -i ./hosts.yml
```


## Interesting commands:

Command to view the connections:
```console
$ virsh net-dumpxml default
```

List ssh keys:
```
$ ls -al ~/.ssh
```


## Notes

------

Using the next command we install ansible 2.7 to build a container image from a ansible playbook we need newer versions.

```console
$ apt-get install ansible
```
------

## Build with:
- [Ansible](https://docs.ansible.com/).
- [Docker](https://www.docker.com/).
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)




## Authors

- Andreu Jové



## License

- This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/alpine_docker_flask/blob/master/LICENSE.MD) file for details.
