#!/usr/bin/env python3

import sys

current_key = None
current_total = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = float(value)

    if current_key != key and current_key:
        avg = current_total / current_count
        print('%s\t%s' % (current_key, avg))
        current_total = value
        current_count = 1
    else:
        current_total += value
        current_count += 1

    current_key = key

if current_key:
    avg = current_total / current_count
    print('%s\t%s' % (current_key, avg))
