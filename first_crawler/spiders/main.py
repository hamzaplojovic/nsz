with open("index.txt") as f:
        data = f.readlines()
        with open("index2.txt", 'w') as f:
                f.write(str(data))