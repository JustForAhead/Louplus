#!/usr/bin/env python3
import sys

def Hours(mi):
    if mi < 0:
        raise ValueError('Input number cannot be negative')
    else:
        H = mi // 60
        m = mi % 60
        print('{} H,{} M'.format(H,m))

#if __name__ == '__main__':
#    if len(sys.argv) > 1:
#        Hours(int(sys.argv[1]))
#    else:
#        sys.exit(-1)
#    sys.exit(0)
try:
    Hours(int(sys.argv[1]))
except:
    print('参数有误.')
