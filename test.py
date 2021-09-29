#!/usr/bin/env python3
name = input('Enter the file name:')
fobj = open(name)
for x in fobj:
    print(x,end='')
fobj.close()
