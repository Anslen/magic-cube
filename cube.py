from vector import Vector
class Cube:
    __slots__ = ['loct','drct']
    def __init__(self,loct:Vector,drct:Vector):
        """
        loct:表示位置
        drct:表示方向
        """
        self.loct = loct
        self.drct = drct

    def __str__(self):
        return 'loct:' + self.loct.__str__()[6:] + ' drct:' +  self.drct.__str__()[6:]
    __repr__ = __str__

if __name__ == '__main__':
    c = Cube(Vector([1,1,-1]),Vector([0,0,1]))
    print(c)
