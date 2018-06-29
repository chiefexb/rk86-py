#!/usr/bin/python3
# -*- coding: utf-8 -*-
from i8080 import *
from rk86_memory import *
from rk86_keyboard import *
from rk86_console import *
from ui import *
def IO():
    pass
    
def Autoexec():
    pass
    
def main():
    keyboard=Keyboard()
    memory=Memory(keyboard)
    cpu= I8080(memory)
    cpu.memory.write(0x8000,0x80)
    #memory.write(0xc000,26)
    console= Console()
    ff=parse_rk86_binary('')
    cpu.memory.load_file(ff)
    while 1:
        a=input()
        #print ("F900 0000 0000 000 0000 fsdfsdfsdfsd.. ")
        console.dump_cmd(cpu)
    
    
    print ("BB",memory.vg75_c001_80_cmd)
if __name__ == "__main__":
    main()
