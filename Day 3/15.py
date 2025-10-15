class Animals:
    def show_case_Animals(self):
        print("There are various types of animals  like :\n\t1.Wildlife\n\t2.Pets\n\t3.Stray")
class Pets(Animals):
    def show_case_Pets(self):
        print("In pets there are different types of animals: \n\t1.Dogs\n\t2.Cats\n\t3.Birds")
class Dogs(Pets):
    def __init__(self):
        self.name = input("Enter the name of your dog : ")
    def barking(self):
        print(f"{self.name} is barking.")

print("Hello there !!")
known = Animals()
get = Pets()
known.show_case_Animals()
choosing = input("Enter what you want to choose  : ")
if(choosing == "pets"):
    get.show_case_Pets()
choose = input("Enter what you want to choose  : ")
if(choose == "dogs"):
    petting = Dogs()
    name= input("Enter what do you want to do with your dog? ")
    petting.barking()



    
