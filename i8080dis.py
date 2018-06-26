tab_opcode={
0X00:{'cmd':'NOP','length':1},
0X08:{'cmd':'NOP?','length':1,'bad':True},
0X10:{'cmd':'NOP?','length':1,'bad':True},
0X20:{'cmd':'NOP?','length':1,'bad':True},
0X18:{'cmd':'NOP?','length':1,'bad':True),
0X28:{'cmd':'NOP?','length':1,'bad':True},
0X30:{'cmd':'NOP?','length':1,'bad':True},
0X38:{'cmd':'NOP?','length':1,'bad':True},

0X01:{'cmd':'LXI','length':3,'arg1':'B','arg2':'im16','data2':True},
0X02:{'cmd':'STAX','length':1,'arg1':'B'},
0X03:{'cmd':'INX','length':1,'arg1':'B'},
0X04:{'cmd':'INR','length':1,'arg1':'B'},
0X05:{'cmd':'DCR','length':1,'arg1':'B'},
}
def function i8080_disasm (binary):
    opcode = binary[0]
    imm8 = binary[1]
    imm16 = imm8 | (binary[2] << 8)
    #var cmd, length, arg1, arg2, code, data1, data2, bad;

    fmt8 = "%02X"
    fmt16 = "%04X"

    imm8 = fmt8.format(imm8)
    imm16 = fmt16.format(imm16)        
    if opcode==0x00:  
        cmd = "NOP"
        length = 1
    elif opcode==0x00 :
        length = 1 
        bad = true
        brea
