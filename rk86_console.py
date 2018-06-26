class Console():
    from_rk86_table = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    " ",  "!",  "\"",  "#",  "$",  "%%",  "&",  "'",
    "(",  ")",  "*",  "+",  ",",  "-",  ".",  "/",
    "0",  "1",  "2",  "3",  "4",  "5",  "6",  "7",
    "8",  "9",  ":",  ";",  "<",  "=",  ">",  "?",
    "@",  "A",  "B",  "C",  "D",  "E",  "F",  "G",
    "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",
    "P",  "Q",  "R",  "S",  "T",  "U",  "V",  "W",
    "X",  "Y",  "Z",  "[",  "\\",  "]",  "^",  "_",
    "Ю",  "А",  "Б",  "Ц",  "Д",  "Е",  "Ф",  "Г",
    "Х",  "И",  "Й",  "К",  "Л",  "М",  "Н",  "О",
    "П",  "Я",  "Р",  "С",  "Т",  "У",  "Ж",  "В",
    "Ь",  "Ы",  "З",  "Ш",  "Э",  "Щ",  "Ч",  "~",]
    
    def dump_cmd(self,cpu):
        #if (typeof self.dump_cmd.last_address == 'undefined')
        #  self.dump_cmd.last_address = 0;
        #if (typeof self.dump_cmd.last_length == 'undefined')
        #  self.dump_cmd.last_length = 128;
        from_ =0x8000
        #parseInt(self.term.argv[1]);
        #if (isNaN(from)) from = self.dump_cmd.last_address;
        #var sz = parseInt(self.term.argv[2]);
        sz=64
        #if (isNaN(sz)) sz = self.dump_cmd.last_length;
        #self.dump_cmd.last_length = sz;
        #mem = self.runner.cpu.memory;
        mem = cpu.memory
        width=8
        while (sz > 0):
            bytes_ = ""
            chars_ = ""
            chunk_sz = min(width, sz)
            for i in range (chunk_sz):
                ch = mem.read_raw(from_ + i)
                #bytes_ += "%02X ".format(ch)
                bytes_ +='{:02X}'.format(ch)+' '
                if ch>=32 and ch<127:
                    chars_=chars_+ self.from_rk86_table[ch]
                else:
                    chars_=chars_+"."
            if (sz < width):
                bytes_ += " "*((width - sz) * 3)
                chars_ += " "*(width - sz)
          
            print ("{}: {} | {}".format(hex(from_)[2:], bytes_, chars_)+'')
            #print (from_, bytes_, chars_)
            #self.term.write("%04X: %s | %s".format(from, bytes, chars));
            #self.term.newLine();
            
            sz -= chunk_sz;
            from_ = (from_ + chunk_sz) & 0xffff;
    ##self.dump_cmd.last_address = from_;
      
    
    
