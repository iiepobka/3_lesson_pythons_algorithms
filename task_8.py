# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов
# строк. Программа должна вычислять сумму введенных элементов каждой
# строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.
LINE = 5
matrix = []

for i in range(LINE):
    matrix.append([float(x) for x in (input(f'Введите три числа цифрами '
                                            f'через пробел - элементы {i + 1}-й строки матрицы 5х4: ').split())])

for n, i in enumerate(matrix):
    line_sum = 0
    for j in i:
        line_sum += j
        print(f'{j:<8}', end='')
    matrix[n] += [line_sum]
    print(f'{line_sum:<10}')
