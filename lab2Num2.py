my_string = "Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
print("     ФИО                               " + "О студенте "  )
data_list = [a.split(';') for i,a in enumerate(my_string.split('_'))]
for a in data_list:
	print(a[0], a[1], a[2] + '           ' , a[4] + ',', a[3])