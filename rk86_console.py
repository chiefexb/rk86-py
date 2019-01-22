from ui import *
class Console():
    def __init__(self,cpu):
        self.cpu=cpu
        self.commands = {
     "d": [self.dump_cmd,
           "dump memory / d [start_address [, number_of_bytes]]" 
    ],
     "i": [self.cpu_cmd, "CPU iformation / i" ],
    "z": [ 0, 
           "disassemble / z [start_address [, number_of_instructions]]" 
         ],
  "w": [ 0,
           "write bytes / w start_address byte1, [byte2, [byte3]...]"
         ],
    "ww": [ 0,
           "write words / ww start_address word1, [word2, [word3]...]"
         ],
    "wc": [ 0,
           "write characters / ww start_address string"
         ],
    "t": [ 0, "debug control / t [on|off]" ],
    "p": [ 0, "pause CPU / p"
         ],
    "r": [ 0, "resume CPU / r" ],
    "g": [ 0, "go to an address / g 0xf86c" ],
    "gr": [ 0, "reset / gr" ],
    "gs": [ 0, "restart / gs" ],
    "s": [ 0, "single step" ],
    "so": [ 0, "step over" ],
    "bl": [ 0,
           "list breakpoints / bl"
         ],
    "be": [ 0,
           "edit breakpoints / be 1 type:exec address:0xf86c count:3"
          ],
     "l": [ self.load_cmd,
           "l - load file / l KAVKAZ.GAM"       
         ],
    "?": [ 0, "this help / ?"]
    }
        self.from_rk86_table = [
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
    def help_cmd (self):
        #print (self.commands)
        for cmd in self.commands.keys() :
            print ("{0} - {1}".format(cmd, self.commands [cmd][1]) )
    def parse (self, cmd):
        rez=cmd.strip()
        aa=rez.split(' ')
        if len (aa)>1:
            aa2=[]
            for i in aa:
                if i!='':
                    aa2.append(i)
        else:
            aa2=aa
        return aa2
    def dump_cmd(self,arg):
        print (len (arg))
        last_address=None
        if len(arg)>1:
            last_address=self.parseInt(arg[1])
        if last_address is None:
            last_address=0
        
        #if (typeof self.dump_cmd.last_address == 'undefined')
        #  self.dump_cmd.last_address = 0;
        #if (typeof self.dump_cmd.last_length == 'undefined')
        #  self.dump_cmd.last_length = 128;
        from_ =last_address
        #parseInt(self.term.argv[1]);
        #if (isNaN(from)) from = self.dump_cmd.last_address;
        #var sz = parseInt(self.term.argv[2]);
        sz=256
        #if (isNaN(sz)) sz = self.dump_cmd.last_length;
        #self.dump_cmd.last_length = sz;
        #mem = self.runner.cpu.memory;
        mem = self.cpu.memory
        width=16
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
          
            print ("{:04X}: {} | {}".format(from_, bytes_, chars_)+'')
            #print (from_, bytes_, chars_)
            #self.term.write("%04X: %s | %s".format(from, bytes, chars));
            #self.term.newLine();
            
            sz -= chunk_sz;
            from_ = (from_ + chunk_sz) & 0xffff;
    ##self.dump_cmd.last_address = from_;
    def cpu_cmd (self,arg):
        cpu = self.cpu;
        mem = cpu.memory;
        #self.term.write("PC=%04X A=%02X F=%s%s%s%s%s HL=%04X DE=%04X BC=%04X SP=%04X"
       
        print ( 'PC={:04X} A={:04X} F={}{}{}{}{} HL={} DE={:04X} BC={:04X} SP={:04X}'.format(  cpu.pc, cpu.a(), 
                      ("C" if cpu.cf else "-"),
                      ("P" if cpu.pf else "-"),
                      ("H" if cpu.hf else "-"),
                      ("Z" if cpu.zf else "-"),
                      ("S" if cpu.sf else "-"),
                      cpu.hl(), cpu.de(), cpu.bc(), cpu.sp) )
    #self.term.newLine();
    def write_byte_cmd (self,cpu):
        mem=cpu.memory
        self.term.write("%04X: %02X -> %02X".format(addr, mem.read_raw(addr), ch));
        #if (self.term.argc < 3) { self.term.write("?"); return; }
        #var addr = parseInt(self.term.argv[1]);
        #if (isNaN(addr)) addr = 0;
        addr =0x8000
        for i in range(addr+32):
        #for (var i = 2; i < self.term.argc; ++i) {
        #var ch = parseInt(self.term.argv[i]);
        #if (isNaN(ch)) break;
            ch=0xEE
              #
              # print ("{:04X}: {} | {}".format(hex(from_)[2:], bytes_, chars_)+'')
            print ("{}%04X: %02X -> %02X{}".format(addr, mem.read_raw(addr), ch));
              #self.term.newLine()
              #print ("{}: {} | {}".format(hex(from_)[2:], bytes_, chars_)+'')
            print("%04X: %02X -> %02X".format(addr, mem.read_raw(addr), ch))
            mem.write_raw(addr, ch);
            addr=addr+1;
            cpu.memory=mem
    
        return cpu
    def load_cmd(self,arg):
        mem=self.cpu.memory
        if len(arg)>1:
            fl=parse_rk86_binary(arg[1])
        else:
            fl=parse_rk86_binary('KAKVAS.GAM')
        print ('Loading file {} size'.format(fl['size']) )
        mem.load_file(fl)
    def parseInt (self,ar):
        ar=ar.lower().lstrip('0x')
        try:
            a=int(ar,16)
        except:
            a=None
        return a

