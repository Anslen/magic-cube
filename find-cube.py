import pickle
import numpy as np
from cube import Cube
from vector import Vector

def d3()->list[Cube]:
    axis = [list() for i in range(3)]
    blanket = [0 for i in range(2)]
    for i in range(3):
        for each in [-1,0,1]:
            new = blanket.copy()
            new.insert(i,each)
            axis[i].append(np.array(new))

    locts = list()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                locts.append(axis[0][i] + axis[1][j] + axis[2][k])
    
    drcts = list()
    blanket = [0 for i in range(2)]
    for i in range(3):
        for each in [-1,1]:
            new = blanket.copy()
            new.insert(i,each)
            drcts.append(np.array(new))

    cubes = list()
    for loct in locts:
        for drct in drcts:
            cubes.append(Cube(Vector(loct),Vector(drct),0))

    i = 0
    while i < len(cubes):
        j = i + 1
        while j < len(cubes):
            if ((cubes[i].loct + cubes[i].drct) == cubes[j].loct):
                if ((cubes[j].loct + cubes[j].drct) == cubes[i].loct):
                    cubes.pop(j)
                    cubes.pop(i)
                    break
            j += 1
        else:
            i += 1
    print(len(cubes))
    for each in cubes:
        print(each)

def d4()->list[Cube]:
    axis = [list() for i in range(4)]
    blanket = [0 for i in range(3)]
    for i in range(4):
        for each in [-1,0,1]:
            new = blanket.copy()
            new.insert(i,each)
            axis[i].append(np.array(new))

    locts = list()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for m in range(3):
                    locts.append(axis[0][i] + axis[1][j] + axis[2][k] + axis[3][m])
    
    drcts = list()
    blanket = [0 for i in range(3)]
    for i in range(4):
        for each in [-1,1]:
            new = blanket.copy()
            new.insert(i,each)
            drcts.append(np.array(new))

    cubes = list()
    for loct in locts:
        for drct in drcts:
            cubes.append(Cube(Vector(loct),Vector(drct),0))

    i = 0
    while i < len(cubes):
        j = i + 1
        while j < len(cubes):
            if ((cubes[i].loct + cubes[i].drct) == cubes[j].loct):
                if ((cubes[j].loct + cubes[j].drct) == cubes[i].loct):
                    cubes.pop(j)
                    cubes.pop(i)
                    break
            j += 1
        else:
            i += 1
    print(len(cubes))
    for each in cubes:
        print(each)

if __name__ == '__main__':
    d4()
