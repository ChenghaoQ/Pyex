f=open('/users/3/cqnp3/Github/FishQ/Files/AcctLiab.md')
#hard way
lines=list(f)
for each_line in lines:
	print(each_line)
#smarter way
for each_line in f:
	print(each_line)
