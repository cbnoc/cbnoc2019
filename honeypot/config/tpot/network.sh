#!/bin/bash

NETWORK_MGMT=10.1.1.0/24
ADDRESS_MGMT=10.1.1.31
NETWORK_UNSECURE=202.236.88.0/24
ADDRESS_UNSECURE=202.236.88.22

# Stop T-Pot
systemctl stop tpot

# FireWall
yes | ufw reset
ufw default deny
ufw allow proto tcp to $ADDRESS_UNSECURE port 1:64000
ufw allow proto udp to $ADDRESS_UNSECURE port 1:64000
ufw allow from $NETWORK_MGMT to $ADDRESS_MGMT port 22
ufw allow proto tcp from $NETWORK_MGMT to $ADDRESS_MGMT port 64001:65535
ufw allow proto udp from $NETWORK_MGMT to $ADDRESS_MGMT port 64001:65535
yes | ufw enable

# Configure T-Pot
sed "s/__IP__/$ADDRESS_UNSECURE/g" tpot.yml > /opt/tpot/etc/tpot.yml

# Restart T-Pot
systemctl start tpot
