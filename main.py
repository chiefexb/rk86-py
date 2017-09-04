#!/usr/bin/python3
# -*- coding: utf-8 -*-
from i8080 import *
from memory import *
def IO():
    pass
    
def Autoexec():
    pass
    
def main():
    memory=Memory()
    cpu= I8080(memory)
    memory.write_raw(0x8003,0x02)
    m=memory.read(0x8003)
    print ('LWB=',memory.last_written_byte)
    print (hex(0x8003 & 0xefff))
    print (m)
if __name__ == "__main__":
    main()

