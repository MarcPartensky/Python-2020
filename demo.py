class Test:
    attributdeclasse = 'attributdeclasse'

    def __init__(self):
        self.attributdinstance = 'attributdinstance'
        self.proprietedinstance = 'proprietedinstance'

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
        return self.proprietedinstance

    @propriete.setter
    def propriete(self, value):
        self.proprietedinstance = value

    @propriete.deleter
    def propriete(self):
        del self.proprietedinstance




t = Test()
print(t.attributdinstance)
print(t.methodedinstance())
print(t.propriete)
t.propriete = 'proprietemodifie'
print(t.propriete)
print(t.proprietedinstance)
del t.propriete

print(Test.attributdeclasse)
print(Test.methodedeclasse())
print(Test.methodestatique())
