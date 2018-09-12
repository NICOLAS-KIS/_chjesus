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
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove()
        self.vm = Moves.VerticalMove()
        self.dm = Moves.DiagonalMove()
        self.add(self.hm)
        self.add(self.vm)
        self.add(self.dm)

class Alphil(Piece):
    def __init__(self):
        self.moves = list()
        self.result = list()
        self.dm = Moves.DiagonalMove()
        self.add(self.dm)

class Tower(Piece):
    def __init__(self):
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove()
        self.vm = Moves.VerticalMove()
        self.add(self.hm)
        self.add(self.vm)
    def move(self,i, f):
        super(Tower, self).move(i, f)
        return self.result[0][0] != self.result[1][0]


class Horsi(Piece):
    def __init__(self):
        self.moves = list()
        self.result = list()
        self.hm = Moves.HorizontalMove(1)
        self.vm = Moves.VerticalMove(2)
        self.add(self.hm)
        self.add(self.vm)

    def move(self,i, f):
        super(Horsi, self).move(i,f)
        return self.result


q = Queen()
print(q.move([1,1],[3,4]))

t = Tower()
print(t.move([1,1],[4,1]))

a = Alphil()
a.move([2,2],[6,6])


h = Horsi()
print(h.move([2,2],[5,3]))