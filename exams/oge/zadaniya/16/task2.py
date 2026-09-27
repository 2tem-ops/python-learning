amount = int(input("Enter amount of numbers: "))
total = 0

for i in range(amount):
    number = int(input("Number: "))
    if 99 < number < 1000:
        if number % 7 == 0:
            total += number

print(f"Sum: {total}")
