import numpy as np
from fractions import Fraction

class Vector:
    __slots__ = ['data','dim','norm',"defined"]
    def __init__(self,array:np.array):
        '''
        n维的向量
        array:用于初始化向量的数组
        '''
        super().__setattr__("defined",False)
        array = np.array(array)
        if array.ndim != 1:
            raise ValueError("需要使用一维数组")
        self.data = array
        self.defined = True

    def __eq__(self, other) -> bool:
        if type(other) != Vector:
            return False
            #不是向量时返回False
        if self.data.shape != other.data.shape:
            return False
            #维数不相等返回False
        return (self.data == other.data).all()
        #每一项数字都相等

    def __ne__(self,other):
        return not self.__eq__(other)

    def __add__(self,other):
        if type(other) != Vector:
            raise TypeError(f"向量不能与{type(other)}相加")
        if self.dim != other.dim:
            raise ValueError("维数相同的向量才能相加")
        return Vector(self.data + other.data)

    def __sub__(self,other):
        if type(other) != Vector:
            raise TypeError(f"向量不能与{type(other)}相减")
        if self.dim != other.dim:
            raise ValueError("维数相同的向量才能相减")
        return Vector(self.data - other.data)
    
    def __mul__(self,other):
        if type(other) is Vector:
            if self.dim != other.dim:
                raise ValueError("维数相同的向量才能相乘")
            return self.data @ other.data
        try:
            new = other * self.data
            return Vector(new)
        except:
            raise TypeError(f'向量不能与{type(other)}相乘')
    __rmul__ = __mul__

    def __bool__(self):
        return bool((self.data == 0).all())
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Vector(-self.data)

    def __str__(self):
        return f'Vector({self.data.__repr__()[7:-2]})'
    __repr__ = __str__

    def __hash__(self):
        return hash(tuple(self.data))

    def __setattr__(self, __name: str, __value) -> None:
        if self.defined == True:
            raise TypeError('Vector类型不可修改')
        super().__setattr__(__name,__value)
        if __name == 'data':
            self.dim = self.data.shape[0]
            self.norm = float(np.sqrt(np.square(self.data).sum()))
            #计算向量的模

def angle(vec1,vec2,cos = True):
    '''
    计算两个向量的夹角
    cos:返回cos值或弧度
    '''
    if (type(vec1) is not Vector) or (type(vec2) is not Vector):
        raise TypeError('angle函数应该接受两个向量')
    result = vec1 * vec2 / (vec1.norm * vec2.norm)
    if cos:
        return result
    else:
        return np.arccos(result)
    
def is_vertical(vec1,vec2):
    if (type(vec1) is not Vector) or (type(vec2) is not Vector):
        raise TypeError('is_vertical函数应该接受两个向量')
    if vec1.dim != vec2.dim:
        raise ValueError('两个向量的维数应该相同')
    return (vec1 * vec2) == 0

def is_parallel(vec1,vec2):
    if (type(vec1) is not Vector) or (type(vec2) is not Vector):
        raise TypeError('angle函数应该接受两个向量')
    if vec1.dim != vec2.dim:
        raise ValueError('两个向量的维数应该相同')
    #筛选错误的输入值
    if ((vec1.data == 0) != (vec2.data == 0)).any():
        return False
    #向量中0的个数或位置不同时返回False
    vec1 = vec1.data[vec1.data != 0]
    vec2 = vec2.data[vec2.data != 0]
    #去除坐标中的0
    return len(np.unique(vec1 / vec2)) == 1

if __name__ == '__main__':
    vec1 = Vector([1,2,3])
    vec2 = Vector([-1,-1,5])
    vec3 = Vector([5,8,4])
