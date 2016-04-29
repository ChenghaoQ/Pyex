#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import useraction
import checklist
import datatrans
import draw
import os
import operation
import movement
import helpdoc


def your_todolist(username):

	today=checklist.TODO('* * * *Today * * * *')
	
	future=checklist.TODO('* * * * Future * * * *')
	
	switcher=0
	#current=today

	def init():

		try:
			#today.tmp='[   ]'
			future.reset('Reset')
			today.reset('Reset')
			#today.todolist=datatrans.loadfile()
			today.todolist[0][2]='[ * ]'
			future.todolist[0][2]='[ * ]'
		except FileNotFoundError:
			today.reset('Reset')
#                future.reset('Reset')
		#opera=operation.Operation(current.todolist,current.cursor,current.status,current.init,current.counter)
		#return opera
	def GoToDo():
		
		nonlocal switcher
		while True:
			#Draw the list
			os.system('clear')
			a=draw.Draw(today.todolist,today.name)
			b=draw.Draw(future.todolist,future.name)
			a.draw_TODO()
			b.draw_TODO()
			
			print("-----%d------"%switcher)
			print("-"*40)
			action = useraction.get_user_action()
			
			
			if action == 'Switch':
				switcher+=1
				continue
			if switcher%2==0:
				future.todolist[future.cursor[0]][2]='[   ]'
				current=today
			elif switcher%2==1:
				today.todolist[today.cursor[0]][2]='[   ]'
				current=future
			
			if action in useraction.moves:
				while True:
					try:
						movement.moves(action,current.todolist,current.cursor,current.tmp,current.i)
						break
					except IndexError:
						action=useraction.get_user_action()
						continue
			else:
				op=operation.Operation(current.todolist,current.cursor,current.status,current.init,current.counter)
				if op.execution(action,username)==0:
					return False
	os.system('clear')
	helpdoc.import_info()
	init()

	GoToDo()
	

