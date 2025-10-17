class Complex:
    def __init__(self,length,width):
        self.real1 = length
        self.imaginary1 = width
    

    def __add__(self,other):
        return Complex(self.real1 + other.real1, self.imaginary1 + other.imaginary1)
    
    def __mul__(self,other):
        real_part = ((self.real1*other.real1) - (self.imaginary1*other.imaginary1))
        imaginary_part = ((self.real1*other.imaginary1) + (self.imaginary1*other.real1))
        return Complex(real_part,imaginary_part)

    def __str__(self):
        return (f"The product of the two complex number is  : {self.real1-self.imaginary1}")
    def __str__(self):
        return (f"{self.real1} + {self.imaginary1}i")
    


b  = Complex( 5,8)
c =  Complex(9,5)

d = b+c
e = b*c
print(d)
print(e)