# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.
from random import randint

COUNT_ITEMS = 10
START_ITEMS = -100
STOP_ITEMS = 100

my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]
print(my_list)

max_negative_item = -1
stop = 0

while stop == 0:
    for n, i in enumerate(my_list):
        if max_negative_item == i:
            index = n
            stop = 1
            print(f'Максимальный отрицательный элемент в массиве: {max_negative_item}. Его индекс: {index}')
    else:
        max_negative_item -= 1
