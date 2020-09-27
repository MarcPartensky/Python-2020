#!/usr/bin/env python
class Salut:
    def __init__(self, bonjour):
        self.bonjour = bonjour

class Salut2:
    def __init__(self, b1njour):
        self.b1njour = b1njour

s = Salut('truc')
print(s.bonjour)

s = Salut2('machin')
print(s.b1njour)
