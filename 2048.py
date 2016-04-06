import curses
from random import randrange,choice     #randrange is randint + randchoice
from collections import defaultdict #still not sure what does defaultdict

actions=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq']   
action_dict=dict(zip(letter_code,actions*2) 
#Main function
def main(stdscr):   #stdscr is in curses library










def get_user_action(keyboard): #Where does keyboard comes from, input?
	char="N"
	while char not in action_dict:  #while user input doesn't match action_dict
		char=keyboard.getch()#?????getch???
		return actions_dict[char]
#转置
def transpose(field):
	return [list(row) for row in zip(*field)]#matrix turn 90 clockwise, reason is using zip to get first letter of each row(first column) to make a new first row, ohters are the same
#Inverse
def invert(field):
	return [row[::-1] for row in field] #matix get inverted, [::-1] is for invert a string

class GameField(object):
	def __inti__(self,height=4,width-4,win=2048) #init the args to the self
		self.height=height        #Height =4
		self.width=width 	  #Width=4
		self.win_value=2048	  #2048 to win
		self.score=0		  #init score=0
		self.highscore		  #The history highest
		self.reset()		  #reset gamefield(all settings),call a function defined later
	def spawn(self):   #spawn mean produce a random 2 or 4
		new_element =4 if randrange(100)>89 else 2 #initial the probability of 2 or 4
		(i,j)=choice([0 for i in range(self.width)] for j in range(self.height))#i,j emulate a matrix of the game field and use the random choice to fill one space,not filling the space ,just get the coordinate
		self.field[i][j] = new_element #fill the coordinate
	
	def move(self,direction): #other than the self element, move also need directions inputed by users
		def move_row_left(row): #(Use left would be easier!)We can just make one sitution to process, and using matrix turn to finish other steps, it is same as copy 3 times,!!!We need to know the numbers elements in a row, 4 is default!!!!!
			def tighten(row): #move all the number to left if has space, not merge,take the row as arguments
				new_row=[i for i in row if i!=0] #(put all the number != 0 to the beginning of a new row)== move them to the left
				new_row += [0 for i in range(len(row) -len(new_row))]#filling the space left with 0
				return new_row #looks like using new row to take place of original one
			def merge(row):#We use tighten first, so assume the new row is in matrix
				pair=False #set pair is False as default,
				new_row= [] # This is a new row for merge
				for i in range(len(row)):#len(row) should be 4, so it is an iteration of i= [0,1,2,3]
					if pair: #if pair is Ture 
						new_row.append(2*row[i]) #put the first merged number to the beginning of the list,value is 2 times
						self.score += 2*row[i]# increase the score by merged value
						pair = False # Because of False, the number can no longer be paired, need to check again
					else:
						if i +1 < len(row) and row[i] == row[i+1]:# (1)row[i+1] should be in the row (2)row[i]==row[i+1] indicate they can merge
							pair=True
							new_row.append(0) #e.g.[2,2,0,0]=>[4,0,0,0], a 0 should be append???????how do they solve [4,4,2,2]?
						else:
							new_row.append(0)
						else:
							new_row.append(0) #???????
				assert len(new_row) == len(row)# ???????????
				return new_row
			#So here, we need to tighten them first and merge them then tighten again
			return tighten(merge(tighten(row)))

			moves={} #Build a dictionary {action:operation}
			moves['Left']= lambda field:[move_row_left(row) for row in field]
			moves['Right']= lambda field: invert(moves['Left'](invert(field)))		
			moves['Up'] = lambda field : transpose(move['Left'](invert(field)))
			moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))
			#Why using lambda here???
			if direction in moves:
				if self.move_is_possible(direction): #What is this?????
					self.field=move[direction](self.field)#why there is a () ,need a test here
					self.spawn()# after move, there should be a new one comes 
					return True #move is True, so you still can move
				else:
					return False #You cannot move, what will hapen?~~
			
		






	def reset(self):  #this function mention in __init__ for reset the game,not restart
		if self.socre > self.highscore:  #assert if the current score higher than record
			self.highscore=self.socre  #reset the highscore 
		self.score=0 #reset status
		self.field=[[0 for i in range(self.width)] for j in range(self.height)] #reset the game field to clear
		self.spawn()
		self.spawn()  #line 50,51 is for put serveral number on gamefield to initialize the game
	
			
		
	


