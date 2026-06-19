class complex:
    def __init__(self, imag=0, real=0):
        self.imag = imag
        self.real = real

    def __str__(self):
        s= f"{self.real}+{self.imag}i"
        return s

    def conjucate(self):
        imag = self.imag* -1
        print(f"{self.real}+{self.imag}i")


cn = complex(3,5)
cn.real,cn.imag
print(cn)
cn.conjucate
print(cn)