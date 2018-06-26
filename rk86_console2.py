#!/usr/bin/python3
# -*- coding: utf-8 -*-
from i8080 import *
from rk86_memory import *
from rk86_keyboard import *


import colorama
from colorama import Fore,Back, Style
from colorama import init

def main():
    keyboard=Keyboard()
    memory=Memory(keyboard)
    cpu= I8080(memory)
   
    init()

    
    import colorama
    
    print(Fore.BLUE + "Hello World")
    print ("dump memory / d [start_address [, number_of_bytes]]")
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
    while True :
        a=input()
        print (a)
    
if __name__ == "__main__":
    main()
