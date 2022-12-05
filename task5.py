# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

num1 = ""
num2 = ""
with open('file5_1.txt', 'r') as file:
    for line in file:
        num1 = line
with open('file5_2.txt', 'r') as file:
    for line in file:
        num2 = line

dict1 = {}
dict2 = {}
num1 = num1.split(" = ")[0]
num2 = num2.split(" = ")[0]
num1_list = num1.split(" + ")
num2_list = num2.split(" + ")

for i in range(len(num1_list)):
    if num1_list[i].count("x^"):
        dict1[int(num1_list[i].split("^")[1])] = int(num1_list[i].split("*")[0])
    elif num1_list[i].count("x"):
        dict1[1] = int(num1_list[i].split("*")[0])
    else:
        dict1[0] = int(num1_list[i])
print(dict1)

for i in range(len(num2_list)):
    if num2_list[i].count("x^"):
        dict2[int(num2_list[i].split("^")[1])] = int(num2_list[i].split("*")[0])
    elif num2_list[i].count("x"):
        dict2[1] = int(num2_list[i].split("*")[0])
    else:
        dict2[0] = int(num2_list[i])
print(dict2)

max_index = 0
for key in dict1.keys():
    if max_index < key:
        max_index = key
for key in dict2.keys():
    if max_index < key:
        max_index = key

dict3 = {}
for i in range(max_index, -1, - 1):
    if i in dict1:
        if i in dict2:
            dict3[i] = dict1[i] + dict2[i]
        else:
            dict3[i] = dict1[i]
    elif i in dict2:
        dict3[i] = dict2[i]
print(dict3)

sum = []
for i in range(max_index, -1, - 1):
    if i in dict3:
        if i == 1:
            sum.append(str(dict3[i]) + "*x")
        elif i == 0:
            sum.append(str(dict3[i]))
        else:
            sum.append(str(dict3[i]) + "*x^" + str(i))

with open('file5_3.txt', 'w') as file:
    print(*sum, file=file, sep=' + ', end=' = 0\n')
