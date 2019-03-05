stroka = input("Введите строку, состоящую из слов, пробелов и знаков препинания: ")
newstroka =[]
strokalist = stroka.split()
for element in strokalist:
	if element[-2:] == 'ов':
		newstroka.append(element)
newstroka1 = ' '.join(newstroka)
print(newstroka1)