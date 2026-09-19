# Файлы, генераторы, max() min(). Найти мин макс и среднюю температуру из файла

file = open("temps.txt")

data = [int(line) for line in file]

print(min(data))
print(max(data))
print(sum(data) / len(data))