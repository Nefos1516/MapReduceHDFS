#!/usr/bin/python3

import sys

for line in sys.stdin:
    collection = line.lower().strip('\r\n ').split(",")
    
    for key in collection:    
        H = {}
        for value in collection:        
            if value in H:
                H[value] += 1
                
            else:
                H[value] = 1
            
        print("{}--{}".format(key, H))