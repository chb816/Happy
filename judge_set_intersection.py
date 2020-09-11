f = int(input())
t = int(input())

a = {i for i in range(f+1) if i > 0 and f % i == 0}
b = {j for j in range(t+1) if j > 0 and t % j == 0}

print(a,b)
divisor = a&b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)

