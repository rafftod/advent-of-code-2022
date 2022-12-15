import re

import numpy as np


test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

puzzle_input = """Sensor at x=3289936, y=2240812: closest beacon is at x=3232809, y=2000000
Sensor at x=30408, y=622853: closest beacon is at x=-669401, y=844810
Sensor at x=3983196, y=3966332: closest beacon is at x=3232807, y=4625568
Sensor at x=929672, y=476353: closest beacon is at x=-669401, y=844810
Sensor at x=1485689, y=3597734: closest beacon is at x=1951675, y=3073734
Sensor at x=69493, y=1886070: closest beacon is at x=-669401, y=844810
Sensor at x=2146060, y=3999371: closest beacon is at x=2300657, y=4128792
Sensor at x=3228558, y=3890086: closest beacon is at x=3232807, y=4625568
Sensor at x=3031444, y=2295853: closest beacon is at x=2928827, y=2611422
Sensor at x=374444, y=3977240: closest beacon is at x=-888612, y=4039783
Sensor at x=1207660, y=2710720: closest beacon is at x=1951675, y=3073734
Sensor at x=3851310, y=61626: closest beacon is at x=4807592, y=976495
Sensor at x=3195193, y=3022787: closest beacon is at x=2928827, y=2611422
Sensor at x=1784895, y=2111901: closest beacon is at x=1951675, y=3073734
Sensor at x=2894075, y=2427030: closest beacon is at x=2928827, y=2611422
Sensor at x=3301867, y=803327: closest beacon is at x=3232809, y=2000000
Sensor at x=2506616, y=3673347: closest beacon is at x=2300657, y=4128792
Sensor at x=2628426, y=3054377: closest beacon is at x=1951675, y=3073734
Sensor at x=2521975, y=1407505: closest beacon is at x=3232809, y=2000000
Sensor at x=2825447, y=2045173: closest beacon is at x=3232809, y=2000000
Sensor at x=2261212, y=2535886: closest beacon is at x=2928827, y=2611422
Sensor at x=3956000, y=1616443: closest beacon is at x=3232809, y=2000000
Sensor at x=3870784, y=2872668: closest beacon is at x=2928827, y=2611422"""

def main():
    # first_question()
    second_question()
    
def m(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def s(x, y):
    return x[0] * y[0] + x[1] * y[1]

def first_question():
    current_input, ty = puzzle_input, 2000000
    # current_input, ty = test_input, 10
    ps = []
    for line in current_input.split("\n"):
        cs = re.findall(r"[-]?\d+", line)
        ps.append(tuple(map(int, cs)))
    ups = set()
    for p in ps:
        print(p)
        sx, sy, bx, by = p
        md = m((sx, sy), (bx, by))
        for i, y in enumerate(range(sy - md, sy + 1)):
            if y != ty:
                continue
            ups =  ups.union({(x, y) for x in range(sx - i, sx + i + 1) if (x, y) not in ((bx, by), (sx, sy))})
        for i, y in enumerate(range(sy + md, sy, -1)):
            if y != ty:
                continue
            ups = ups.union({(x, y) for x in range(sx - i, sx + i + 1) if (x, y) not in ((bx, by), (sx, sy))})
    print(len([(x, y) for x,y in ups if y == ty]))
            

def second_question():
    current_input = puzzle_input
    minc, maxc = 0, 4000000
    ps = []
    for line in current_input.split("\n"):
        cs = re.findall(r"[-]?\d+", line)
        ps.append(tuple(map(int, cs)))
    for y in range(maxc + 1):
        print(f"{y/4000000:.2%}")
        ranges = []
        for sx, sy, bx, by in ps:
            d = m((sx, sy), (bx, by))
            o = d - abs(sy - y)
            if o < 0:
                continue
            lx = sx - o
            hx = sx + o
            ranges.append((lx, hx))
        ranges.sort()
        q = []
        for low, high in ranges:
            if not q:
                q.append([low, high])
                continue
            qlow, qhigh = q[-1]
            if low > qhigh + 1:
                q.append([low, high])
                continue
            q[-1][1] = max(qhigh, high)
        x = 0
        for low, high in q:
            if x < low:
                print(x * 4000000 + y)
                break
            x = max(x, high + 1)
            if x > maxc:
                break
        
if __name__ == "__main__":
    main()