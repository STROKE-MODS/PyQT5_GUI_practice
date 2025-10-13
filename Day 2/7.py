with open("this.txt","r") as f:
    d = f.read()
with open("this.txt","w") as f:
    f.write(" ")

print(f"{d} \n---> This data is been delted from the file")