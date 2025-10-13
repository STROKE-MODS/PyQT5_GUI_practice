class Calculator:
    Number = 0
    def square(self,number):
        print(f"The square of {number} :",(number **2))    
    def square_root(self,number):
        print(f"The square root of {number} is : {number**(1/2)}")
    def cube(self,number):
        print(f"The cube of {number} is : {number**3}")
calculation = Calculator()
calculation.Number = float(input("Enter the number : "))
work = input("What do you want to do ?\n---->")
if (work == "square"):
    calculation.square(calculation.Number)
if (work == "squareroot"):
    calculation.square_root(calculation.Number)
if (work == "cube"):
    calculation.cube(calculation.Number)