def main():
	file1=input("Please enter the name of file1:")
	count1=int(input("from which line to begin:"))
	end1=int(input("to which line want to check:"))
	file2=input("Please enter the name of file2:")
	count2=int(input("from which line to begin:"))
	
	differ = check_line(file1,file2,count1,count2,end1)
	
	if len(differ) == 0:
		print("***************S A M E ***************")
	else:
		print("There are %d differences"%len(differ))
		for each in differ:
			print('the %d%d line is different'%each)



def check_line(file1,file2,count1,count2,end1):
	f1=open(file1)
	f2=open(file2)
	differ = []

	for line1 in f1:
		line2=f2.readline()
		if line1=='':
			f1.readline()
		elif line2=='':
			f2.readline()
		count1+=1
		count2+=1
		if line1 != line2:
			differ.append((count1,count2))
		if count1==end1:
			break
	f1.close()
	f2.close()
	return differ
main()
