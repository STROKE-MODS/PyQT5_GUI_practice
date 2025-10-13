with open("4.txt","r") as f:
    d = f.read()
with open("this.txt","r") as f:
    e = f.read()

if (d==e):
    print("Both file data is same.")
else:
    print("File data is different.")
    