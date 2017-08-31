#!/usr/bin/python3
import array
class Memory:
    def __init__(self):
        self.buf=[0x10000 * [0]][0]
        self.vg75_c001_00_cmd = 0
        self.screen_size_x_buf = 0
        self.screen_size_y_buf = 0
        self.ik57_e008_80_cmd = 0
        self.vg75_c001_80_cmd = 0
        self.cursor_x_buf = 0
        self.cursor_y_buf = 0
        self.tape_8002_as_output = 0
        self.video_memory_base_buf = 0
        self.video_memory_size_buf = 0
        self.video_memory_base = 0
        self.video_memory_size = 0
        self.video_screen_size_x = 0
        self.video_screen_size_y = 0
        self.video_screen_cursor_x = 0
        self.video_screen_cursor_y = 0
    def zero_ram():
        for i in range (0x8000): buf[i] = 0
    def length(): 
        return 0x10000
    def read_raw(addr):
        addr =addr & 0xffff
        return buf[addr] & 0xff

