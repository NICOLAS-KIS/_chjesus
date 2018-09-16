from Piece import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

q = Queen()
k = King()
t = Tower()
a = Alphil()
h = Horsi()
p = Pawn()

class Table():
    def __init__(self):
        self.table = dict()
        self.table = {
              'A': ['_','_','_','_','_','_','_','_']
            , 'B': ['_','_','_','_','_','_','_','_']
            , 'C': ['_','_','_','_','_','_','_','_']
            , 'D': ['_','_','_','_','_','_','_','_']
            , 'E': ['_','_','_','_','_','_','_','_']
            , 'F': ['_','_','_','_','_','_','_','_']
            , 'G': ['_','_','_','_','_','_','_','_']
            , 'H': ['_','_','_','_','_','_','_','_']
            }
        self.init_table = {
              'A': [t,p,'_','_','_','_','_','_']
            , 'B': [h,p,'_','_','_','_','_','_']
            , 'C': [a,p,'_','_','_','_','_','_']
            , 'D': [k,p,'_','_','_','_','_','_']
            , 'E': [q,p,'_','_','_','_','_','_']
            , 'F': [a,p,'_','_','_','_','_','_']
            , 'G': [h,p,'_','_','_','_','_','_']
            , 'H': [t,p,'_','_','_','_','_','_']
            }
    def printtable(self):
        print("    ", *[1, 2, 3, 4, 5, 6, 7, 8])
        for key, values in self.init_table.items():
            print(key, ": ", end=' ')  # ,*[v.getName() for v in values])
            for v in values:
                if v == '_':
                    print(v, end=' ')
                else:
                    print(v.getName()[0], end=' ')
            print('')


t = Table()
t.printtable()

array = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

while True:
    _from_let = input()
    _to_let = input()

    _from = [array[_from_let[0]] - 1, int(_from_let[1]) - 1] #paso los valores a indiced de arrays
    _to = [array[_to_let[0]] - 1, int(_to_let[1]) - 1] #paso los valores a indiced de arrays

    piece = t.init_table[_from_let[0]][int(_from_let[1])-1]

    if piece.move(_from, _to) and piece.checkMove(t.init_table, _from_let, _to_let):
        t.init_table[_from_let[0]][_from[1]] = '_'
        t.init_table[_to_let[0]][_to[1]] = piece


    t.printtable()