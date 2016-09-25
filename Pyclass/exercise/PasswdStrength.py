#This one is to check the password strength
#list the symbol first
symbols = r'''`!@#$%^&*()_+-=/?><{}[]\|;:,.'''
chars = 'qwertyuiopasdfghjklzxcvbnm'
nums='0123456789'
passwd=input("please input your password: ")

length=len(passwd)
while(passwd.isspace() or length==0):
	passwd=input("Error, None or include space,please enter again:")

if length<=8:
	flag_len=1
elif 8<length<16:
	flag_len=2
else:
	flag_len=3
#flag =1 if length<=8 else (flag_len=2 if 8<length<16 else 3)

for each in passwd:
	if each in symbols:
		flag_con +=1
		
for each in passwd:
	if each in chars:
		flag_con+=1
		break
for each in passwd:
	if each in nums:
		flag_con+=1
		break
while True:
	if flag_len==1 or flag_con==1:
		print("Low")
	elif flag_len==2 or flag_con ==2:
		print("Medium")
	else:
		print("High,good habit!")
		break
	print("There is three way to keep good passwd \n\
		1 \n\
		2 \n\
		3 \n\' ")
	break
		

		
	
