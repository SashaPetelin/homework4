# Вычислить число Пи c заданной точностью d

# Пример:

#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

pnum = '3, 1 4 1 5 9 2 6 5 3 5'
d = '0.0001'

x,y = d.split(".") 
l = (len(y))

x1,y1 = pnum.split(",")

list1 = y1.split()

def accuracy(n,l):
    lst2 = []
    for i in range (l):
        lst2.append(n[i])
    return (''.join(lst2))

print(f'3,{accuracy(list1,l)}')

