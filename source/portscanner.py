#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

star = '*********************************************************************'

print star

portscanner_ico = '''
 ____  _                 _     _____ ____ ____  ____                  
/ ___|(_)_ __ ___  _ __ | | __|_   _/ ___|  _ \/ ___|  ___ __ _ _ __  
\___ \| | '_ ` _ \| '_ \| |/ _ \| || |   | |_) \___ \ / __/ _` | '_ \ 
 ___) | | | | | | | |_) | |  __/| || |___|  __/ ___) | (_| (_| | | | |
|____/|_|_| |_| |_| .__/|_|\___||_| \____|_|   |____/ \___\__,_|_| |_|
                  |_|     Author : Ismail Tasdelen               v1.2           
'''

print portscanner_ico

print star

if __name__ == '__main__':
    target = raw_input('TARGET IP : ')
    target_IP = gethostbyname(target)
    print star
    print 'Starting scan on host... ', targe_tIP
    print star

    for port_range in range(0, 65535):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((target_IP, port_range))

        if(result == 0) :
            print 'PORT %d: OPEN' % (port_range,)
        s.close()
