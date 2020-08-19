# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.
from random import randint

COUNT_ITEMS = 10
START_ITEMS = -100
STOP_ITEMS = 100

my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]
print(my_list)

max_item = 0
max_item_index = 0
min_item = 0
min_item_index = 0
items_sum = 0

for n, i in enumerate(my_list):
    if max_item < i:
        max_item = i
        max_item_index = n
    elif min_item > i:
        min_item = i
        min_item_index = n

if max_item_index > min_item_index:
    for el in my_list[min_item_index + 1: max_item_index]:
        items_sum += el
else:
    for el in my_list[max_item_index + 1: min_item_index]:
        items_sum += el

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {items_sum}')
