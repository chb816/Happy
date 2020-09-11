def countdown(n):
    def realdown():
        nonlocal n
        n = n -1
        return n
    return realdown

def countdown2(n):
    
    return lambda n : n-1

n=0    
n = int(input())



c = countdown2(n)


for i in range(n) :
    print(c(n), end=' ')