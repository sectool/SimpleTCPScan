#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

star = '*********************************************************************'

print star

portscanner_ico = '''
#########################################################
#              PORT SCANNER - GH0ST S0FTWARE            #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#########################################################
'''

print portscanner_ico

print star

if __name__ == '__main__':
    target = raw_input('TARGET IP : ')
    targetIP = gethostbyname(target)
    print star
    print 'Starting scan on host... ', targetIP
    print star

    for port_araligi in range(0, 65535):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, port_araligi))

        if(result == 0) :
            print 'PORT %d: OPEN' % (port_araligi,)
        s.close()
