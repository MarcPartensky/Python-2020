print('salut')

a = 1

print(a.denominator)


# print(a.to_bytes())
class Salut:

    def __init__(self, truc):
        self.truc = truc 

    def stuff(self) -> dict:
        return {'truc': self.truc}

s = Salut('bidule')

s.truc

b = s.stuff()
wesh = b.pop('truc')
print(wesh.replace('dule', 'de'))
