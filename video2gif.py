#!/usr/bin/env python
import os
import sys

DEFAULT_RATIO = 15

if len(sys.argv)>1:
    args = sys.argv[1].split('.')
    file = '.'.join(args[:-1])
    extension = args[-1]
else:
    print("You must give at least file as an argument.")

if len(sys.argv)>2:
    ratio = sys.argv[2]
else:
    ratio = DEFAULT_RATIO

if len(sys.argv)>3:
    pass

print(f"file is {file}")
print(f"extension is {extension}")

cmd = f"ffmpeg -i {file}.{extension}"

cmd += f" -r {ratio}"

cmd += f" {file}.gif"

os.system(cmd)
