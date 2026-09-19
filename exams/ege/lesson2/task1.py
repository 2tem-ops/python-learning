# Цикл for. Ввести 5 чисел через цикл, посчитать сумму и сколько из них положительных

total = 0
count = 0

for i in range(5):
    x = int(input())
    total += x
    if x > 0:
        count += 1

print("Сумма:", total)
print("Положительных:", count)