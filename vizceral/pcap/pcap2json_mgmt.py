import dpkt
import socket
import json
import collections as cl
import re


def main():
    # define node
    f = open ("/root/pcap/cbnoc_node.json")
    json_data = json.load(f)

    # read pcap
    filename = u'/root/pcap/test.pcap'
    pcr = dpkt.pcap.Reader(open(filename,'rb'))

    packet_count = 0
    flow_list = {} 

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
            flow_word = src + "to" + dst
            if flow_list.has_key(flow_word):
                flow_list[flow_word] += len(str(buf))
            else:
                flow_list[flow_word] = len(str(buf))

    for k,v in flow_list.iteritems():
        srcdst = k.split("to")
#        print srcdst[0],':',srcdst[1], ':', v, '[Byte]'

        # region
        region = "CODEBLUE network"

        # traffic between region
        srcaddr = intIP(srcdst[0])
        dstaddr = intIP(srcdst[1])
        if srcaddr in range(intIP('10.1.1.0'),intIP('10.1.1.256')) and not(dstaddr in range(intIP('10.1.1.0'),intIP('10.1.1.256'))):
          for i in json_data['connections']:
            if i['source'] == region:
#               print "a"
               i['metrics']['normal'] += int(v)
        
        if dstaddr in range(intIP('10.1.1.0'),intIP('10.1.1.256')) and not(srcaddr in range(intIP('10.1.1.0'),intIP('10.1.1.256'))):
          for i in json_data['connections']:
            if i['target'] == region:
               print "a"
#               i['metrics']['normal'] += int(v)

        # connection
        for i in json_data['nodes']:
           if i['name'] == region:

              # node
              flag = 0
              for j in i['nodes']:
                if j['name']==srcdst[0]:
                  flag += 1
                if j['name']==srcdst[1]:
                  flag += 2
                if flag > 2:
                  break
              if flag==0:
                # add src and dst
                i['nodes'].append(mkNode(srcdst[0]))
                i['nodes'].append(mkNode(srcdst[1]))
              elif flag==1:
                i['nodes'].append(mkNode(srcdst[0]))
                # add src
              elif flag==2:
                i['nodes'].append(mkNode(srcdst[1]))
                # add dst 

              # connection
              conn1 = {}
              conn1["source"] = srcdst[0]
              conn1["target"] = srcdst[1]
              conn1["metrics"] = ({"normal": v})
              conn1["notices"] = ()
              conn1["class"] = "normal"
              i['connections'].append(conn1)
#           print(i['connections'])

    # write JSON        
    wf = open("/root/vizceral-example/dist/sample_data.json","w")
    json.dump(json_data,wf,indent=4)

    # end

def mkNode(name):
  node1={}
  node1["name"] = name
  node1["node_type"] = "client"
  node1["class"] = "normal"
  node1["renderer"] = "focusedChild"
  return node1

def intIP(ipaddr):
  i =ipaddr.split(".")
  j = ((int(i[0])*256+int(i[1]))*256+int(i[2]))*256+int(i[3])
  return j

if __name__ == '__main__':
    main()
