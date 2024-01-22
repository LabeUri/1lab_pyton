def proste(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
start, end = map(int, input("Напишіть початок і кінець діапазону через пробел: ").split())
print(f"Прості числа в діапазоні від {start} до {end}:", [num for num in range(start, end + 1) if proste(num)])