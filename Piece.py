import Moves

dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class Piece:
    def __init__(self, color):
        super(Piece, self).__init__()
        self.moves = list()
        self.color = color

    def add(self,move):
        self.moves.append(move)

    def checkMove(self,table, i, f):
        return True

    def move(self,i, f):
        self.result = list()
        for m in self.moves:
            self.result.append(m.move(i,f))
        return all(self.result)

class Queen(Piece):
    def __init__(self):
        super().__init__()
        self.moves = list()
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
        self.moves = list()
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
        self.moves = list()
        self.result = list()
        self.dm = Moves.DiagonalMove()
        self.add(self.dm)
    def checkMove(self,table, i, f):
        inicio = dic.index(i[0]) + 1
        final = dic.index(f[0]) + 1
        if inicio > final:
            inicio, final = final, inicio
        columna  = int(i[1])
        for v in dic[inicio:final]:
            if table[v][columna] is not '_': return False
            columna += 1
        else: return True
    def getName(self):
        return "Alphil"
    def move(self,i, f):
        super(Alphil, self).move(i, f)
        return self.result

class Tower(Piece):
    def __init__(self):
        self.moves = list()
        self.hm = Moves.HorizontalMove()
        self.vm = Moves.VerticalMove()
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "Tower"
    def checkMove(self,table, i, f):
        if i[0] == f[0]:
            for v in table[i[0]][int(i[1]):int(f[1])]:
                if v is not '_': return False
        elif i[1] == f[1]:
            inicio = dic.index(i[0]) + 1
            final = dic.index(f[0]) + 1
            for v in dic[inicio:final]:
                if table[v][int(i[1])] is not '_': return False
    def move(self,i, f):
        super(Tower, self).move(i, f)
        return self.result[0][0] != self.result[1][0]


class Horsi(Piece):
    def __init__(self):
        self.moves = list()
        self.hm = Moves.HorizontalMove(2)
        self.vm = Moves.VerticalMove(2)
        self.add(self.hm)
        self.add(self.vm)
    def getName(self):
        return "Horsi"
    def move(self,i, f):
        super(Horsi, self).move(i,f)
        if any([self.result[0][0],self.result[1][0]]): return False #valido que no haya movimiento puro vertical u horizontal
        else: return all([self.result[0][1],self.result[1][1]]) # tengo que reconstruir el movimiento vertical y
                                                                # horizontal en este caso

class Pawn(Piece):
    def __init__(self):
        self.moves = list()
        self.hm = Moves.HorizontalMove(2)
        self.add(self.hm)
    def getName(self):
        return "Pawn"
    def move(self,i, f):
        super(Pawn, self).move(i, f)
        print(self.result)
        return all(*self.result)

"""
print("    ", *[1,2,3,4,5,6,7,8])
for key, values in table.table.items():
    print(key,": ",*values)
#print(self.table)
"""

"""
print("    ", *[1,2,3,4,5,6,7,8])
for key, values in table.table.items():
    print(key,": ",values.getName())
"""