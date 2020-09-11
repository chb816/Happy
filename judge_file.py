with open('hello.txt', 'r') as file :
    for line in file :
        sline = line.split()
        for i in sline :
            if 'c' in i :
                print(i)
