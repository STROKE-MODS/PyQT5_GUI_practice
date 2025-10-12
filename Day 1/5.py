with open ("4.txt","r") as f:
    d = f.read()

with open("this.txt","a") as f:
    f.write(d)