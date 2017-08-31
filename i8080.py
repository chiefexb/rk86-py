def class  I8080(): #(memory, io) 
    self.pc = 0;
    self.iff = 0;
    self.sf = 0;
    self.pf = 0;
    self.hf = 0;
    self.zf = 0;
    self.cf = 0;
    # Registers: b, c, d, e, h, l, m, a
    #            0  1  2  3  4  5  6  7
    self.regs = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
	# this.memory = memory;
    #this.io = io;
    def self.memory_read_byte (addr):
        return self.memory.read(addr & 0xffff) & 0xff

  this.memory_write_byte = function(addr, w8) {
    this.memory.write(addr & 0xffff, w8 & 0xff);
  }

  this.memory_read_word = function(addr) {
    return this.memory_read_byte(addr) | (this.memory_read_byte(addr + 1) << 8); 
  }

  this.memory_write_word = function(addr, w16) {
    this.memory_write_byte(addr, w16 & 0xff);
    this.memory_write_byte(addr + 1, w16 >> 8);
  }
