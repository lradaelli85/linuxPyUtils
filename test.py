#!/usr/bin/python
# -*- coding: utf-8 -*-.

from utils.networklib import networklib
import sys

if __name__ == "__main__":
#    ip = sys.argv[1]
#    cidr = sys.argv[2]
    a = networklib()
#    if a.is_in_net(ip,cidr):
#        print '{} is in net {}'.format(ip,cidr)
#    else:
#        print '{} is in not in net {}'.format(ip,cidr)
#    if a.is_usable_ip(ip,cidr):
#        print '{} : usable ip'.format(ip)
#    else:
    #     print '{} : not usable ip'.format(ip)
    # net = a.get_network_addr(cidr)
    # if net:
    #     print "network address : {}".format(".".join(map(str, net)))
    # broad = a.get_broadcast_addr(cidr)
    # if broad:
    #     print "network broadcast : {}".format(".".join(map(str, broad)))
    # z = a.usable_ip_range(cidr)
    # print "usable range : {} - {}".format(".".join(map(str, z["first_ip"])) , ".".join(map(str, z["last_ip"])))
    # nnn = a.usable_ips(cidr)
    #print "usable ip : {}".format(nnn)
    print a.get_routes('enp0s25')
