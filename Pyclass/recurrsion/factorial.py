def factorial(n):
	if n==1:
		return 1
	else:
		return n* factorial(n-1)

number = int(input('Please enter the number that you need to get the factorial: '))
print(factorial(number))

