x, y = map(int, input().split())

def calc(x, y) :
    sum = x+y
    mis = x-y
    mul = x*y
    div = x/y
    return sum, mis, mul, div

sum, mis, mul, div = calc(x, y)
print('+ : {0}, - :{1}, * :{2}, / :{3}'.format(sum, mis, mul, div))
