import menu
import helpdoc
import yourtodo
import usermanager

def main():
	user=usermanager.User()
	while True:
		menu.main_menu()
		select=int(input())
		if select == 1:
			user.add_user()


		elif select == 2:
			while True:
				name_input=input("Please Enter your username: ")

				if user.user_login(name_input):
					while True:
						menu.after_login(name_input)
						option=int(input())
						if option == 1:
							yourtodo.your_todolist(name_input)
						elif option == 2:
							pass
						elif option == 3:
							user.delete_user()
						elif option == 4:
							break	
				else:
					continue
				break


		elif select == 3:
			print(' **** Chenghao Qian is a lazy guy ****')
			input("Press Enter to continue...")
			continue
		elif select == 4:
			print(helpdoc.help)			
			input("Press Enter to continue...")

		elif select == 5:
			break
		else:
			print("Invalid selection, try again please")
			continue





if __name__ == '__main__':
	main()





