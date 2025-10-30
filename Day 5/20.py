from random import randint

while(1):
    print("Welcome to the Guess the Number Game .............")
    print("Rules : \n\tA number will be selected from 1-100. You have to Guess it with minimum guess. ")
    number = randint(1,100)
    b = 0
    while(1):
        guessed_number = int(input("Enter the number : "))
        if (guessed_number==number):
            print(f"Congrats you got it correct.\nIn {b} guesses.")
            break
        elif(guessed_number>number):
            print("Guessed number is greater than number.")
        elif(guessed_number<number):
            print("Guessed number is less than the number.")
        b+=1
    break

