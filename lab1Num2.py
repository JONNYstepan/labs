from random import randint
a = int(input("Введите начальное число диапазона: "))
b = int(input("Введите конечное число дипазона: "))
c = randint(a,b)
n = 1
g = int(input("Попробуйте угадать число: "))
while g != c:
	if g == c:
		break
	if (g < a) or (g > b):
		print('Неверно, данное число не находится в заданном диапазоне')
	else:
		print('Неверно')
	g = int(input("Попробуйте угадать число: "))
	n += 1
print('\n' + 'Ура! Вы угадали!')
print("Число попыток: " + str(n))
