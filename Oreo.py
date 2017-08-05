#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Now there are 8 patterns of packages of Oreo. How many packages should you buy so that you can get all 8 patterns? (calculate the expectation of the number.)

More generally, if there are N patterns, what is the result?
'''
import random
import sys

def findN(n=8):
    pts = set()
    ans=0
    while len(pts)<n:
        pts.add(random.randint(1,n))
        ans+=1
    return ans

def MC(n=8,rep=1e6):
    n=int(n)
    rep=int(rep)
    ans=0
    for i in range(int(rep)):
        ans+=findN(n)
        if i%1e4==0:
            print(i)
    return ans/rep

if __name__=='__main__':
    print(MC(*sys.argv[1:]))
