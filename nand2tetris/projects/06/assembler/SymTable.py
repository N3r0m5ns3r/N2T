#!/usr/local/bin/python3

class SymTable(object):
    def __init__(self):
        self._symbols \
            = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
               'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
               'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
               'SCREEN':0x4000, 'KBD':0x6000}

        def add_entry(self, symb, address):
            self._symbols[symb] = address
        def contains(self, symbol):
            return symb in self._symbols

        def get_address(sel, symb):
            return self._symbols[symb]
