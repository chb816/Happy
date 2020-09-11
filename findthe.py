munja = str(input())

munja = munja.replace(',','')

munjalist = munja.split()

cnt = 0

for i in munjalist:
    if i == 'the' :
        cnt = cnt + 1

print(cnt)