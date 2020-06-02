import pexpect
child = pexpect.spawn('touch osef')
child.sendline('ls')
child.expect(pexpect.EOF)
print(child.before)
child.sendline('rm osef')
