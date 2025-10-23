
class Imag:
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def __add__(self,other):
        return Imag(self.re+other.re, self.im + other.im)

    def __sub__(self,other):
        return Imag(self.re-other.re,self.im - other.im)

    def __str__(self):
        if self.im >= 0:
            return f"{self.re}+{self.im}i"
        else:
            return f"{self.re}{self.im}i"

a = Imag(2,3)
b = Imag(1,4)

print("a=", a)
print("b=", b)
print("a+b=", a+b)
print("a-b=", a-b)
