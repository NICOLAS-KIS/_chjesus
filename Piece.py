import Moves

class Piece:
    def __init__(self):
        self.moves = list()
        self.result = list()

    def add(self,move):
        self.moves.append(move)

    def move(self,i, f):
        for m in self.moves:
            self.result.append(m.move(i,f))
        return all(self.result)

class Queen(Piece):
    def __init__(self):
        self.initposition = 'E1'
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove()
        self.vm = Moves.VerticalMove()
        self.dm = Moves.DiagonalMove()
        self.add(self.hm)
        self.add(self.vm)
        self.add(self.dm)
    def getName(self):
        return "Queen"

class King(Piece):
    def __init__(self):
        self.initposition = 'D1'
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove(1)
        self.vm = Moves.VerticalMove(1)
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "King"
    def move(self,i, f):
        super(King, self).move(i, f)
        return self.result[0][0] != self.result[1][0]

class Alphil(Piece):
    def __init__(self):
        self.initposition = ['C1','F1']
        self.moves = list()
        self.result = list()
        self.dm = Moves.DiagonalMove()
        self.add(self.dm)
    def getName(self):
        return "Alphil"

class Tower(Piece):
    def __init__(self):
        self.initposition = ['A1','H1']
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove()
        self.vm = Moves.VerticalMove()
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "Tower"
    def move(self,i, f):
        super(Tower, self).move(i, f)
        return self.result[0][0] != self.result[1][0]


class Horsi(Piece):
    def __init__(self):
        self.initposition = ['B1','G1']
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove(1)
        self.vm = Moves.VerticalMove(2)
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "Horsi"
    def move(self,i, f):
        super(Horsi, self).move(i,f)
        return self.result

class Pawn(Piece):
    def __init__(self):
        self.initposition = ['A2','B2','C2','D2','E2','F2','G2','H2']
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove(1)
        self.vm = Moves.VerticalMove(2)
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "Pawn"


import Table
table = Table.Table()

q = Queen()
k = King()
t = Tower()
a = Alphil()
h = Horsi()
p = Pawn()


table.table[k.initposition[0]][int(k.initposition[1])-1] = k.getName()[0]
table.table[q.initposition[0]][int(q.initposition[1])-1] = q.getName()[0]


for i in t.initposition:
    table.table[i[0]][int(i[1])-1] = t.getName()[0]
for i in a.initposition:
    table.table[i[0]][int(i[1])-1] = a.getName()[0]
for i in h.initposition:
    table.table[i[0]][int(i[1])-1] = h.getName()[0]
for i in p.initposition:
    table.table[i[0]][int(i[1])-1] = p.getName()[0]


for key, values in table.table.items():
    print(*values)
#print(self.table)
