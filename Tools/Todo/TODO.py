import menu
def main():
        while True:
                menu.main_menu()
                select=int(input())
                if select not in range(1,6):
                #   useraction.main_select(select)#         
                #Here to make selection
		if select == 1:
			user.add_user()


		elif select == 2:

			if user.userlogin():
				while True:
					menu.after_login()
					option=int(input())
					if option == 1:
						pass
					elif option == 2:
						pass
					elif option == 3:
						user.delete_user()
					elif option == 4:
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

	

 

