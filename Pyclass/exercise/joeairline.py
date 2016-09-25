import random
ROW = 6
COL = 4
MAX = 25
costMatrix=[(300,200,200,300),
	    (300,200,200,300),
   	    (300,200,200,300),
 	    (300,200,200,300),
	    (300,200,200,300),
	    (300,200,200,300)]
def main():
	flight_1=[];flight_2=[];flight_3=[];name=[];flight_number=[]
	#Bug fixed, forget to add flight_x on line 14,15,16
	flight_1=initialSeats(flight_1,random.randint(0,30))
	flight_2=initialSeats(flight_2,random.randint(0,30))
	flight_3=initialSeats(flight_3,random.randint(0,30))
	adminPawprint="cqnp3";adminpassword="pythongogo"

	while True:
		while True:
			displayMenu()
			option=int(input("Choose an option:"))
			if option in (1,2,3):
				break
			elif option != 1 or option != 2 or  option !=3:
				print("\nWrong option! Choose a right option again\n")
				continue
		if option is 1:
			while True:
				input_pawprint=input("Admin Pawprint: ")
				input_password=input("Admin password: ")
				
				if loginMatch(adminPawprint,input_pawprint) is True  or loginMatch(adminpassword,input_password) is True:
					break
				else:
					print("\nInvalid Pawpint and Password combination\n")
					continue
				print("Your total revenue is $%d"%getTotalRevenue(flight_1,flight_2,flight_3))
				 
				print("\nPrinting the Flight Map of flight Columbia to Miami...\n")
				printFlightMap(flight_1)
				print("\n\nPrinting the Flight Map of flight Columbia to Nashville...\n")
				printFlightMap(flight_2)
				print("\nPrinting the Flight Map of flight Columbia to Las Vegas...\n")
				printFlightMap(flight_3)
				print("\nThe total earning from all the flights:$ %d \n\n "%getTotalRevenue(flight_1,flight_2,flight_3))		
		elif option is 2:
			while True:
				flightMenus()
				flight_choice=int(input("\nChoose a flight: "))
				if flight_choice in range(1,4):
					break
			name=input("Enter your first name: ")
			if flight_choice is 1:
				flight_number="MIA1050"
				seatReservation(flight_1)
			elif flight_choice is 2:
				flight_number="BNA1050"
				seatReservation(flight_2)
			else:
				flight_number="LAS1050"
				seatReservation(flight_3)
			
			print("\n\nCongrats! %s, your flight %s is booked, Your e-ticket number is %s: \n"%(name,flight_number,
					''.join(printMessage(name,flight_number))))	
		
		else:
			print("\nTerminating the program ...\nThank you for using Joe's Airline Booking System.\n") 
			break

		

def initialSeats(flight,count):
	flight=[['O' for col in range(COL)] for row in range(ROW)]
	i=0
	while i < count:
		row=random.randint(0,ROW-1)
		col=random.randint(0,COL-1)
		if flight[row][col] == 'O':
			flight[row][col]='X'
			i+=1
	return flight #Bug here, forget to add return flight, cause NoneType error
def displayMenu():
	print("\n********** WELCOME TO JOE'S AIRLINE BOOKING SYSTEM **********\n")
	print("\n 1.) Admin Log-in\n 2.)Reserve a seat\n 3.) Exit\n")

def printFlightMap(flight):
	i = 0
	while i<ROW:
		print(flight[i])
		i+=1
def loginMatch(string1,string2):
	return string1 == string2

def getTotalRevenue(f1,f2,f3):
	total=0;i=0;j=0
	for i in range(ROW):
		for j in range(COL):
			if f1[i][j] == 'X':
				total += costMatrix[i][j]
	for i in range(ROW):
		for j in range(COL):
			if f2[i][j] == 'X':
				total += costMatrix[i][j]
	for i in range(ROW):
		for j in range(COL):
			if f3[i][j] == 'X':
				total += costMatrix[i][j]
	return total 
def flightMenus():
	print("\n 1.)COU ---> MIA\n 2.) COU ----> BNA \n 3.) COU ----> LAS\n")

def seatReservation(flight):
	printFlightMap(flight)
	while True:
		row=int(input("\nEnter the row number:"))
		while row<0 or row > 5:
			print("\nSeat Rows are between 0 and 5")
			row = int(input("Try again. Which seat row do you want?:"))
		col= int(input("\nEnter the column number:"))
		while col<0 or col > 5:
			print("\nSeat Columns are between 0 and 5")
			col = int(input("Try again. Which seat column do you want?:"))
		if flight[row][col] is 'X':
			print("Sorry!! Someone has reserved that seat. Please Try Again.")
		elif flight[row][col] is 'O':
			flight[row][col] = 'X'
			break
	printFlightMap(flight)
	print("\nYour requested seat has been reserved")

def printMessage(string1,string2):
	string3=[]
	i=0
	length=int(len(string1+string2)/2)
	for i in range(length):
		string3.append(string1[i])
		string3.append(string2[i])
	return string3

main()
