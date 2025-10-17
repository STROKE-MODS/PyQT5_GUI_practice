class WHat_to_do:
    def __init__(self):
        self.called = "Himanshu Singh"
    @property
    def Name(self):
        my = self.called.split(" ")
        fname = my[0]
        # lname = my[1]
        return fname
    @Name.setter
    def Name(self,Value):
        self.called = Value
        print(f"The Name is  {self.fname}")

ho = WHat_to_do()
print(ho.Name)

ho.Name = "Rohan Kumar"
print(ho.Name)