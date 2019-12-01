#!/usr/bin/env python

import dpkt
from scapy.all import *

def main():
    filename = u'test.pcap'
    pcr = dpkt.pcap.Reader(open(filename,'rb'))
    packet_count = 0
    packet = rdpcap(filename)

    for ts,buf in pcr:
        packet_count += 1

        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            print 'Fail parse FrameNo:', packet_count, '. skipped.'
            continue

        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            flow_word = src + " to " + dst
            if flow_list.has_key(flow_word):
                flow_list[flow_word] += len(str(buf))
            else:
                flow_list[flow_word] = len(str(buf))

    for k,v in flow_list.iteritems():
        print k, ':', v, '[Byte]'
#
#        print packet_count, '. time: ', ts, 'Length:', len(buf)
#        print buf

if __name__ == '__main__':
    main()

