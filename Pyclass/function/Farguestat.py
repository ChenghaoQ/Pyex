def count(*param):
	length=len(param)
	letters=0
	space=0
	digit=0
	others=0
	for each in param:
		if each.isalpha():
			letter+=1
		elif each.isdigit():
			digit+=1
		elif each ==' ':
			space+=1
		else:
			others+=1
	print('
