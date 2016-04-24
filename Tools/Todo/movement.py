class Move(object):
        def __init__(self,todolist,cursor):
                self.tmp='[   ]'
                self.cursor=cursor
                self.todolist=todolist
                self.i=0
        def move_cursor(direction):
                if direction == 'Up':
                        self.cursor -= 1
                elif direction== 'Down':
                        self.cursor += 1
        def put_cursor(cursor):
                self.todolist[cursor][2]='[ * ]'
        def restore_cursor(cursor,tmp):
                self.todolist[cursor][2]=tmp



def movement(action):
        pass
