def file_write(file_name):
	f= open(file_name,'w')
	print('Please edit the text,\':w\'for save and exit')

	while True:
		write_some=input()
		if write_some!=':w':
			f.write('%s\n'%write_some)
		else:
			break
	f.close()
def main():
	file_name= input("Please Enter the file name(you can write the directory before file, default is current dir): ")
	file_write(file_name)

main()
