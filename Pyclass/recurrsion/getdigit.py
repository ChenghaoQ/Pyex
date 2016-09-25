result=[]
def get_digits(n):
	if n>0:
		result.insert(0,n%10)
		get_digits(n//10)

get_digits(12345)
print(result)
