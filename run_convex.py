#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
try:
    while True:
        f = f.add(R2Point())
        a = [
            R2Point(0.0, 0.0),
            R2Point(0.0, 3.0),
            R2Point(3.0, 0.0),
            R2Point(3.0, 3.0)
        ]
        print(f"S = {f.area()}, P = {f.perimeter()}, C = {f.cvad(a)}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
