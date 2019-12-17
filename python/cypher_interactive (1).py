from operator import add
def code():
	"""returns a scrambled message where each letter is moved by shift places"""
	print("Enter the message you want to code .")
	string = str(input())
	rv = ""
	print("How many letters do you want to shift by.")
	shift = input()
	for i in range(0,len(string)):
		rv += (chr(ord(string[i]) + shift))
	return rv
