#Get the narcissistic number between 100-999: 153=1^3+5^3+3^3
i=100
N=[]
while i <=999:
	first=i//100
	third=i%10
	second=(i//10)%10
	nar=first**3+second**3+third**3
	if i==nar:
		print(i)
		i+=1
	else:
		i+=1
#Anwser Key
for i in range(100,1000):
	sum=0
	temp=i
	while temp:
		sum=sum+(temp%10)**3
		temp//=10
	if sum =i
		print(i)
