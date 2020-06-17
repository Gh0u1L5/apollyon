#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of GFWList.
#
# Copyright (C) 2018 GFWList Project
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""" Pretty simple CIDR calculator
Author: Christopher Meng

Usage: ./calcCIDR.py [CIDR1] [CIDR2] ...

Example: ./calcCIDR.py 10.0.0.0/15 192.168.100.0/24
"""

import sys

if sys.version_info[:2] < (3,3):
    raise Exception("Python 3.3 onwards is required!")

if len(sys.argv) < 2:
    print('Usage: ./calcCIDR.py [CIDR1] [CIDR2] ...')
    print('Example: ./calcCIDR.py 10.0.0.0/15 192.168.0.0/24')
    sys.exit(0)

import ipaddress
import itertools

def get_hosts(cidr):
    hosts_list = list(ipaddress.ip_network(cidr).hosts())
    return [str(x) for i, x in enumerate(hosts_list)]

if __name__ == "__main__":
    cidrs = sys.argv[1:]
    try:
        hosts = [get_hosts(cidr) for cidr in cidrs]
        merged_hosts = list(itertools.chain(*hosts))
        with open('hosts.txt', 'w') as output:
            for host in merged_hosts:
                output.write(host + '\n')
    except ValueError:
        print('Check if given CIDR is valid, or if the network has host bits set!')
