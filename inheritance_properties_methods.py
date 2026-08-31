class demo:
    a = 1
    b = 2
    def abc(self):
        print("abc")
class sample(demo):
    c = 3
    d = 4
    def cde(self):
        print("cde")
c1 = sample()
print(c1.a)
print(c1.b)
print(c1.c)
print(c1.d)
c1.abc()
c1.cde()