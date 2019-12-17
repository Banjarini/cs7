default = "9999"
master = "0000"
class account:
	""""
	>>> jonathan = account()
	>>> jordan = account()
	>>> jordan.password("1234")
	correct
	>>> jordan.password("1111")
	Incorrect pasword you have 2 tries left
	>>> jordan.password("1111")
	Incorrect pasword you have 1 tries left
	>>> jordan.password("1111")
	Incorrect password your account has been blocked
	>>> jordan.password("1111")
	Your account has been blocked contact your service provider
	>>> jordan.password(master)
	Your password has been reset to 9999
	>>> jordan.key
	'9999'
	>>> jordan.changePassword("9999", "9876")
	Your password has been changed to 9876
	>>> jordan.balance
	0
	>>> jordan.deposit(100)
	>>> jordan.withdraw(10,"9876")
	Your new balance is $90
	>>> jordan.balance
	90
	>>> jordan.transfer(50, "9876", jonathan)
	Your new balance is $40
	>>> jonathan.balance
	50
	"""
	min_length = 8
	def __init__(self, password="1234", balance=0):
		self.key = password
		self.balance = balance
		self.master = master
		self.numberTrys = 3
		print("Thank You for creating an account youn default password is " + str(default))

	def password(self, password):

		if password == self.master:
			self.numberTrys == 3
			self.key = default
			print("Your password has been reset to " + str(self.key))

		elif self.numberTrys == 0:
			print("Your account has been blocked contact your service provider")

		#check if the password is correct
		elif password == self.key:
			self.numberTrys = 3
			return true

		#if the password is wrong print out a message
		else:
			self.numberTrys -= 1
			if self.numberTrys == 0:
				print("Incorrect password your account has been blocked")
			else:
				print("Incorrect pasword you have " + str(self.numberTrys) + " tries left")

	def changePassword(self, password, newPassword):
		if self.key == password:
			if not isinstance(newPassword, str):
				raise TypeError("password must be a string")
			if len(newPassword) < self.min_length:
				raise ValueError("password must be at least %d character long"  % (self.min_length))
			self.key = newPassword
		else:
			raise ValueError("Incorrect password")

	def withdraw(self, amount, password):
		if password == self.key:
			if self.balance > amount:
				self.balance -= amount
				print("Your new balance is $" + str(self.balance))
			else:
				print("Insuficient funds")

	def deposit(self, amount):
		self.balance += amount
		#print("Your account balance is $" + str(self.balance))

	def transfer(self, amount, password, accountNo):
		self.withdraw(amount, password)
		accountNo.deposit(amount)
		# print(str(account)+ "'s balance is" + str(account.balance))
		# print("Your account balance is $" + str(self.balance))
while True:
	print("what would you like to do?")
	print("C = Create account")
	print("D = Deposit money")
	print("W = Withdraw money")
	print("T = Transfer money")
	print("P = Change Password")
	response = input().casefold() 
	if response == "c":
		print("what account name do you want")
		name = input()
		name = account()
	elif response == "d":
		print("what account do you want to deposit to")
		accname = input()
		print("How much are you depositing?")
		amount = input()
		accname.deposit(amount)

	elif response == "w":
		print("what account do you want to withdraw from")
		accname = input()
		print("How much are you withdrawing?")
		amount = input()
		 
	elif response == "t":
		print("account name?")
		accname = input()
		print("password")
		password = input()
		print("who do you want to transfer to?")
		accountNo = input()
		print("How much")
		amount = input()
		accname.transfer(amount,password,accountNo)
	else:
		print("error")