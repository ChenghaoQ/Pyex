def main():
	print("* * * Tips: The file name can be with the directory path ~* * *")
	file1=input("Please enter name of the file1:")
	file2=input("Please enter name of the file2:")
	differ =file_compare(file1,file2)
	if len(differ)==0:
		print(" They are the same:)")
	else:
		print("There are %d differences:"%len(differ))
		for each in differ:
			print("The %d line is different"%each)






def file_compare(file1,file2):
	f1=open(file1)				
	f2=open(file2)		#No args('r','w',etc) because the default is 'rt'-->readtext
	count=0    #Stats the lines 
	differ=[]  # set a list of difference

	for line1 in f1:    #get each line from f1
		line2 =f2.readline()  # get each line from f2
		count+=1		#count the line we have already go through
		if line1 != line2:      # check if they are the same 
		differ.append(count)    # 
	f1.close()
	f2.close()	#close the file
	return differ
main()
