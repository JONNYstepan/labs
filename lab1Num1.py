a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
k = int(input("Введите k: "))
try:
    y = (((a**2)/b**2)+(c**2)*a**2)/(a+b+c*(k-a/b**3))+c+(k/b - k/a)*c
except ZeroDivisionError:
    print("Невозможно получить решение из-за деления на 0")
    exit(0)
print("Ответ: " + str(abs(y)))