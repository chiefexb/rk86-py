import unicurses 
import os, time
stdscr = unicurses.initscr()
pd = unicurses.newpad(10, 10)
heigth=100
width=100
stdscr.refresh()
st = ''
pd.addstr(1,1, st)
#pd.border(1)
pd.box()
pd.refresh( 0,0, 5,5, 20,75)
for x in range(15):
    time.sleep(1)
    stdscr.refresh()
    pd.refresh( 0,x, 5,5, 20,75)


while True:
    c = stdscr.getch()
    if c == ord('q'):
        break  # Exit the while loop
unicurses.endwin()

