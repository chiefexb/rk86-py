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
    memory.write(0xc001,0x80)
    memory.write(0xc000,26)
    print ("C",memory.cursor_x_buf)
    
    
    
    print ("BB",memory.vg75_c001_80_cmd)
if __name__ == "__main__":
    main()

