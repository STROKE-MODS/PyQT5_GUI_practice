
with open("2.txt","r") as f:
    d = f.read()


if ("donkey" in d):
    d = d.replace("donkey","####")

with open("2.txt","w") as f:
    f.write(d)

print(d)
