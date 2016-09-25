def dec2bin(dec):
	result=''
	if dec:
		result = dec2bin(dec//2)
		return result + str(dec%2)
	else:
		return result
print(dec2bin(62))
