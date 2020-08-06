class Test:
    attributdeclasse = 'attributdeclasse'

    def __init__(self):
        self.attributdinstance = 'attributdinstance'

    def methodedinstance(self):
        return self.attributdinstance

    @classmethod
    def methodedeclasse(cls):
        return cls.attributdeclasse

    @staticmethod
    def methodestatique():
        return 'methodestatique'

    @property
    def propriete(self):
        return 'propriete'

t = Test()
print(t.attributdinstance)
print(t.methodedinstance())
print(t.propriete)

print(Test.attributdeclasse)
print(Test.methodedeclasse())
print(Test.methodestatique())
