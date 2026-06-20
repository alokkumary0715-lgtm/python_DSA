class complex:
    def __init__(self, imag=0, real=0):
        self.imag = imag
        self.real = real

    def __str__(self):
        return ("hi my name is")

    def conjucate(self):
        imag = self.imag* -1
        print(f"{self.real}+{self.imag}i")


# cn = complex(3,5)
cn = complex(3,-5) # here when we are giviing - what we get is
"""so to solve that issue we use magic method (dundur) which is __str__ this gets called when we use  print"""
# cn.real,cn.imag
# print(cn)
# cn.conjucate
print(cn)