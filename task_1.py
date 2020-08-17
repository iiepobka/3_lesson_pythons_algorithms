# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

divisible = [i for i in range(2, 100)]
dividers = [x for x in range(2, 10)]

for number in dividers:
    count = 0
    for n in divisible:
        if n % number == 0:
            count += 1
    print(f'В диапазоне натуральных чисел от 2 до 99 на {number} без остатка делиться {count} чисел')
