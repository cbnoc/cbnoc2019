#!/bin/bash

IP=10.1.1.32
HOSTNAME=cbnoc-cms1

# Stop T-Pot
systemctl stop tpot

# HostName
hostnamectl set-hostname $HOSTNAME

# IP
sed -i -e "s/^ address.*/ address $IP/" /etc/network/interfaces
sed -i -e "s/^ListenAddress.*/ListenAddress $IP/" /etc/ssh/sshd_config

# Logstash
sed -i -e "s/    index => \".*-%{+YYYY.MM.dd}\"/    index => \"$HOSTNAME-%{+YYYY.MM.dd}\"/" /opt/tpot/etc/logstash.conf

# Network
./network.sh

reboot
