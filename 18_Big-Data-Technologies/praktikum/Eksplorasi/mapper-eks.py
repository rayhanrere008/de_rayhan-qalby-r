#!/usr/bin/env python3

import sys

def is_palindrome(word):
    return word == word[::-1]

for line in sys.stdin:
    word = line.strip()
    if is_palindrome(word):
        print('%s\t%s' % (word, "True"))
    else:
        print('%s\t%s' % (word, "False"))