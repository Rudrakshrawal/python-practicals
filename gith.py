#Python uses interpreter that means it directly runs on an virtual machine





spam_amount = 0
#Variable assignment** : Here we create a variable called spam_amount and assign it the value of 0 using =,
#which is called the assignment operator.
----------






print(spam_amount)
#Function calls:. print is a Python function that displays the value passed to it on the screen. 
#We call functions by putting parentheses after their name, and putting the inputs (or arguments) to the function in those parentheses.
-----------






if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam Spam Spam"
print(viking_song)
#Python is prized for its readability and the simplicity.
#Note how we indicated which code belongs to the if. "But I don't want ANY spam!" is only supposed to be printed 
#if spam_amount is positive. But the later code (like print(viking_song)) should be executed no matter what. How do we (and Python) know that?
#The colon (:) at the end of the if line indicates that a new code block is starting. Subsequent lines which are indented are part of that code block.



"But I don't want ANY spam!"
#This code snippet is also our first sighting of a string in Python^
#Strings can be marked either by double or single quotation marks. (But because this particular string contains a single-quote character, 
#we might confuse Python by trying to surround it with single-quotes, unless we're careful.)
# -------------------------



type(spam_amount)
#this function is very useful in python to find the type of a variable. 
#There are 4 types of types-- Float(19.32), Integer(3), boolean(True/False), string("any word written")
# -------------------------
# Operator	Name	Description
# a + b:	Addition	Sum of a and b
# a - b:	Subtraction	Difference of a and b
# a * b:	Multiplication	Product of a and b
# a / b:	True division	Quotient of a and b
# a // b:	Floor division	Quotient of a and b, removing fractional parts
# a % b:	Modulus	Integer remainder after division of a by b
# a ** b:	Exponentiation	a raised to the power of b
# -a:	Negation	The negative of a
# -------------------------








#Order of operations
#The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. 
# Some remember these by a mnemonic such as PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
#----------------





#Builtin functions are the ones that are already implied or used in the python IDE
#-------------------------









# min and max return the minimum and maximum of their arguments, respectively.
print(min(1, 2, 3))
#output 1
print(max(1, 2, 3))
#output 3
#abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))
#both 32
#--------------






# The help() function is possibly the most important Python function you can learn. 
#If you can remember how to use help(), you hold the key to understanding most other functions.





print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

#-----------------------------------









def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
     return min(diff1, diff2, diff3)
#   This creates a function called least_difference, which takes three arguments, a, b, and c.

# Functions start with a header introduced by the def keyword. The indented block of code following the : is run when the function is called.

# return is another keyword uniquely associated with functions. When Python encounters a return statement, it exits the function immediately, and passes the value on the right hand side to the calling context.

# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call help() on a function, it shows the docstring.

# Aside: The last two lines of the docstring are an example function call and result. (The >>> is a reference to the command prompt used in Python interactive shells.) 
# Python doesn't run the example call - it's just there for the benefit of the reader. 
# The convention of including 1 or more example calls in a function's 
# docstring is far from universally observed, but it can be very effective at helping someone understand your function.
print(1, 2, 3, sep=' < ')
#Know how to use a sep func
#----------------------------------






def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
# Hello, Colin
# Hello, Kaggle
# Hello, world
#def function
#-------------------------------------












def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# mult_by_five(x): This function takes an argument x and returns the result of multiplying x by 5.
# call(fn, arg): This function takes two arguments: fn (a function) and arg (an argument to be passed to the function). It calls the function fn with the argument arg and returns the result.
# squared_call(fn, arg): This function also takes two arguments: fn (a function) and arg (an argument to be passed to the function). It calls the function fn twice with the argument arg and returns the result of the second call of fn on the result of the first call.
# The print statement at the end demonstrates the usage of these functions:
# call(mult_by_five, 1): Calls the mult_by_five function with the argument 1, resulting in 5 because 5 * 1 = 5.
# squared_call(mult_by_five, 1): Calls the mult_by_five function with the argument 1, and then calls it again on the result (5). This results in 25 because 5 * 5 = 25.

#---------------------------






def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)


# This code snippet demonstrates the use of the max() function along with a custom function mod_5(x)
#--------------------------












True or True and False

# and is evaluated before or. That's why the first expression above is True. If we evaluated it from left to right, we would have calculated True or True first (which is True), 
# and then taken the and of that result with False, giving a final value of False.






# Booleans are most useful when combined with conditional statements, using the keywords if, elif, and else.
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)




-------
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool("")



-----
#LIST
l=[32,5,32,5,6,72,2]
l.append(3)#add 7 to the list
l.sort(reverse=True)#sort in descending order
l.reverse#reverse the list
print(l.index(72))#gives the index value of the number
print(l,count(72))#to find how many times did that term

#TO Copy LIST
m=l.copy()
m[0]
print(l)

#To insert
l.insert(1,888)#(index,value)
#To Extend
m=[321,342,5,43]
l.extend(m)#if we use the append func then the whole list along with the square brackets will be added in the list

#To add a new list
m=[6,5,3,7,4]
k= l+ m
print(k)

-----

#TUPLE         (Are Immutable)
tup = (3,34,2,5,2)
print(type(tup), tup)
print(tup[2])#to find the value at that index
#slicing
tup2=tup[1:4]#tup[start:end]
print(tup2)#[2,5,2]

#Tuple to list and back to tiple
countries=("italy","russia","china","america","bhutan")
check=list(countries)
check.append("czech_republic")
check.pop(2)#Remove item
check[2]="poland"#Chnages item
countries=tuple(check)
print(countries)

#can also add by making a new tuple

tuple=[3,42,4,4,4,4,4,32,442,3,33,44,2]
res = tuple.count(4)
print('count of 4 in tuple is', res)

res=tuple.index(3)
res=tuple.index(3,4,8)#[to find,from,till]

res = len(tuple)


#the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple
x = 0.125
x.as_integer_ratio()
#output --> (1,8)




planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

# The for loop specifies

# the variable name to use (in this case, planet)
# the set of values to loop over (in this case, planets)
# You use the word "in" to link them together.

# The object to the right of the "in" can be any object that supports iteration. Basically,
# if it can be thought of as a group of things, you can probably loop over it. In addition to lists, we can iterate over the elements of a tuple:
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

# The other type of loop in Python is a while loop, which iterates until some condition is met


#LIST COMPREHENSION
squares = [n**2 for n in range(10)]
squares













--------
#F-String
sentance= "my name is {} and i'm from {}" 
country = "india"
name = "ruu"
print(sentance.format(country, name)


#again
      =print(f"My name is {name} and i'm from {Country}")
      

name=[Ruu]
Country = [Bharat]
bre
--------

#Docsstring
'''written just below a function or just above the end of a defined function'''

def money(n):
    '''haatho ka maail'''
    print(n*"i")
print(money.__doc__)
money(100000)
----------

#BREAK FUNCTION IS USED TO BREAK THE WHILE LOOP NOT TO CANCEL THE WHOLE FUNCTION SO TO DO THAT YOI MUST USE 
exit()#FUNCTION


--------------
#while using a def function we can uuse return and enter a condition to get a True value and return not to get the False value
def is_positive(number):
    return number>0
#return not
def is_negative(number):
    return not number>0





# Going between strings and lists:
# .split() and .join()
str.split() turns a string into a list of smaller strings, breaking on whitespace by default. 
# This is super useful for taking you from one big string to a list of words.

words = claim.split()
words
# ['Pluto', 'is', 'a', 'planet!']
datestr = '1956-01-31'
year, month, day = datestr.split('-')
# str.join() takes us in the other direction, sewing a list of strings up into one long string, using the string it was called on as a separator.
'/'.join([month, day, year])
# '01/31/1956' output


# Dictionaries are a built-in Python data structure for mapping keys to values.

numbers = {'one':1, 'two':2, 'three':3}
# In this case 'one', 'two', and 'three' are the keys, and 1, 2 and 3 are their corresponding values.

# Values are accessed via square bracket syntax similar to indexing into lists and strings.





