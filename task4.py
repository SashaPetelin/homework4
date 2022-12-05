# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена 
# и записать в файл многочлен степени k.

#     *Пример:* 

#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

import random

k = int(input("Введите значение степени k: "))
while k < 1:
    print("Степень должна быть натуральной!")
    k = int(input("Введите значение степени k: "))

lst_coef =[]
for i in range(k+1):
    lst_coef.append(random.randint(0,101))

str = ""
for i in range(len(lst_coef)):
    if i != len(lst_coef)-1 and i != len(lst_coef)-2:
        str+=f'{lst_coef[i]}x^{len(lst_coef)-i-1}'
        if lst_coef[i] == 0:
            str+=""
        elif lst_coef[i+1] != 0:
            str+= ' + '
    elif i == len(lst_coef)-2:
        str+=f'{lst_coef[i]}x'
        if lst_coef[i] == 0:
            str+=""
        elif lst_coef[i+1] != 0:
            str+= ' + '
    elif i == len(lst_coef)-1 and lst_coef[i] != 0:
        str+=f'{lst_coef[i]} = 0'
    elif i == len(lst_coef)-1 and lst_coef[i] == 0:
        str+= ' = 0'
print(str)

with open('file_t4.txt','w') as data:
    data.write(str)