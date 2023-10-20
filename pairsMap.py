#!/usr/bin/python3

import sys

for line in sys.stdin:
    collection = line.lower().strip('\r\n ').split(",")
    for key in range(len(collection)):
        for value in range(key + 1, len(collection)):
            if collection[value] > collection[key]:
                print(f'{collection[key]}:{collection[value]}--1')
            else:
                print(f'{collection[value]}:{collection[key]}--1')