'''	Functions can be defined using the def <function name>():
Note: Use proper indentations inside the function.							'''
def hello():
	print('Hello World, This is Python 3 Programming'); # atleast one whitespce is needed 

hello();
print("Calculator Function:")
# implementation of function in a program
x = int(input("Enter a Number:- ")); # int(input()) must be used because input default to str without defining it
y = int(input("Enter another Number:- "));
def cal(): # declaring a function 
	print('Sum is ',x + y)
	print('Difference is ',x - y)
	print('Product is ',x * y)
	print('Qoutient is ',x / y, 'and Reminder is ',x % y)

cal(); # calling the function for running	