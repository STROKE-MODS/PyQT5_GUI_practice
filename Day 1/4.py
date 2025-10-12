with open("4.txt","r") as f:
    number_of_line = 1

    data = f.readline()
    while (data!=""):
        data = f.readline()
        number_of_line+=1
        if "python" in data:
            print(f"Python is present.\nIn line {number_of_line}")