#!/usr/bin/python3

class Memory:
    buf=[0x10000 * [0]][0]
    def zero_ram():
        for i in range (0x8000): buf[i] = 0
    vg75_c001_00_cmd = 0
    screen_size_x_buf = 0
    screen_size_y_buf = 0
    ik57_e008_80_cmd = 0
    vg75_c001_80_cmd = 0
    cursor_x_buf = 0
    cursor_y_buf = 0
    tape_8002_as_output = 0
    video_memory_base_buf = 0
    video_memory_size_buf = 0
    video_memory_base = 0
    video_memory_size = 0
    video_screen_size_x = 0
    video_screen_size_y = 0
    video_screen_cursor_x = 0
    video_screen_cursor_y = 0
    def length(): 
        return 0x10000
    def read_raw(addr):
        addr =addr & 0xffff
        return buf[addr] & 0xff
    def read (addr,self):
        addr =  addr & 0xffff
        f=self.buf[addr]
        if (addr == 0x8002):
            pass
            #f=self.keyboard.modifiers
        if (addr == 0x8001):
            #keyboard_state = this.keyboard.state
             ch = 0xff
             kbd_scanline = ~this.buf[0x8000]
             for  i in range(8):
                 if ((1 << i) & kbd_scanline):
                     ch &= keyboard_state[i]
                     f =ch
        if (addr == 0xC001):
             f= 0xff
        return f
     
