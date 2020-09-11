def prime_number_generator(start, stop):
    n = start
    while n < stop :
        count = 0
        i = 1
        while i <= n :
            if n%i == 0 :
                count = count + 1
            i = i + 1
        if count == 2  :
            yield n
        n = n + 1

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)

print(type(g))
for i in g :
    print(i, end=' ')
