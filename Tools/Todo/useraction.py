#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getch
actions=['Up','Down','Complete','New','Postpone','Remove','Exit']#'Save','Quit']
letter_code="WSKJLRQwskjlrq"
action_dict=dict(zip(letter_code,actions*2))
moves=set(['Up','Down'])

def get_user_input():
	task = input("What Are We Gonna TODO today? :")
	return task



def get_user_action():
	char='N'
	print("please enter an action: ")
	char=getch.getch()
	while char not in action_dict:
		print("please enter an action again: ")
		char=getch.getch()
	return action_dict[char]


