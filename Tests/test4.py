class Test:
    def __init__(self):
        self.a = 234
    def __getattribute__(self, att):
        return 2


t = Test()
print(t.asdfa)
