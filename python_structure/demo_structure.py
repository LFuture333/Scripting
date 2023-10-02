from collections import namedtuple



Point = namedtuple('Point', ['x', 'y'])

npt= Point(x=0.5, y=9.5)

print(npt.x)

print(npt)