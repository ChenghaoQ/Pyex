contain=input("Please enter the text")
length=len(contain)
def checkcheck(x):
	global length
	posi=length
	for each in range(length//2):
		if x[each]==x[posi]:
			each+=1
			length-=1
			continue
		else:
			print("Sorry, it is not")
			break

＃Answer
def palidrome(string):
	length=len(string):
	last = lenth-1
	flag=1
	lenth //=2
	for each in range(length):
		if string[each] !=string[last]:
			flag=0
		last -=1
	if flag==1:
		return True
	else:
		return False
def palidromeeasy(string):
	list1=list(string)
	list2=list1.sort()
	if list1==list2:
		return True
	else:
		return False

string = input('Please input a string:')
if palidrome(string)==1:
	print('Yes, it is a palindrome')
else:
	print('aOh')
