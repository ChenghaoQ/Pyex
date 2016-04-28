#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import useraction

class TODO(object):
	
	def __init__(self,name):
		self.todolist=[]
		self.status=['☐','☑','☒']
		self.counter=[0]
		self.init=5
		self.cursor=[0]
		self.i=[0]
		self.tmp=["[   ]"]
		self.blank='_'*30
		self.name=name
	def reset(self,passwd):
		if passwd== 'Reset':
			del self.todolist[:]
			for n in range(5):
				self.todolist.append([self.status[0],self.blank,'[   ]'])
			self.tmp='[   ]'
			self.new=0

