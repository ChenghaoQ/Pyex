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

	post=checklist.TODO('* * * * Gone * * * *')
	
	comp=checklist.TODO('* * * * Complete * * * *')
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
			future.reset('Reset')

	def GoToDo():
		
		nonlocal switcher
		while True:
			#Draw the list
			os.system('clear')
			a=draw.Draw(today.todolist,today.name)
			b=draw.Draw(future.todolist,future.name)
			c=draw.Draw(post.todolist,post.name)
			d=draw.Draw(comp.todolist,comp.name)
			a.draw_TODO()
			b.draw_TODO()
			c.draw_TODO()
			d.draw_TODO()
			print("-"*40)
			#Here is a problem
			if switcher%4==0:
				future.todolist[future.cursor[0]][2]='[   ]'
				current=today
				print("Your Current position: Today")
			elif switcher%4==1:
				today.todolist[today.cursor[0]][2]='[   ]'
				current=future
				print("Your Current position: Future")
			elif switcher%4==2:
				#post.todolist[post.cursor[0]][2]='[   ]'
				current=post
				print("Your Current position: Gone")
			elif switcher%4==3:
				#comp.todolist[post.cursor[0]][2]='[   ]'
				current=comp
				print("Your Current position: Complete")

			action = useraction.get_user_action()
			
			
			if action == 'Switch':
				switcher+=1
				continue
			if action in useraction.moves:
				while True:
					try:
						movement.moves(action,current.todolist,current.cursor,current.tmp,current.i)
						break
					except IndexError:
						action=useraction.get_user_action()
						continue
			else:
				op=operation.Operation(current.todolist,current.cursor,current.status,current.init,current.counter,post.todolist,comp.todolist)
				if op.execution(action,username)==0:
					return False
	os.system('clear')
	helpdoc.import_info()
	init()

	GoToDo()
	

