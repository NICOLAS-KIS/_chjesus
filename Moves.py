class Moves():
    def __init__(self,limit = 16):
        self.limit = limit

    def move(self, i, f):
        pass

class HorizontalMove(Moves):
    def move(self, i, f):
        return [f[0]-i[0] == 0, abs(f[1] - i[1]) <= self.limit] # la primera corrobora que se mueva horizontalmente
                                                                # la segunda corrobora que los movimientos sean menores a los
                                                                # posibles
class VerticalMove(Moves):
    def move(self, i, f):
        return [f[1]-i[1] == 0, abs(f[0]-i[0]) <= self.limit]

class DiagonalMove(Moves):
    def move(self, i, f):
        return all([(abs(f[1] - i[1]) == abs(f[0] - i[0])),  abs(f[1] - i[1]) <= self.limit,  abs(f[0] - i[0]) <= self.limit])

