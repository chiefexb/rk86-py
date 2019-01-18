#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from i8080 import *
from rk86_memory import *
from rk86_keyboard import *
from rk86_console import *
def IO():
    pass
    
def Autoexec():
    pass
    
def main():
    keyboard=Keyboard()
    memory=Memory(keyboard)
    cpu= I8080(memory)
    #memory.write(0xc001,0x80)
    #memory.write(0xc000,26)
    console=Console(cpu)
    #print ("C",memory.cursor_x_buf)
    #console.dump_cmd(cpu)
    print (cpu.a() )
    console.help_cmd()
    exit_code=1
    while exit_code:
        a=input()
        arg= console.parse(a)
        if arg[0].lower()=='q':
            exit_code=0
        else: 
            fn=console.commands[arg[0].lower()][0]
            fn(arg)
    
    
    
    #print ("BB",memory.vg75_c001_80_cmd)
if __name__ == "__main__":
    main()

