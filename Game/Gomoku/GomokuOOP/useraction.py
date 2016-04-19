#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getch
action=['Up','Left','Down','Right','Spawn','Restart','Exit']
letter_code='WASDGEQwasdgrq'
action_dict=dict(zip(letter_code,action*2))


def get_user_action():
	print("Move cursor please: ")
	#char = input("Move cursor please: ")
	char= getch.getch()
	while char not in action_dict:
		print("Wrong direction, again please: ")
		char=getch.getch()
	return action_dict[char]