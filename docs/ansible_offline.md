
## Create an offline Ansible installation

In some circumstances it might be useful to have a working copy of Ansible without having to resort to installing via an distro-package or
python pip.  To accomplish this see the following steps below.


### Prerequisites
First we need to make sure python-pip is installed, if we are using CentOS or RHEL EPEL needs to be installed.
```bash
[root@ff372106292c /]# yum install python-pip python-devel make gcc -y
```

Next we need python virtualenv
```bash
[root@ff372106292c /]# pip install virtualenv
```

### Creating a python virtual environment

```bash
[root@ff372106292c /]# virtualenv viransible
```

### Install Ansible and other dependencies

Source the Python virtualenv...
```bash
[root@ff372106292c /]# source viransible/bin/activate
```
And within the virtualenv install ansible and docker-py
```bash
(viransible)[root@ff372106292c /]# pip install ansible docker-py
```
Once that is complete we are good to package the install in a tar file to be used in a offline manner
```bash
(viransible)[root@ff372106292c /]# tar -cvf viransible.tar viransible/
```

## Using an Offline Ansible installation

Extract the tarball
```bash
[root@1aed89c65969 /]# tar -cvf viransible.tar viransible/
```

Source activate
```bash
[root@1aed89c65969 /]# source viransible/bin/activate
```

Example execution
```bash
(viransible)[root@1aed89c65969 /]# ansible localhost -m setup -c local -i localhost,
localhost | success >> {
    "ansible_facts": {
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "04/01/2014",
        "ansible_bios_version": "1.8.1-20150318_183358-",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.10.0-229.7.2.el7.x86_64",
            "LANG": "en_US.UTF-8",
            "console": "ttyS0,115200n8",
            "crashkernel": "auto",
            "net.ifnames": "0",
            "no_timer_check": true,
            "ro": true,
            "root": "UUID=a4cc056f-4b5b-43dc-9b85-c6d230aa0829"
        },
...
```
