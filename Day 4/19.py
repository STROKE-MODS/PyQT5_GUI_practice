class printing:
    def __init__(self,x_axis,y_axis,z_axis):
        self.i = x_axis
        self.j = y_axis
        self.k = z_axis
    
    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")


a = int(input("Enter the points : "))
b = int(input("Enter the points : "))
c = int(input("Enter the points : "))
hello = printing(a,b,c)

print(f"The vector is  : {hello}")