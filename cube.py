from vector import Vector
class Cube:
    __slots__ = ['loct','drct','color']
    def __init__(self,loct:Vector,drct:Vector,color:int):
        """
        loct:表示位置
        drct:表示方向
        color:颜色信息
        """
        self.loct = loct
        self.drct = drct
        self.color = color

    def __str__(self):
        return 'loct:' + self.loct.__str__()[6:] + ' drct:' +  self.drct.__str__()[6:]\
        + f' color:{self.color}'
    __repr__ = __str__

if __name__ == '__main__':
    c = Cube(Vector([1,1,-1]),Vector([0,0,1]))
    print(c)
