from unicurses import *
import os, time
UCS_DHLINE=chr(0x2550)
UCS_DVLINE=chr(0x2551)

stdscr = initscr()
#pd = newpad(10, 10)
heigth=100
width=100
stdscr.addch(0x2551)
stdscr.refresh()
#st = unicurses.ACS_BOARD
#pd.addchr(1,1, st)
#pd.border(1)

#int borderX(ls, rs, ts, bs, tl, tr, bl, br)  
#wborder(pd,UCS_DVLINE,0 , 0, 0, 0, 0, 0, 0)  
#pd.refresh( 0,0, 5,5, 20,75)
#for x in range(15):
#    time.sleep(1)
#    stdscr.refresh()
 #   pd.refresh( 0,x, 5,5, 20,75)


while True:
    c = stdscr.getch()
    if c == ord('q'):
        break  # Exit the while loop
unicurses.endwin()

