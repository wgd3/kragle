FROM centos:latest
MAINTAINER Joseph Callen <jcpowermac@gmail.com>


RUN yum -y update \
  && yum -y install qemu-kvm epel-release gcc git wget \
  && yum -y install qemu \
  && yum -y install python-pip python-devel unzip \
  && pip install ansible \
  && pip install requests \
  && yum clean all
  
RUN mkdir /opt/packer \
  && cd /opt/packer \
  && wget -nv $(python -c 'import requests;print "https://dl.bintray.com/mitchellh/packer/packer_%s_linux_amd64.zip" % requests.get("https://api.github.com/repos/mitchellh/packer/tags").json()[0]["name"].replace("v","")') -O /opt/packer/packer.zip \
  && unzip packer.zip

RUN cd /opt \
  && git clone https://github.com/csc/kragle.git

EXPOSE 5900
WORKDIR /build
ENTRYPOINT ["/opt/packer/packer"]
CMD ["--help"]

