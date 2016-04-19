import curses
from random import randrange,choice     #randrange is randint + randchoice
from collections import defaultdict #still not sure what does defaultdict

actions=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq']   
action_dict=dict(zip(letter_code,actions*2)) 
#Main function
def main(stdscr):   #stdscr is in curses library
	def init(): # reset the game field and restart the game
		game_field.reset() # using game_field not GameField because there is a statement below
		return 'Game'	#can we use dictionary like this? why>
	
	def not_game(state): #Not game status is for gameover or win after game
		game_field.draw(stdscr)   #other than self, there is another variable in it
		action = get_user_action(stdscr)#where is this
		response = defaultdict(lambda:state) #default is current status, no action will keep the current status
		response['Restart'],response['Exit'] ='Init','Exit' # Restart need to  init again, exit just exit
		
		return response[action]#Return the users respones
	def game():
		game_field.draw(stdscr) # draw the current field status
		action=get_user_action(stdscr)#get useer action

		if action =='Restart':
			return 'Init'
		if action =='Exit':
			return 'Exit'
		if game_field.move(action): # move successful ( move not none)
			if game_field.is_win():
				return 'Win'
			if game_field.is_gameover():
				return 'Gameover'
		return 'Game'

	state_actions ={'Init':init,  #put state into a dictionary
			'Win':lambda:not_game('Win'),
			'Gameover':lambda:not_game('Gameover'),
			'Game':game
		}

	curses.use_default_colors()
	game_field=GameField(win=32) # how to change to Mac
	
	state='Init' # initialize the state

	# circulated the status machine
	while state !='Exit':
		state = state_actions[state]() # state_action[state] from dictionary actually is a function, so put the argument in the ()	








def get_user_action(keyboard): #Where does keyboard comes from, input?
	char="N"
	while char not in action_dict:  #while user input doesn't match action_dict
		char=keyboard.getch()#?????getch???
	return action_dict[char]
#转置
def transpose(field):
	return [list(row) for row in zip(*field)]#matrix turn 90 clockwise, reason is using zip to get first letter of each row(first column) to make a new first row, ohters are the same
#Inverse
def invert(field):
	return [row[::-1] for row in field] #matix get inverted, [::-1] is for invert a string

class GameField(object): #where did screen, direction comes from
	def __init__(self,height=4,width=4,win=2048): #init the args to the self, Recently error write init wrong will cause the class object take no(arg)
		self.height=height        #Height =4
		self.width=width 	  #Width=4
		self.win_value=2048	  #2048 to win
		self.score=0		  #init score=0
		self.highscore=0		  #The history highest
		self.reset()		  #reset gamefield(all settings),call a function defined later

	def draw(self,screen):
		help_string1= '(W)Up (S)Down (A)Left (D)Right '
		help_string2 = '     (R)Restart (Q)Exit'
		gameover_string='		GAME OVER'
		win_string='		You win'
		def cast(string):
			screen.addstr(string+'\n')

		def draw_hor_separator():#shows how to draw the hor_separator
			line='+' +('+------' * self.width + '+')[1:] #You cannot remove the first + in '+------" because you need it for the following lines, use [1:] to cut the first +
			separator =defaultdict(lambda:line) # what does defaultdict do
			if not hasattr(draw_hor_separator,"counter"): # what?
				draw_hor_separator.counter = 0
			cast(separator[draw_hor_separator.counter]) 
			draw_hor_separator.counter +=1

		def draw_row(row):# shows how to draw the row, calls later
			cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')# what ??

		screen.clear() # refresh the screen
		cast('SCORE: ' + str(self.score))  # display the score
		if 0 != self.highscore:
			cast('HIGHSCORE: ' + str(self.highscore))
		for row in self.field: # draw the field
			draw_hor_separator()
			draw_row(row)
		draw_hor_separator()# draw the last line
		if self.is_win():
			cast(win_string)
		else:
			if self.is_gameover():
				cast(gameover_string)
			else:
				cast(help_string1)
		cast(help_string2)

	def spawn(self):   #spawn mean produce a random 2 or 4
		new_element =4 if randrange(100)>89 else 2 #initial the probability of 2 or 4
		(i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] ==0])    #i,j emulate a matrix of the game field and use the random choice to fill one space,not filling the space ,just get the coordinate
		self.field[i][j] = new_element #fill the coordinate
	
	def move_is_possible(self,direction): # this part looks same to the move function
		def row_is_left_moveable(row): #check if numbers can move to the left
			def change(i):
				if row[i] ==0 and row[i+1]!=0:    #if the number on the left is None and has number on the right
					return True      #Movable
				if row[i] !=0 and row[i+1] == row[i]:      #if it has same number tightened
					return True	#Mergeable
				return False		#attention here, not using eles:return False(Set False as default)
			return any(change(i) for i in range(len(row)-1)) # if iterable has a True, return True ,All false, return false, this function check if there is at lease one situdation satisfied
		check={}#build a dict for the check of four direction
		check['Left'] =lambda field:any(row_is_left_moveable(row) for row in field)
		check['Right']=lambda field: check['Left'](invert(field))
		check['Up'] =lambda field: check['Left'](transpose(field))
		check['Down'] =lambda field:check['Right'](transpose(field))

		if direction in check: #if the direction has a match value in check
			return check[direction](self.field)  #why has ( )
		else:
			return False
	
	
	
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
							new_row.append(row[i])
				assert len(new_row) == len(row)# ???????????
				return new_row
			#So here, we need to tighten them first and merge them then tighten again
			return tighten(merge(tighten(row)))

		moves={} #Build a dictionary {action:operation}
		moves['Left']= lambda field:[move_row_left(row) for row in field]
		moves['Right']= lambda field: invert(moves['Left'](invert(field)))		
		moves['Up'] = lambda field : transpose(moves['Left'](transpose(field)))
		moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))
		#Why using lambda here???
		if direction in moves:
			if self.move_is_possible(direction): #check if move_if_possible with direction input is true
				self.field=moves[direction](self.field)#why there is a () ,need a test here
				self.spawn()# after move, there should be a new one comes 
				return True #move is True, so you still can move
			else:
				return False #You cannot move, what will hapen?~~
		
	def is_win(self):
			return any(any(i >= self.win_value for i in row) for row in self.field)# check any numbers in the field >= 2048

	def is_gameover(self):
			return not any(self.move_is_possible(move) for move in actions) #when is_win is false and cannot move, gameover



		
		






	def reset(self):  #this function mention in __init__ for reset the game,not restart
		if self.score > self.highscore:  #assert if the current score higher than record
			self.highscore=self.score  #reset the highscore 
		self.score=0 #reset status
		self.field=[[0 for i in range(self.width)] for j in range(self.height)] #reset the game field to clear
		self.spawn()
		self.spawn()  #line 50,51 is for put serveral number on gamefield to initialize the game
	
			
		
	


curses.wrapper(main) # Wrap as curses


#License

#本作品在 GFDL1.2 协议下授权使用,ekCit作品
