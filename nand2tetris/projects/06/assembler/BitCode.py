#!/usr/local/bin/python3

# generate bitcode and output it 16 bit instructions per line

class Code(object):
    def __init__(self):
        pass

    def gen_a(self, addr):
        return '0' + self._bits(addr).zfill(15)

    def gen_c(self, dest, comp, jmp):
        return '111' + self.comp + self.dest(dest) + self.jmp(jmp)

    _dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD', 'DM','ADM']
    def dest(self, d):
        return self._bits(self._dest_codes.index(d).zfill(3))

    _comp_codes = {'0':'0101010',  '1':'0111111',  '-1':'0111010', 'D':'0001100', 
                    'A':'0110000',  '!D':'0001101', '!A':'0110001', '-D':'0001111', 
                    '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110', 
                    'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111', 
                    'D&A':'0000000','D|A':'0010101',
                    '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx',   '':'xxxxxxx', 
                    'M':'1110000',  '':'xxxxxxx',   '!M':'1110001', '':'xxxxxxx', 
                    '-M':'1110011', '':'xxxxxxx',   'M+1':'1110111','':'xxxxxxx', 
                    'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111', 
                    'D&M':'1000000', 'D|M':'1010101'}

    def comp(self, c):
        return self._comp_codes[c]

    _jmp_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def jmp(self, j):
        return self._bits(self._jmp_codes.index(j)).zfill(3)

    def _bits(self, n):
        return bin(int(n))[2:]
