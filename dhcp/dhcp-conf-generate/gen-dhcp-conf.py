network_info = [
('mgmt','10.1.1.0/24','10.1.1.0 - 10.1.1.255','10.1.1.100 - 10.1.1.191'),

('chicken','10.1.8.0/21','10.1.8.0 - 10.1.15.255','10.1.8.30 - 10.1.15.254'),

('private2','10.1.16.0/24','10.1.16.0 - 10.1.16.255','10.1.16.30 - 10.1.16.254'),

('flets1','-','-',''),

('flets2','-','-',''),

('user','202.1.208.0/20','202.1.208.0 - 202.1.223.255','202.1.208.30 - 202.1.223.254'),

('unsecure','202.236.88.0/24','202.236.88.0 - 202.236.88.255','202.236.88.30 - 202.236.88.254'),

('reserve2','202.236.89.0/24','202.236.89.0 - 202.236.89.255','202.236.89.30 - 202.236.89.254'),

('reserve3','202.236.90.0/24','202.236.90.0 - 202.236.90.255','202.236.90.30 - 202.236.90.254'),

('reserve4','202.236.91.0/24','202.236.91.0 - 202.236.91.255','202.236.91.30 - 202.236.91.254'),

('reserve5','202.236.92.0/24','202.236.92.0 - 202.236.92.255','202.236.92.30 - 202.236.92.254'),

('reserve6','202.236.93.0/24','202.236.93.0 - 202.236.93.255','202.236.93.30 - 202.236.93.254'),

('reserve7','202.236.94.0/24','202.236.94.0 - 202.236.94.255','202.236.94.30 - 202.236.94.254'),

('reserve8','202.236.95.0/24','202.236.95.0 - 202.236.95.255','202.236.95.30 - 202.236.95.254'),

('v6only','-','-',''),

('reserve10','-','-',''),
]

BASE_CONF = '''
# TITLE
subnet NETWORK_ADDR netmask SUBNET {
    range DHCP_BEGIN DHCP_END;
    option routers ROUTER_ADDR;
    option domain-name-servers DNS_ADDR;
} '''

for ni in network_info:
    try:
        net_addr = int(ni[1][-2:])
    except Exception:
        continue
    net_addr_bin = '1'*net_addr + '0'*(32-net_addr)
    subnet_bin = [str(int(net_addr_bin[i*8:(i+1)*8], 2)) for i in range(len(net_addr_bin)//8)]

    subnet = '.'.join(subnet_bin)
    netaddr = ni[1].split('/')[0]
    dhcp_begin = ni[3].split(' - ')[0]
    dhcp_end = ni[3].split(' - ')[1]
    print(BASE_CONF.replace("TITLE", ni[0])
                   .replace("NETWORK_ADDR", netaddr)
                   .replace("SUBNET", subnet)
                   .replace("DHCP_BEGIN", dhcp_begin)
                   .replace("DHCP_END", dhcp_end)
                   .replace("ROUTER_ADDR", netaddr[:-1]+'1')
                   .replace("DNS_ADDR", netaddr[:-1]+'21')
    )
