'''      Creating Variables
	Variables are containers for storing data values.
	Unlike other programming languages, Python has no command for declaring a variable.
	A variable is created the moment you first assign a value to it.'''
print("Python Programming at College of Engineering, Attingal")
x = 5;
y = "CEAL";
print(x)
print(y)
# Variables do not need to be declared with any particular type and can even change type after they have been set.
x = 10; # x is of type int
y = "Daksha_Yanthra"; # y is of type str
print(x)
print(y)
# String variables can be declared either by using single or double quotes:
x = "IEEE";
# is the same as
x = 'IEEE';
print(x,y)
''' Assign Value to Multiple Variables
	Python allows you to assign values to multiple variables in one line: '''
x,y,z = 'apples','oranges','bananas'
print(x,y,z)
print(x)
print(y)
print(z)
x = y = z = 'hello world'
print(x)
print(y)
print(z)
''' Output Variables
	The Python print statement is often used to output variables.
	To combine both text and a variable, Python uses the + character:'''
x = 'awesome';
print('Python is ' + x)
# You can also use the + character to add a variable to another variable:
x = 'IEEE';
y = ' is Institute of Electrical and Electronics Engineers.';
z =x + y;
print(z)
# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
'''	Global Variables
	Variables that are created outside of a function is called Global variables. 
	They can be accessed both outside as well as inside of a function '''
x = 'Kerala';
def myfunc():
	print(x+" is God's own country") ;

myfunc()

''' Global Variables as accesseble globally but locally declared variables is accessable to the function 
    where it is declared '''
x = "the devil" # Globally Declared Variable
def myfunc():
  x = "Lucifer Morningstar" # Locally Declared Variable
  print("I am " + x)

myfunc()

print("I am " + x)
''' We can also Declare variable globally inside a function using global keyword '''
def myfunc():
  global x # x is declared globally 
  x = "powliyanu, powerfullanu......"

myfunc()

print("Python " + x)
