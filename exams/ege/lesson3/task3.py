# Функция приветствия
def introduce(name, age=17):
    print("Привет, это " + name + " ей " + str(age) + " лет. ")

introduce('Анастасия', 18)
introduce('Таня')
introduce('Саша')


# Функция is_prime (простые числа делятся только на 1 и на себя)
def is_prime(x):
    return all([x % d != 0 for d in range(2, x)])

print(is_prime(15))

x = 5
if is_prime(x):
    print("простое")