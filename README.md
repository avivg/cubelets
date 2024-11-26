Given 6 white cubes with 1 side painted black and 1 all-white cube,
1 cube is picked at random and rolled. After rolling, all visible
sides are white. What are the chances of the bottom side being black?

Naively - bottom is black if one of the black painted cubes were
initially picked - so 6/7 chance, but:

Define:
```
  B = A cube with a black face was selected.
  W = A cube with all white sides was selected.
  Q = Bottom side is black after rolling.
  R = All visible sides are white after rolling.
```
We are interested in `P(Q|R)`

```
P(Q|R) = P(Q+R) / P(R)
```

Note that: 
```
P(R) = P(Q+R) + P(W) = P(Q+R) + 1/7
```
So just need `P(Q+R)`:
```
P(Q+R) = P(B) * P(roll black face down)
       = 6/7 * 1/6 = 1/7
```
So:
```
P(Q|R) = 1/7 / (1/7 + 1/7) = 1/2
```
🤯
