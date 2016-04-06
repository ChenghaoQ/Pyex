import curses
form random import randrange,choice
from collections import defaultdict  #what is defaultdict
#主逻辑

#用户行为
	actions=['Up','Left','Down','Right','Restart','Exit']#define six user actions
	letter_codes=[ord(ch) for ch in 'WASDRQwasdrq'] #ord以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常
	action_dict=dict(zip(letter_code,action*2)) #将用户行为和键入的字母对应起来，大小写各对应一次，所以action *2
	
#状态机，处理游戏主逻辑常用技术，将游戏状态分块
def main(stdscr):
	def init():
	#重置游戏棋盘
	game_field.reset()
	return 'Game'
	
	def not_game(state):
	#画出 Gameover 或者 Win 的界面
	#读取用户输入得到的action,判断是重启游戏还是结束程序
	responses = defaultdict(lambda:state)#m默认是当前状态，没有行为就会在当前界面循环
	responses['Restart'],responses['Exit']='Init','Exit'#对应不同的行为到不同的状态
	return response[action]
	
	def game()；
	#画出当前棋盘状态
	#读取用户输入的得到action
	if action =='Restart':
		return 'Init'
	elif action== 'Exit':
		return 'Exit'
	#if 成功移动了一步
		if 游戏胜利了：
			return 'Win'
		if 游戏失败了：
			return 'Gameover'
		return 'Game'  #等价于重复调用自身，等于while true

	state_actions={
		'Init':init,
		'Win':lambda:not_game('Win')
		'Gameover':lambda:not_game('Gameover') #为什么这里要加lambda
		'Game':game
	}

	state='Init'

	#状态机循环
	while state != 'Exit'
		state = state_action[state]()


	
#用户输入处理
#阻塞+循环，直到获得用户有效输入才返回对应行文
def get_user_action(keyboard):
	char="N"
	while char not in actions_dict:
		char=keyboard.getch()
	return actions_dict[char]

#矩阵转置与矩阵逆转
#加入这两个操作可以大大减少代码量，感受一下
#矩阵转置
def transpose(field):
	return [list(row) for row in zip(*field)]

#矩阵逆转（不是逆矩阵）：
def invert(field):
        return [row[::1] for row in field]



#创建棋盘:



#初始化棋盘的参数，可以指定棋盘的高和宽以及游戏胜利条件，默认是最经典的 4x4～2048。
class GameField(object):
        
        def __init__(self,height=4,width=4,win=2048) #Actually the arg* has already had value for the self pointer
                self.height=height
                self.width=width
                self.win_value=2048 #过关分数
                self.score=0    #当前分数
                self.highscore=0 #最高分
                self.reset()  #棋盘重置

#棋盘操作
#随机生成一个 2 或者 4
        def spawn(self):
                new_element =4 if randrange(100)>89 else 2 # When random number is 100 get 4 else 2
                (i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] ==0])
                self.field[i][j] =new_element
#重置棋盘
        def reset(self):
                if self.socre > self.highscore:
                        self.highscore=self.score
                self.score=0
                self.field = [[0 for i in range(self.width)] for j in range(self.height)]
                self.spawn()
                self.spawn()


#一行向左合并
#(注：这一操作是在 move 内定义的，拆出来是为了方便阅读)
def move_row_left(row):
        def tighten(row): #把零散的非零单元挤到一块
                new_row=[i for i in row if i!=0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row
        
        def merge(row):
                pair =False
                new_row=[]
                for i in range(len(row)):
                        if pair:
                                new_row.append(2 * row[i])
                                self.score +=2 * row[i]
                                pair = False
                        else:
                                if i + 1 <len(row) and row[i] ==row[ i+1]:
                                        pair=True
                                        new_row.append(0)
                                else:
                                        new_row.append(0)
                assert len(new_row) == len(row)
                return new_row
                ##先挤到一块再合并再挤到一块
        return tighten(merge(tighten(row)))  #?????????????????
                                                                                                                                             
#棋盘走一步
#通过对矩阵进行转置与逆转，可以直接从左移得到其余三个方向的移动操作 !!!!!!!!!!!!!!!!!!!!
def move(self,diection):
        def move_row_left(row):
        #一行向左合并

        moves={}
        moves['Left']= lambda field:[move_row_left(row) for row in field]
        moves['Right']= lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field : transpose(move['Left'](invert(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
                if self.move_is_possible(direction):
                        self.field=moves[direction](self.field)
                        self.spawn()
                        return True
                else:
                        return False

#判断输赢
def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

#判断能否移动
def move_is_possible(self,direction):
        def row_is_left_moveable(row):
                def change(i);
                        if row[i] ==0 and row[i+1]!=0 #可以移动
                                return True
                        if row[i] !=0 and row[i+1][ == row[i]: # 可以合并
                                return True
                        return False          #Attention here, no using else:return false
                return any(chaage(i) for i in range(len(row) -1))

        check={}

        check['Left'] =lambda field:any(row_is_left_movable(row) for row in filed)
        check['Right']=lambda field: check['Left'](invert(field))
        check['Up'] =lambda field: check['Left'](transpose(field))
        check['Down'] =lambda field check['Right'](transpose(field))

        if direction in check




#绘制游戏界面（注：这一步是在棋盘类内定义的）
def draw(self,screen):
        help_string1='(W)Up (S)Down (A)Left (D)Right'
        help_string2='          (R)Restart (Q)Exit'
        gameover_string='               GAME OVER               '
        win_string='            You WIN!'
        def cast(string):
                screen.addstr(string + '\n')

        #绘制水平分割线
        def draw_hor_separator():
                line= '+' +('+------'*self.width+'+')[1:]# what does [1:] do
                separator = defaultdict(lambda:line) #what doss defaultdict do
                if not hasattr(draw_hor_separator,"counter") #where did hasattr come and why use if not
                        draw_hor_separator.counter =0
                cast(separator[draw_hor_separator.counter])
                draw_hor_separator.counter ==1
        def draw_row(row):
                cast(''.join('|{: ^5} '.format(num) if num > 0 else '|' for num in row) + '|')
	screen.clear()
	cast('SCORE: ' + str(self.score))
	if 0 != self.highscore:
		cast('HIGHSCORE: '+str(self.highscore))

	for row in self.field:
		draw_hor_separator()
		draw_row(row)
	draw_hor_separator()

	if self.is_win():
		cast(win_string)
	else:
		if self.is_gameover()；
			cast(gameover_string)
		else:
			cast(help_string1)
	cast(help_string2)

#完成主逻辑
#完成以上工作后，我们就可以补完主逻辑了！
def main(stdscr):
    def init():
        #重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): # move successful
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    curses.use_default_colors()
    game_field = GameField(win=32)  #Linux系统不能运行的原因之一


    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

#运行
#填上最后一行代码：
curses.wrapper(main)

#全部代码
#-*- coding:utf-8 -*-

import curses
from random import randrange, choice # generate and place new tile
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

def get_user_action(keyboard):    
    char = "N"
    while char not in actions_dict:    
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            def tighten(row): # squeese non-zero elements together
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:                              \
                transpose(moves['Left'](transpose(field)))
        moves['Down']  = lambda field:                              \
                transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def move_is_possible(self, direction):
        def row_is_left_movable(row): 
            def change(i): # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0: # Move
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # Merge
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

def main(stdscr):
    def init():
        #重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): # move successful
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    curses.use_default_colors()
    game_field = GameField(win=32)


    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)

#License

本作品在 GFDL1.2 协议下授权使用,ekCit作品




