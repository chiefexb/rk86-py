import unicurses
import locale

stdscr = unicurses.initscr()
stdscr.clear()
cursor_x = 0
cursor_y = 0
for y in range (16):
    for x in range (16):
        stdscr.addstr(x, y, u'\u259A',               unicurses.A_REVERSE)
stdscr.refresh()
while True:
    c = stdscr.getch()
    if c == ord('q'):
        break  # Exit the while loop
unicurses.endwin()

