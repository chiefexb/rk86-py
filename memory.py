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
    def read_raw(self,addr):
        addr =addr & 0xffff
        f=self.buf[addr] & 0xff
        return f
    def read (self,addr):
        addr =  addr & 0xffff
        f=self.buf[addr]
        if (addr == 0x8002):
            pass
            #f=self.keyboard.modifiers
        if (addr == 0x8001):
            #keyboard_state = this.keyboard.state
             ch = 0xff
             #kbd_scanline = ~this.buf[0x8000]
             #for  i in range(8):
              #   if ((1 << i) & kbd_scanline):
               #      ch &= keyboard_state[i]
                #     f =ch
        if (addr == 0xC001):
             f= 0xff
        return f
    last_written_byte = -1
    def write_raw (self,addr, byte):
        self.buf[addr & 0xffff] = byte & 0xff
    def write (self,addr, byte):
        addr &= 0xffff
        byte &= 0xff
        
        print ('ADR=',hex(addr))
        if (addr >= 0xF800): 
            pass
        if (addr <0xF800):
            self.buf[addr] = byte
            peripheral_reg = addr & 0xefff;
            #RUS/LAT indicator
            print ('PREG=',hex(peripheral_reg))
            if (peripheral_reg == 0x8003):
                print ('CATCH')
                if (byte == self.last_written_byte):
                    pass
                if (byte != self.last_written_byte):
                #    # The indicator status can is "byte & 0x01".
                    self.last_written_byte = byte
      
    
  
     
