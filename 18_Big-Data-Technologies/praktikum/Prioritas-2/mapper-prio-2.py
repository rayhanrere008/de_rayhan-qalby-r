#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split(',')
    print('%s\t%s' % (key, value))
