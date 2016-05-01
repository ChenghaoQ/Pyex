#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getch
#import user
actions=['Up','Down','New','Complete','Postpone','Remove','Help','Other','Switch']
letter_code="WSNCPRHOVwsncprhov"
action_dict=dict(zip(letter_code,actions*2))
moves=set(['Up','Down'])
def main_select(select):
	main_selection={'1':user.add_user(),
			'2':user.user_login()}#,
			#'3':pass,
			#'4':pass,}
	return main_selection[select]()
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


