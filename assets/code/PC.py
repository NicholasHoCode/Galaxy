import dpkt
import datetime
import socket
from dpkt.compat import compat_ord
import codecs
import math
import numpy as np
import csv

if __name__ == '__main__':
    f = open('', 'rb')
    pcap = dpkt.pcapng.Reader(f)
    bArray = []
    time = []
    for t, b in pcap:
        e = dpkt.ethernet.Ethernet(b)
        ip = e.data
        tcp = ip.data
        if (len(b) == 132):
                bArray.extend([b])
                time.extend([(str(datetime.datetime.utcfromtimestamp(t)))])
    for i in range(0,len(bArray)):        
        symbols.extend([str(bArray[i][65:73],'utf-8')])
        hex_bytes = codecs.encode(bArray[i][78:85],'hex_codec')
        hex_str = hex_bytes.decode("ascii")
        hex_str_rev = "".join(reversed([hex_str[k:k+2] for k in range(0,len(hex_str),2)]))
        p = int(str(int(hex_str_rev[6:15],16)))/1000000
        price.extend([p])        
        hex_bytes = codecs.encode(bArray[i][86:89], 'hex_codec')
        hex_str = hex_bytes.decode("ascii")
        hex_str = "".join(reversed([hex_str[k:k+2] for k in range(0,len(hex_str),2)]))
        v = int(str(int(hex_str,16)))
        volume.extend([v])
        hex_bytes = codecs.encode(bArray[i][90:91], 'hex_codec')
        hex_str = hex_bytes.decode("ascii")
        hex_str = "".join(reversed([hex_str[k:k+2] for k in range(0,len(hex_str),2)]))
        bb = int(str(int(hex_str,16)))
        buyBroker.extend([bb])
        hex_bytes = codecs.encode(bArray[i][104:105], 'hex_codec')
        hex_str = hex_bytes.decode("ascii")
        hex_str = "".join(reversed([hex_str[k:k+2] for k in range(0,len(hex_str),2)]))
        sb = int(str(int(hex_str,16)))
        sellBroker.extend([sb])
        d = time[i][0:4]+time[i][5:7]+time[i][8:10]
        date.extend([d])
        hex_bytes = codecs.encode(bArray[i][124:131], 'hex_codec')
        hex_str = hex_bytes.decode("ascii")
        hex_str = "".join(reversed([hex_str[k:k+2] for k in range(0,len(hex_str),2)]))
        et = str(int(str(int(hex_str,16)))/1000000)
        etn = "{0:0=2d}".format(int(time[i][10:13])-4)+time[i][13:19]+":."+et[11:17]
        et_2 = "0."+et[11:17]
        exchangeTime2.extend([float(et_2)])
        exchangeTime.extend([etn])
        time_str = "{0:0=2d}".format(int(time[i][10:13])-4)+time[i][13:19]+":"+time[i][19:len(time[0])]
        time_str2 = "0"+time[i][19:len(time[0])]
        localTime2.extend([float(time_str2)])                    
        localTime.extend([time_str])
    cArray = np.asarray(localTime2) - np.asarray(exchangeTime2)
    cArray[::-1].sort()
    with open('','w', newline='') as f:
        writer = csv.writer(f)
        for row in zip():
            writer.writerow(row)
