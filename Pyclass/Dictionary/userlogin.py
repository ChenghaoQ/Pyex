
"""option=input('''* * * * * Main Menu * * * * *
	1. Create a new account
	2. User login
	3. Exit
	Please choose an option: ''')

	if option == 1:
		input("Please Enter the Username: ")
		
		input("Please Enter the password: ")
		print("New user created successfully!")
	
	elif option==2:
		input("Please Enter the Username: ")
		input("Please Enter the password: ")
		
		print("welcome to xxoo system!")
	else:
		break
"""
#using dictionary
user_data={}
def new_user():
	prompt="Please Enter the Username:"    #1\using a variable instead a string
	while True:
		name=input(prompt)             #1\Using a variable instead a string
		if name in user_data:
			prompt = 'Already Exist!'
			continue
		else:
			break
	passwd=input("Please Enter the password: ")#2\Unitl now , there are nothing added to the dict
	user_data[name]=passwd			   #2\Add User and passwd to dict		
	print("New user created successfully!")

def exist_user():
	prompt="Please Enter the Username:"
	while True:
		name = input(prompt)
		if name not in user_data:		#3\Check if username in dict
			prompt='User not exist'
			continue
		else:
			break
	passwd=input("Please Enter the password: ")
	if passwd== user_data.get(name):		#3\Check if passwd match username in dict
		print('Welcome!')
	else:
		print("username password doesn't match")

def showmenu():
	
	option='''* * * * * Main Menu * * * * *
	1. Create a new account(N/n)
	2. User login(E/e)
	3. Exit(Q/q)
	Please choose an option: '''
	while True:
		chosen=False  #\4set up a condition , I would like to use break on line 66 instead.
		while not chosen:	#4\ if user while True instead , line 66 should be break
			choice= input(option)
			if choice not in'NnEeQq':
				print('Invalid choice,try again please')
			else:
				chosen=True	#\4Related to line 60
		if choice == 'Q' or choice =='q':
			break
		elif choice == 'N' or choice =='n':
			new_user()
		elif choice == 'E' or choice =='e':
			exist_user()

showmenu()	
