import os
#check the filetype under current location
all_files = os.listdir(os.curdir)# us os.curdir to represent the current dir
type_dict={}

for each_file in all_files:
	if os.path.isdir(each_file):
		type_dict.setdefault('Folder',0)
		type_dict['Folder']+=1
	else:
		ext =os.path.splitext(each_file)[1]
		type_dict.setdefualt(ext,0)
		type_dict[ext]+=1

for each_type in type_dict.keys():
	print('There are %d  type of %s files in current dir'%(type_dict[each_type],each_type)) 
