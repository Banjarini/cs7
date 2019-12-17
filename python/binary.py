def from_binary(x):
	""""
	>>> from_binary("00110011")
	51
	>>> from_binary("01111111")
	127
	>>> from_binary("10011001")
	153
	"""
	x = str(x)
	assert len(x) == 8, "binary has 8 bits !!!"
	total = 0
	x = reverse(x)
	for i in range(0,len(x)):
		if x[i] == "1":
			total += 2**i
			
	return total

def to_binary(x):
	rv = ""
	for i in range(0,8):
		rv = rv + str(x % 2)
		x = x // 2
	return reverse(rv)

def reverse(x):
	rv = ""
	for i in range(1,len(x)+1):
		rv = rv + x[-i]
		
	return rv 
