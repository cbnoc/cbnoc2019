# dhcp-zabbix-sender

## これは何

isc-dhcpサーバーのステータスを表示するスクリプト(python3)


```
cbnoc-dhcp lease-ip.10.1.1.0_24 1
cbnoc-dhcp lease-ip.10.1.8.0_21 0
cbnoc-dhcp lease-ip.10.1.16.0_24 0
cbnoc-dhcp lease-ip.202.1.208.0_20 1
cbnoc-dhcp lease-ip.202.236.88.0_24 0
cbnoc-dhcp lease-ip.202.236.89.0_24 0
cbnoc-dhcp lease-ip.202.236.90.0_24 0
cbnoc-dhcp lease-ip.202.236.91.0_24 0
cbnoc-dhcp lease-ip.202.236.92.0_24 0
cbnoc-dhcp lease-ip.202.236.93.0_24 0
cbnoc-dhcp lease-ip.202.236.94.0_24 0
cbnoc-dhcp lease-ip.202.236.95.0_24 0
lease         starts                 ends                   hardware                    client-hostname
------------  ---------------------  ---------------------  --------------------------  -------------------------------
10.1.1.175    1 2019/11/25 03:57:49  1 2019/11/25 06:57:49  ethernet 00:0c:29:85:3f:60  "cbnoc-perfomance-check"
202.1.212.97  1 2019/11/25 03:53:05  1 2019/11/25 06:53:05  ethernet 00:0c:29:96:25:04  "vyos"
```

## 使い方

Zabbix Senderを導入して，Cronでそれを定期的に実行する．

```
  *  *  *  *  * root       /root/zabbix_script/zabbix-send.sh
```
