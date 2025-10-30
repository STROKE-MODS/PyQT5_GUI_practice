try:
    b = int(input("Enter the number you want the table of : "))
    list = [f"{b} X {i} = {b*i}\n"  for i in range(1,11)]

    print(list)
    with open("Tables.txt","a") as f:
        for i in list:
            f.write(i)

except Exception as e:
    print(e)