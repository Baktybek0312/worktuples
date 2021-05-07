# PROBLEM 72
#
# Удалить из Листа №1 все чётные индексы до 10.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
for i in range(1, 11, 2):
    list1.remove(i)
    print(i)

