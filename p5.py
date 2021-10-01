a = int(input ("Введите 5 значное число: "))
if  (a>9999) and (a<100000):
	if(a // 10000 == a % 10)and((a // 1000) % 10 == (a % 100) // 10):
		print ("Yes")
	else:
		print ("No")
else:
	print ("Invalid data")