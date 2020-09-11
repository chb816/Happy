sale = str(input())
sale = sale.split(';')
sale.sort(reverse=True)
for i in sale :
    i = int(i)
    print('{0:>9,}'.format(i))

