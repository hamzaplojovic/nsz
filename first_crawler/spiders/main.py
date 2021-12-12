with open("index.txt") as f:
        data = f.readlines()
        data2 = str(data)
        with open("index2.txt", 'w') as f:
                f.write(str(data2))
