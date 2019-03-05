data = input('Вводите каждый новый элемент через пробел: ')
list1 = data.split()
if len(list1) <= 10:
	while len(list1) <= 10:
		print('Введено менее 10 - ти элементов, введите ещё: ')
		i = input()
		list1 += i.split()		
print(" В исходном списке " + str(len(list1)) + " элементов")
list1 += ['1', '17', '66', '228', '99']
list2 = [el for el in list1 if int(el) % 2] 
print(list2)