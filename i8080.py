
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

    # def self.memory_read_byte (addr):
        # return self.memory.read(addr & 0xffff) & 0xff
    # def self.memory_write_byte(addr, w8):
        # self.memory.write(addr & 0xffff, w8 & 0xff)
      # def self.memory_read_word (addr):
        # return self.memory_read_byte(addr) | (self.memory_read_byte(addr + 1) << 8)
    # def self.memory_write_word (addr, w16):
        # self.memory_write_byte(addr, w16 & 0xff)
        # self.memory_write_byte(addr + 1, w16 >> 8)
    # def self.reg (r):
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

   
   
#    def store_flags () 
 ##      if (self.sf):
  #          f = f |F_NEG
   #     else f &= ~F_NEG

        # if (self.zf) f |= F_ZERO   else f &= ~F_ZERO
        # if (self.hf) f |= F_HCARRY else f &= ~F_HCARRY
        # if (self.pf) f |= F_PARITY else f &= ~F_PARITY
        # if (self.cf) f |= F_CARRY  else f &= ~F_CARRY
        # f |= F_UN1    // UN1_FLAG is always 1.
        # f &= ~F_UN3   // UN3_FLAG is always 0.
        # f &= ~F_UN5   // UN5_FLAG is always 0.
    #    return f

    # def self.retrieve_flags (f):
        # self.sf = f & F_NEG    ? 1 : 0
        # self.zf = f & F_ZERO   ? 1 : 0
        # self.hf = f & F_HCARRY ? 1 : 0
        # self.pf = f & F_PARITY ? 1 : 0
        # self.cf = f & F_CARRY  ? 1 : 0
  

    # def self.bc(): return self.rp(0) 
    # def self.de(): return self.rp(2) 
    # def self.hl(): return self.rp(4) 

    # self.b = function()  return self.reg(0) 
    # self.c = function()  return self.reg(1) 
    # self.d = function()  return self.reg(2) 
  # self.e = function()  return self.reg(3) 
  # self.h = function()  return self.reg(4) 
  # self.l = function()  return self.reg(5) 
  # self.a = function()  return self.reg(7) 

  # self.set_b = function(v)  self.set_reg(0, v) 
  # self.set_c = function(v)  self.set_reg(1, v) 
  # self.set_d = function(v)  self.set_reg(2, v) 
  # self.set_e = function(v)  self.set_reg(3, v) 
  # self.set_h = function(v)  self.set_reg(4, v) 
  # self.set_l = function(v)  self.set_reg(5, v) 
  # self.set_a = function(v)  self.set_reg(7, v) 

  # self.next_pc_byte = function() 
    # var v = self.memory_read_byte(self.pc)
    # self.pc = (self.pc + 1) & 0xffff
    # return v

  

  	
