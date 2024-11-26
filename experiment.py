"""
Trying out the cubelet thing
"""

import random as rnd

class Face:
    BLACK=1
    WHITE=2
    def __init__(self, val):
        self._val = val
    def val(self):
        return self._val

class Cube:
    def __init__(self, wfaces: int, bfaces: int):
        self.wfaces = wfaces
        self.bfaces = bfaces

    def __str__(self):
        return f'Cube<W:{self.wfaces}, B:{self.bfaces}>'
    
    def throw(self) -> int:
        """returns the bottom face"""
        sel = rnd.randint(0, self.bfaces + self.wfaces - 1)
        if sel < self.wfaces:
            return Face.WHITE
        return Face.BLACK

def main():
    cubes = [Cube(5, 1)] * 6 + [Cube(6,0)]
    valid_games = 0
    black_bottom_games = 0
    for _ in range(1000):
        c = rnd.choice(cubes)
        res = c.throw()
        # print(f'selected {c}, black on bottom: {res == Face.BLACK}')
        if res == Face.BLACK:
            valid_games += 1
            black_bottom_games += 1
        elif c.bfaces == 0:
            valid_games += 1
    print(f'valid games: {valid_games}, black on bottom: {black_bottom_games}, ratio: {black_bottom_games / valid_games}')

if __name__ == '__main__':
    main()
