def countfiles():
	import os

	folder = input("Введите путь к папке:")
	files = next(os.walk(folder))[2]
	print(len(files))

def products():
	global new_list
	new_list = [] 
	n = 1
	with open('C:\\Py\\products.txt', 'r') as f:
		data_list = [line.strip().split(';') for line in f]
	for i in data_list:
		if int(i[2]) > 1700:
			new_list.append(i)
	for a in new_list:
		del a[0]
	new_list.sort()
	print("№,Наименование товара,Цена,Количество")
	for x in new_list:
		x.insert(0,str(n))
		print(x)
		n += 1

def reduce_cost():
	products()
	number_list = []
	number = input("Укажите номера товаров, у которых нужно уменьшить цену через пробел : ")
	cost = int(input("На сколько уменьшить цены? : "))
	number_list = number.split()
	for x in new_list:
		if x[0] in number_list:
			x[2] = int(x[2]) - cost
		print(x)

def save_changes():
	reduce_cost()
	file = open(input("Введите путь к файлу, в который сохранить данные: "), 'w')
	for x in new_list:
		file.write(str(x[0]) + ';' + x[1] + ';' + str(x[2]) + ';' + str(x[3]) + '\n')
	file.close()

while True:
	x = int(input("Введите число, соответствующее нужной вам функции :"))
	if x == 0:
		break
	elif x == 1:
		countfiles()
	elif x == 2:
		products()
	elif x == 3:
		reduce_cost()
	elif x == 4:
		save_changes()
	else:
		print('Некорректный ввод')

	y = input('Вы хотите продолжить? :')
	if y == '0' or y == 'no' or y == 'N' or y == 'нет':
		break
	if y == '1' or y == 'yes' or y =='Y' or y == 'да':
		continue
	else:
		print('Некорретный ввод')
		break