amount = int(input("Количество чисел: "))
counter = 0

for i in range(amount):
    number = int(input("Введите число: "))
    if number % 4 == 0 and number % 7 != 0:
        counter += 1

print(f"Вывод: {counter}")