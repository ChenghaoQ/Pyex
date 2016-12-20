import os
number = 0
def search(path,keyword):
        global number
        content= os.listdir(path)
        for each in content:
                each_path = path+os.sep+each
                number +=1
                if os.path.isdir(each_path):
                        search(each_path,keyword)
search(os.getcwd(),input('Your Keyword:'))
print(number) 
