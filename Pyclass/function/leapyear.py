def main():
	year=int(input("请输入一个年份："))
	while not year.isdigit():
		year=int(input("Sorry, number only:")
	if year%4==0 and year % 100 != 0:
		print("%d 年是闰年～"%year)
	elif year %400 ==0:
		print("%d 年是闰年～"%year)
	else:
		print("%d 年是平年～"%year)


main()
