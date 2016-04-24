#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import useraction

class TODO(object):
	
	def __init__(self,name):
		self.todolist=[]
		self.status=['☐','☑','☒']
		self.counter=0
		self.init=5
		self.cursor=0
		self.i=0
		self.tmp='[   ]'
		self.blank='________________________'
		self.name=name
	def move(self,direction):
		def init_cursor(cursor,tmp):
			tmp=self.todolist[cursor][2]
			return cursor,tmp
		def move_cursor(direction):
			if direction == 'Up':
				self.cursor -= 1
			elif direction== 'Down':
				self.cursor += 1
		def put_cursor(cursor):
			self.todolist[cursor][2]='[ * ]'
		def restore_cursor(cursor,tmp):
			self.todolist[cursor][2]=tmp
		
		move_cursor(direction)
		restore_cursor(self.i,self.tmp)
		self.i,self.tmp=init_cursor(self.cursor,self.tmp)
		put_cursor(self.cursor)
	def operation(self,action):
		def new_todo():
			task=useraction.get_user_input()
			if task =='Reset':
				return 'Init'

			if self.counter<5:
				self.todolist[self.counter]=[self.status[0],task,'[   ]']
			else:
				self.todolist.append([self.status[0],self.task_jar[self.counter],'[   ]'])
			self.counter+=1
		def complete_todo():
			self.todolist[self.cursor][0]=self.status[1]
		def postpone_todo():
			self.todolist[self.cursor][0]=self.status[2]
		def remove_task():
			del self.todolist[self.cursor]
			self.counter-=1
			self.init-=1
			if self.init<5:
				self.todolist.append([self.status[0],self.blank,'[   ]'])
				self.init+=1
				
		def execution(action):
			if action ==  'New':
				new_todo()
			elif action == 'Complete':
				complete_todo()
			elif action == 'Postpone':
				postpone_todo()
			elif action == 'Remove':
				remove_task()
			elif action == 'Help' :
				pass
		#execution(action)
	def draw(self):
		def draw_title():
			print("* * * * Welcome to Chenghao's todo list * * * * *")
		def draw_list():
			for each in self.todolist:
				print('  '.join(each))
		os.system('clear')
		draw_title()
		draw_list()
	def reset(self,passwd):
		if passwd== 'Reset':
			del self.todolist[:]
			for n in range(5):
				self.todolist.append([self.status[0],self.blank,'[   ]'])
			self.tmp='[   ]'
			self.new=0
