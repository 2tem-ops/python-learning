amount = int(input("Количество чисел: "))
counter = 0

for i in range(amount):
    number = int(input("Число: "))
    if number <= 30000:
        if number % 6 == 0:
            counter += 1

print(f"Количество чисел кратных 6: {counter}")
