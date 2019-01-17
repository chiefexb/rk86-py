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
    def __init__(self,keyboard):
        self.keyboard=keyboard
    def length(): 
        return 0x10000
    def read_raw(self,addr):
        addr &= 0xffff
        f=self.buf[addr] & 0xff
        return f
    def read (self,addr):
        addr &=  0xffff
        f=self.buf[addr]
        if (addr == 0x8002):
            f=self.keyboard.modifiers
        if (addr == 0x8001):
            keyboard_state = self.keyboard.state
            ch = 0xff
            kbd_scanline = ~self.buf[0x8000]
            for  i in range(8):
                if ((1 << i) & kbd_scanline):
                    ch &= keyboard_state[i]
                    f =ch
        if (addr == 0xC001):
             f= 0xff
        return f
    last_written_byte = -1
    def write_raw (self,addr, byte):
        self.buf[addr & 0xffff] = byte & 0xff
    def write (self,addr, byte):
        print ("IN WRITE")
        addr &= 0xffff
        byte &= 0xff
        print ('ADR=',hex(addr))
        if (addr >= 0xF800): 
            pass
        if (addr == 0x8002):
            pass
        # Tape I/O isn't implemented yet.
        # if (this.tape_8002_as_output)
        #   this.tape_write_bit(byte & 0x01);
        if (addr <0xF800 and addr != 0x8002):
            self.buf[addr] = byte
            peripheral_reg = addr & 0xefff
            #RUS/LAT indicator
            print ('PREG=',hex(peripheral_reg))
            if (peripheral_reg == 0x8003):
                print ('CATCH')
                if (byte == self.last_written_byte):
                    pass
                if (byte != self.last_written_byte):
             # The indicator status can is "byte & 0x01".
                    self.last_written_byte = byte
             # The cursor control sequence.
            if (peripheral_reg == 0xc001 and byte == 0x80):
                self.vg75_c001_80_cmd = 1
            if (peripheral_reg == 0xc000 and self.vg75_c001_80_cmd == 1):
                self.vg75_c001_80_cmd += 1
                self.cursor_x_buf = byte + 1
            if (peripheral_reg == 0xc000 and self.vg75_c001_80_cmd == 2):
                self.cursor_y_buf = byte + 1
                #screen.set_cursor(self.cursor_x_buf - 1, self.cursor_y_buf - 1)
                self.video_screen_cursor_x = self.cursor_x_buf
                self.video_screen_cursor_y = self.cursor_y_buf
                self.vg75_c001_80_cmd = 0
            if (peripheral_reg == 0xc001 and byte == 0):
                self.vg75_c001_00_cmd = 1
            if (peripheral_reg == 0xc000 and self.vg75_c001_00_cmd == 1):
                self.screen_size_x_buf = (byte & 0x7f) + 1
                self.vg75_c001_00_cmd += 1
            if (peripheral_reg == 0xc000 and self.vg75_c001_00_cmd == 2):
                self.screen_size_y_buf = (byte & 0x3f) + 1;
                self.vg75_c001_00_cmd = 0;
     # The screen area parameters command sequence.
            if (peripheral_reg == 0xe008 and byte == 0x80):
                self.ik57_e008_80_cmd = 1
                self.tape_8002_as_output = 1
            if (peripheral_reg == 0xe004 and self.ik57_e008_80_cmd == 1):
                self.video_memory_base_buf = byte
                self.ik57_e008_80_cmd += 1
            if (peripheral_reg == 0xe004 and self.ik57_e008_80_cmd == 2):
                self.video_memory_base_buf |= byte << 8
                self.ik57_e008_80_cmd += 1
            if (peripheral_reg == 0xe005 and self.ik57_e008_80_cmd == 3):
                self.video_memory_size_buf = byte
                self.ik57_e008_80_cmd += 1
            if (peripheral_reg == 0xe005 and self.ik57_e008_80_cmd == 4):
                self.video_memory_size_buf = ((self.video_memory_size_buf | (byte << 8)) & 0x3fff) + 1
                self.ik57_e008_80_cmd = 0
            # Settings for video memory boundaries and the screen format
            # only take an effect after the DMA command 0xA4 (start the channel).
            if (peripheral_reg == 0xe008 and byte == 0xa4):
                if (self.screen_size_x_buf and self.screen_size_y_buf):
                   # Save ("apply") the screen dimentions.
                    self.video_screen_size_x = self.screen_size_x_buf
                    self.video_screen_size_y = self.screen_size_y_buf
                   # Save ("apply") the video area parameters.
                    self.video_memory_base = self.video_memory_base_buf
                    self.video_memory_size = self.video_memory_size_buf
                  #// Re-configure video.
                   #screen.set_geometry(self.video_screen_size_x, self.video_screen_size_y, self.video_memory_base);
                self.tape_8002_as_output = 0
        
    def load_file (self, f):
        #for (var i = file.start; i <= file.end; ++i) {
        #this.write_raw(i, file.image.charCodeAt(i - file.start));
         for i in range(f['start'],f['end']):
             self.write_raw(i,f['image'][ i-f['start'] ] )
    
     #   #for (var i = file.start; i <= file.end; ++i) {
      #  #this.write_raw(i, file.image.charCodeAt(i - file.start));
     
   
