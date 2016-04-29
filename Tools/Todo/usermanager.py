class User(object):

	def __init__(self):
		self.usr={}

	def add_user(self):
		while True:
			name= input("Please enter your username: ")
			if name in self.usr:
				print("We have already has this username ~")
				continue
			else:
				passwd=input("Please enter Your Password: ")
				self.usr[name]=passwd
				print("Congrats!Your account has been successfully established!")
				break
	def user_login(self,name_input):
		while True:
			counter = 0
			
			if name_input in self.usr:
				while True:
					attempt=0
					passwd_input=input("Please Enter your password: ")
					if passwd_input==self.usr[name_input]:
						return True
					else:
						print("Invaild Password, try again please!")
						attempt+=1
					if attempt>3:
						print("You have run out of your choice!Break Anyway")
						break
				break
			else:
				print("User not exists, try again please!")
			counter+=1
			if counter >3:
				print("You have run out of your choice!Break Anyway")
				break
			return False

	def delete_user(self):
		print("For your account protection, we need to verify your information")
		while True:
			counter = 0
			name_attempt=input("Please Enter your username: ")
			if name_attempt in self.usr:
				while True:
					attempt=0
					passwd_attempt=input("Please Enter your password: ")
					if passwd_attempt==self.usr[attempt_name]:
						del self.usr[name_attempt]
						del name_attempt
						del passwd_attempt
						print("You account has been successfully canceled, welcome back any time!")
						break
					else:
						print("Invaild Password, try again please!")
						attempt+=1
						if attempt>3:
							print("You have run out of your choice!Break Anyway")
							break
						continue
					break
			else:	
				print("User not exists, try again please!")
				counter+=1
				if counter >3:
					print("You have run out of your choice!Break Anyway")
					break

	def modify_user(self):
		print("For your account protection, we need to verify your information")
		while True:
			name_attempt=input("Please Enter your username: ")
			if name_attempt in self.usr:
				while True:
					attempt=0
					passwd_attempt=("Please Enter your password: ")
					if passwd_attempt==self.usr[attempt_name]:
						passwd=("Please enter your new password: ")
						self.usr[name_attempt]=passwd
						del passwd_attempt
						print("You account has been successfully canceled, welcome back any time!")
						break
					else:
						print("Invaild Password, try again please!")
						attempt+=1
						if attempt>3:
							print("You have run out of your choice!Break Anyway")
							break
				break
			else:
				print("User not exists, try again please!")
				counter+=1
				if counter >3:
					print("You have run out of your choice!Break Anyway")
				break

