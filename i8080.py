
class  I8080 :
    sp = 0
    pc=0
    iff=0
    sf=0
    pf=0
    hf=0
    fzf=0
    fcf=0
    #  Registers: b, c, d, e, h, l, m, a
    #             0  1  2  3  4  5  6  7
    regs=[ 0, 0, 0, 0, 0, 0, 0, 0 ]
    def __init__(self,memory):
        self.memory = memory
        #self.io = io 
    def memory_read_byte (self,addr):
        m=self.memory.read(addr & 0xffff) & 0xff
        return m
    def set_reg (r, w8,self):
        w8 = w8 & 0xff
        if (r != 6):
            self.regs[r] = w8
        else:
            pass
           # self.memory_write_byte(self.hl(), w8)
    @property
    def hl(self):
        return this.rp(4)
    # def self.memory_read_byte (addr):
        # return self.memory.read(addr & 0xffff) & 0xff
    # def self.memory_write_byte(addr, w8):
        # self.memory.write(addr & 0xffff, w8 & 0xff)
      # def self.memory_read_word (addr):
        # return self.memory_read_byte(addr) | (self.memory_read_byte(addr + 1) << 8)
    # def self.memory_write_word (addr, w16):
        # self.memory_write_byte(addr, w16 & 0xff)
        # self.memory_write_byte(addr + 1, w16 >> 8)
    def reg (self,r):
        if r !=6:
            self.regs[r]
        else:
            self.memory_read_byte(self.hl());
        # return r != 6 ? self.regs[r] : self.memory_read_byte(self.hl())

    def set_reg (r,w8,self):
        w8 = w8 & 0xff
        if (r != 6):
            self.regs[r] = w8
        else:
            pass
           # self.memory_write_byte(self.hl(), w8)
     #// r - 00 (bc), 01 (de), 10 (hl), 11 (sp)
    def rp (r): 
        if r != 6:
            f=(self.regs[r] << 8) | self.regs[r + 1] 
        else: 
             f=self.sp
        return  f
    #def set_rp (r, w16):
    #    if (r != 6) 
    #        self.set_reg(r, w16 >> 8)
    #        self.set_reg(r + 1, w16 & 0xff)
    #    else:
    #        self.sp = w16

    parity_table = [
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
  ]
  


    half_carry_table = [ 0, 0, 1, 0, 1, 0, 1, 1 ]
    sub_half_carry_table = [ 0, 1, 1, 1, 0, 0, 0, 1 ]
    F_CARRY  = 0x01 
    F_UN1    = 0x02 
    F_PARITY = 0x04 
    F_UN3    = 0x08 
    F_HCARRY = 0x10 
    F_UN5    = 0x20 
    F_ZERO   = 0x40 
    F_NEG    = 0x80 
    def execute (self,opcode):
        cpu_cycles = -1;
        #var r, w8, w16, direction, flags;
    def instruction (self):
        pass
    def  jump (self,addr):
        self.pc=addr & 0xffff
        
   
   
