Numerator = float(input("Entert the numerator : "))
Denominator = float(input("Enter the denominator : "))

if (Denominator == 0):
    raise ZeroDivisionError 
    print("The Denominator cant be zero")

print(f"The Divsion answer is : {Numerator/Denominator}")
