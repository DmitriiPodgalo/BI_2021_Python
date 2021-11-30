#!/usr/bin/env python3

import sys


lines = []
for line in sys.stdin:
    lines.append(line)

print(*sorted(lines), sep='')
