# Object Oriented Programming
name = 'Jordan'
surname = 'Sherfield'
class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    Fib object, value 0
    >>> start.next()
    Fib object, value 1
    >>> start.next().next()
    Fib object, value 1
    >>> start.next().next().next()
    Fib object, value 2
    >>> start.next().next().next().next()
    Fib object, value 3
    >>> start.next().next().next().next().next()
    Fib object, value 5
    >>> start.next().next().next().next().next().next()
    Fib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    Fib object, value 8
    """
    
    def __init__(self, value=0):
        self.value = value
        next_value = 1
        self.next_value = next_value


    def next(self):
        new = self.value + self.next_value
        self.value = self.next_value
        self.next_value = new
        self.next = next()

    def __repr__(self):
        return "Fib object, value " + str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.balance = 0
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.cost:
            return 'You must deposit $'+ str(self.cost - self.balance) +' more.'
        if self.balance == self.cost:
            self.stock -= 1
            return 'Here is your '+ str(self.name) + '.'
        self.stock -= 1
        self.balance -= self.cost
        rv = 'Here is your ' + str(self.name) + ' and $'+ str(self.balance) + ' change.'
        self.balance = 0
        return rv
    def deposit(self,amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) +'.'
        self.balance += amount
        return 'Current balance: $' + str(self.balance)

    def restock(self,amount):
        self.stock += amount
        return 'Current ' + str(self.name)+' stock: ' + str(self.stock)



