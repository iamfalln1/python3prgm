'''	Functions can be defined using the def <function name>():
Note: Use proper indentations inside the function.							'''
def hello():
	print('Hello World, This is Python 3 Programming');

hello();

# implementation of function in a program
x = int(input()); # int(input()) must be used because input default to str without defining it
y = int(input());
def cal(): # declaring a function 
	print('Sum is ', x + y)
	print('Difference is ', x - y)
	print('Product is ', x * y)
	print('Qoutient is ', x / y, 'and Reminder is ', x % y)

cal(); # calling the function for running	