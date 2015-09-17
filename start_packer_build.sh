#!/bin/bash


DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
docker run -it -e HOME=/ --privileged=true -p 5900:5900 -v /dev/kvm:/dev/kvm:rw -v /dev/net/tun:/dev/net/tun:rw -v $DIR:/build kragle-packer-build build /opt/kragle/rhel7.json 
