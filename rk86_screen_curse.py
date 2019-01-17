import curses
#stdscr = curses.initscr()
#begin_x = 20; begin_y = 7
#height = 5; width = 40
#win = curses.newwin(height, width, begin_y, begin_x)
#pad = curses.newpad(100, 100)
# These loops fill the pad with letters; addch() is
# explained in the next section
#for y in range(0, 99):
#    for x in range(0, 99):
#        pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#
# Displays a section of the pad in the middle of the screen.
# (0,0) : coordinate of upper-left corner of pad area to display.
# (5,5) : coordinate of upper-left corner of window area to be filled
#         with pad content.
# (20, 75) : coordinate of lower-right corner of window area to be
#          : filled with pad content.
#pad.refresh( 0,0, 5,5, 20,75)
class Screen( ui, memory):
    width=78
    height=30
    cursor_state = True
    cursor_x = 0
    cursor_y = 0
    video_memory_base = 0
    video_memory_size = 0
    cache = []
    
    def __init__(self,ui,memory):
        self.ui=ui
        self.memory=memory
        self.stdscr = curses.initscr()
        self.pad=curses.newpad(self.width, self.height)
        
    def init_cache (self,sz):
        for i in range (sz):
            self.cache.append (True)
            
    def draw_char (self,x, y, ch):
        self.pad.addch(y,x, ch)
        
    def draw_cursor (x, y, visible):
        pass
    def  flip_cursor():
        pass
    def disable_smoothing = function():
        pass
    def set_geometry  (width, height, base):
        pass
    def set_view function(width, height, scale_x, scale_y):
        pass
    def set_cursor (self,x, y):
        self.draw_cursor(self.cursor_x, self.cursor_y, false)
        self.cursor_x = x
        self.cursor_y = y
  
    def draw_screen = function():
        i=self.video_memory_base
        for y in range(self.height):
            for x in range(self.width)
                cache_i=i-self.video_memory_base
                ch=self.memory.read(i)
                if self.cache[cache_i] != ch:
                     draw_char(x, y, ch)
                     self.cache[cache_i] = ch
                i+=1
                
                
        
        
     
        
            

