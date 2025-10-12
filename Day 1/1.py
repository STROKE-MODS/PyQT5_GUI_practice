for z in range(2,21):
    with open(f"tables/{z}_table.txt","a") as f:
        for i in range(1,11):
            f.write(f"{z} X {i} = {z*i}\n")
