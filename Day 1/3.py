list =["donkey","gadha","mc","bkl"]

with open("3.txt","r") as f:
    data = f.read()

for word in list:
    if (word in data):
        data = data.replace(word,"#####")

with open("3.txt","w") as f:
    f.write(data)

