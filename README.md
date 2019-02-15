# juniper-ztp
All our tips and tricks on provisioning Juniper gear.

# Installation

Setup ISC DHCP

    yum -y install dhcp
    mv dhcpd.conf /etc/dhcp/dhcpd.conf

Setup a webserver

    yum -y install nginx
    mv nginx.conf /etc/nginx/sites-available/zerotouch.conf
    ln -s /etc/nginx/sites-available/zerotouch.conf /etc/nginx/sites-enabled/zerotouch.conf
    mkdir -p /opt/zerotouch

Python version:

    mv cpe-hostname.py /opt/zerotouch
    mv default.python.conf /opt/zerotouch/default.conf

Slax version:

    mv cpe-hostname.slax /opt/zerotouch
    mv default.slax.conf /opt/zerotouch

