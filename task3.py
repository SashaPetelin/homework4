# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

lst = [1,1,2,4,5,6,7,7,8]

excep = list({n for n in lst if lst.count(n) > 1})   # ищем повторяющиеся элементы и заносим их в отдлеьный список
print(excep)

lst1 = []
for i in range(len(lst)):
    if lst[i] not in excep:     # если элемента из исходного списка нет в списке с исключениями, то записываем его в ответ
        lst1.append(lst[i])
print(lst1)


