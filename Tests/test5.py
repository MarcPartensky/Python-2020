import re
import sys

t = ''.join(sys.argv[1:])

p = re.compile(' ( )* ')
t = re.sub(p, ' ', t)

print(t)

p = re.compile(r'(\n)+')
t = re.sub(p, ' ', t)

print(t)

