import dpkt
from scapy.all import *
import socket
import json
import collections as cl
import re

def main():
    regionArray = ((intIP('10.1.1.0'),intIP('10.1.1.255')),(intIP('202.1.208.0'),intIP('202.1.223.255')))
    internet = 'INTERNET'

    # define node
    f = open ("/root/pcap/cbnoc_node.json")
    json_data = json.load(f)

    # read pcap
    filename = u'/root/pcap/test.pcap'
#    pcr = dpkt.pcap.Reader(open(filename,'rb'))
    packet = rdpcap(filename)

    packet_count = 0
    flow_list = {} 
    flow_list_error = {} 

    # read pcap to flow_list
    # key = srcIP to dstIP
    # value = byte
    # flow_list = {"0.0.0.0to0.0.0.0":0000,"0.0.0.1to0.0.0.1":1111,...}
#    print packet

    for pac in packet:
        packet_count += 1
#        print packet_count
#        try:
#            eth = dpkt.ethernet.Ethernet(buf)
#        except:
#            print 'Fail parse FrameNo:', packet_count, '. skipped.'
#            continue

#        if type(eth.data) == dpkt.ip.IP:
#            ip = eth.data
        try:
            src = pac.psrc
        except:
#            print "error"
            continue

        try: 
            dst = pac.pdst
        except:
#            print "error"
            continue

        flow_word = src + "to" + dst

            ## danger check (not implemented)
#            if type(ip.data) == dpkt.tcp.TCP:
#              if (ip.data.flags & dpkt.tcp.TH_RST) != 0 :
        if flow_list.has_key(flow_word):
           flow_list[flow_word] += len(pac)
#                  flow_list_error[flow_word] += len(str(buf))
#                else:
#                  flow_list_error[flow_word] = len(str(buf))
#              elif flow_list.has_key(flow_word):
#                flow_list[flow_word] += len(str(buf))
        else:
#                flow_list[flow_word] = len(str(buf))
           flow_list[flow_word] = len(pac)

    # recieved per sec
    for i in flow_list.values():
      i = int(i)/300
#    for i in flow_list_error.values():
#      i = int(i)/300

#    print flow_list

    # make json object
    for k,v in flow_list.iteritems():
      srcdst = k.split("to")
#      print srcdst[0],':',srcdst[1], ':', v, '[Byte]'
      for regrange in regionArray:
#        print regrange
        for regionInt in range(regrange[0],regrange[1],256):
         # region
         region = strIP(regionInt)+"/24"
         IPstart = regionInt
         IPend = regionInt + 255
#         IPstart = regrange[0]
#         IPend = regrange[0]+255
#         print strIP(IPstart) +" to " + strIP(IPend)

         # traffic between region
         srcAddr = intIP(srcdst[0])
         dstAddr = intIP(srcdst[1])
         if srcAddr in range(IPstart,IPend):
# and dstAddr in range(regionArray[0][0],regionArray[0][1]) and dstAddr in range(regionArray[1][0],regionArray[1][1]):
           # define region
           flag = 0
           for i in json_data['nodes']:
             if i['name'] == region:
               flag = 1
               break
           if flag != 1:
             json_data['nodes'].append(mkRegion(region))
             json_data['connections'].append(mkConn((region,internet),0,0))
           # add connection
           for i in json_data['connections']:
             if i['source'] == region:
               i['metrics']['normal'] += int(v)
#             if k in flow_list_error:
#               i['metrics']['danger'] += int(flow_list_error[k])
        # WARN: region traffic can not draw bidirectional.
#        if dstaddr in range(IPstart,IPend) and not(srcaddr in range(IPstart,IPend)):
#          for i in json_data['connections']:
#            if i['target'] == region:
#               i['metrics']['normal'] += int(v)

           # connection
           for i in json_data['nodes']:
            if i['name'] == region:

              # src and dst node defined?
              flag = 0
              for j in i['nodes']:
                if j['name']==srcdst[0]:
                  flag += 1
                if j['name']==srcdst[1]:
                  flag += 2
                if flag > 2:
                  break

              # define node
              if flag==0:
                # add src and dst
                i['nodes'].append(mkNode(srcdst[0]))
                i['nodes'].append(mkNode(srcdst[1]))
                # add src
              elif flag==1:
                i['nodes'].append(mkNode(srcdst[1]))
                # add dst 
              elif flag==2:
                i['nodes'].append(mkNode(srcdst[0]))

              # connection
#              if k in flow_list_error:
#                i['connections'].append(mkConn(srcdst,v,flow_list_error[k]))
#              else:
              i['connections'].append(mkConn(srcdst,v,0))
#                print(i['connections']['metrics']['danger'])

    # write JSON        
    wf = open("/root/vizceral-example/dist/sample_data.json","w")
    json.dump(json_data,wf,indent=4)
#    print json_data

    # end
#    print "end"

def mkConn(srcdst,v,e):
#  print "mkConn"
  conn1 = {}
  conn1["source"] = srcdst[0]
  conn1["target"] = srcdst[1]
  conn1["metrics"] = ({"normal": v,"danger":e})
  conn1["notices"] = ()
  conn1["class"] = "normal"
  return conn1

def mkRegion(name):
#  print "= mkRegion(" + name + ")"
  node1={}
  node1["name"] = name
  node1["displayName"] = name
  node1["class"] = "normal"
  node1["nodes"] = []
  node1["connections"] = []
  node1["renderer"] = "region"
  return node1

def mkNode(name):
#  print "mkNode" + name
  node1={}
  node1["name"] = name
  node1["node_type"] = "client"
  node1["class"] = "normal"
  node1["renderer"] = "focusedChild"
  return node1

def intIP(ipaddr):
  i = ipaddr.split(".")
  j = ((int(i[0])*256+int(i[1]))*256+int(i[2]))*256+int(i[3])
  return j

def strIP(i):
  ipaddr4 = i%256
  ipaddr3 = (i/256)%256
  ipaddr2 = (i/(256*256))%256
  ipaddr1 = i/(256*256*256)
  j = str(ipaddr1)+"."+str(ipaddr2)+"."+str(ipaddr3)+"."+str(ipaddr4)
  return j

if __name__ == '__main__':
    main()
