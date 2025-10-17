class Employee :

    def __init__(self,salary = 25000):
        self._salary = salary
    
    @property
    def salary(self):
        return (self._salary + ((self._salary*5)/100))
    
    @salary.setter
    def salary(self,value):
        self._salary = value

e = Employee()

e.salary  = int(input("Enter your salary : "))

print(f"The salary is : {e.salary}")