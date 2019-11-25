# PreScript
/usr/sbin/unbound-control stats | egrep '(num.query.type|mem.cache|total.num)' | sed 's/=/ /g' | sed 's/^/cbnoc-dns /g' > /root/zabbix_script/result

# Conf
ZABBIX_IPADDR='10.1.1.24'
ZABBIX_PORT='10051'
YOUR_HOSTNAME_ON_ZABBIX="cbnoc-dns"

# Send
/usr/bin/zabbix_sender -z ${ZABBIX_IPADDR} \
                       -p ${ZABBIX_PORT} \
                       -s ${YOUR_HOSTNAME_ON_ZABBIX} \
                       -i /root/zabbix_script/result &>/dev/null
# -vv
