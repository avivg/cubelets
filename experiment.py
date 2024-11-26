"""
Trying out the cubelet thing:
Given 6 white cubes with 1 side painted black and 1 all-white cube,
1 cube is picked at random and rolled. After rolling, all visible
sides are white. What are the chances of the bottom side being black?

Naively - bottom is black if one of the black painted cubes were
initially picked - so 6/7 chance, but:

Define:
  B = A cube with a black face was selected.
  W = A cube with all white sides was selected.
  Q = Bottom side is black after rolling.
  R = All visible sides are white after rolling.

Note that Q => R, so P(R|Q) = 1
We want P(Q|R) = P(Q+R) / P(R).
Note that: P(R) = P(Q+R) + P(W) = P(Q+R) + 1/7
P(Q+R) = P(B) * P(roll black face down)
       = 6/7 * 1/6 = 1/7
So:
P(Q|R) = 1/7 / (1/7 + 1/7) = 1/2
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
