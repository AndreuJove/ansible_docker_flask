## Package Crawler description:

Flask application using Ansible with Docker.




## Requirements

Python3.





## VM Machine installation and connection:

1) Download and unzip de `debian10-ssh.img.tar.xz`
2) Download Virtual Machine Manager (https://virt-manager.org/download/)
3) Create the VM using the `debian10-ssh.img.tar.xz` file and XML file for the configuration of the VM.
4) Run the VM using Virtual Machine Manager.
5) Connect to the virtual machine using: 
    ```console
    $ ssh -i /path/to/rsa.pub root@192.168.122.188
    ```

## VM SETUP:

6) Solve dpkg problems using:
```console
$ dpkg --configure -a
```
Choose to install GRUB in the device: /dev/vda

7) Install git:
    ```console
    $ apt install git
    ```
8) Install docker using the next following steps:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10


9) Install pip:
    ```console
    $ apt install python3-pip
    ```


10) Install ansible by python3
    ```console
    $ pip3 install ansible
    ```
11) Install docker python package (required to build an image inside ansible):
    ```console
    $ pip3 install docker
    ```

12) Run:
    ```console
    $ git clone https://github.com/AndreuJove/alpine_docker_flask.git
    ```

13) Move to the project directory:
```console
$ cd alpine_docker_flask
```

14) Run the playbook of build and run the container:
```console
$ ansible-playbook build_run_container.yml
```

15) Check that the container is running using:
```console
$ docker ps
```


## Interesting commands:

Command to view the connections:
- $ virsh net-dumpxml default

List ssh keys:
- $ ls -al ~/.ssh



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