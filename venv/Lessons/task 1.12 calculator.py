a = float(input())
b = float(input())
z = input()

if z == '+':
    print(a + b)

elif z == '-':
    print(a - b)

elif z == '/':
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")

elif z == '*':
    print(a * b)

elif z == 'mod':
    if b != 0:
        print(a % b)
    else:
        print("Деление на 0!")

elif z == 'pow':
    print(a ** b)

elif z == 'div':
    if b != 0:
        print(a // b)
    else:
        print("Деление на 0!")
