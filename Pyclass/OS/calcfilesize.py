#calc the file size under current directory
import os
all_files=os.listdir(os.curdir) # move all the files in the all_files[]
file_dict={}

for each_file in all_files:
	if os.path.isfile(each_file): # check if it is file
		file_size=os.path.getsize(each_file)
		file_dict[each_file]=file_size

for each in file_dict.items():
	print('%s[%dbytes]' %(each[0],each[1]))
