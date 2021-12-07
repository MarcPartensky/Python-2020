#!/usr/bin/env python

# from subprocess import Popen, PIPE

# p = Popen("/usr/bin/zsh", stdin=PIPE)
# p.communicate(b"echo a")
# p.communicate(b"cd ..")
# p.communicate(b"echo b")
# p.kill()

from __future__ import print_function, unicode_literals
import subprocess

shell = subprocess.Popen(
    ["/bin/sh"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True,
)

shell.stdin.write("echo a")
print(shell.stdout.raw)
shell.stdin.write("echo b")
print(shell.stdout.raw)
print(shell.stdout)
shell.stdin.close()
