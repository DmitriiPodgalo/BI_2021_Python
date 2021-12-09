#!/usr/bin/env python3

import os


PATH = os.environ['PATH'].split(':')[0]
FILES = ['wc.py', 'ls.py', 'sort.py', 'rm.py', 'grep.py', 'cat.py', 'tail.py', 'mkdir.py']

for file in FILES:
    path = os.path.join(PATH, file)
    with open(file) as inf, open(path, 'w') as ouf:
        ouf.write(inf.read())
        os.chmod(path, 0o777)

print('Files added to', PATH)
