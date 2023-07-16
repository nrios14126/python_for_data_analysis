
#### Chapter 2: Python Language Basics ############################################################

### The Python Intepreter #########################################################################

# Python is an interpreted language. The Python interpreter runs a program by executing one 
# statement at a time. To run a Python program from the terminal:
#
# > python hello_world.py

# When using Jupyter Notebooks, the '%run' command executes the code in a specified file in the 
# same process, enabling you to explore the results interactively:
#
# In [1]: %run hello_world.py

### IPython Basics ################################################################################

## Running the IPython Shell **********************************************************************

# When you type just a variable into IPython, it renders a string representation of the object:
import numpy as np
data = {i: np.random.randn() for i in range(7)}
data    # different from print(data)

## Running the Jupyter Notebook *******************************************************************

# One of the major components of the Jupyter project is the notebook, a type of interactive 
# document for code, markup text, data visualizations, and other outputs. The notebook interacts 
# with kernels, which are implementations of the Jupyter interactive computing protocol in any 
# number of languages. To start up Jupyter, run the following command in the terminal:
#
# > jupyter notebook

## Introspection **********************************************************************************

# Using a '?' before or after a variable will display some general information about the object:
# 
# In [1]: ?data
# In [2]: data?

# This is referred to as object introspection. If the object is a function or instance method, the
# docstring (if defined) will also be shown:
def add_numbers(a, b):
    '''
    Add two numbers together
    
    Returns
    -------
    the_sum : type of arguments
    '''
    return a + b

# Using '?' will also describe a function:
#
# In [1]: add_numbers?

# Using '??' will also show the function's source code if possible:
#
# In [1]: add_numbers??

# The question mark has a final usage, which is for searching the IPython namespace. A number of 
# characters with a wildcard (*) will show all names matching the expression:
#
# In [1]: np.*load*?

## The %run Command *******************************************************************************

# You can run any Python file inside the IPython environment using the '%run' command. The script 
# is run in an empty namespace (with no imports or other variables defined) so that the behavior 
# should be identical to running the program on the command line. All of the variables defined in 
# the file will then be accessible (different from importing):
#
# In [1]: %run ipython_script_test.py
# In [2]: print(c)    # where c is defined in the script ipython_script_test.py

# In the Jupyter Notebook, you may also use the related '%load' magic function, which imports a 
# script directly into a code cell:
# 
# In [1]: %load ipython_script_test.py

## About Magic Commands ***************************************************************************

# IPython's special commands (which are not built into Python itself) are known as magic commands. 
# These are designed to facilitate command tasks. A magic command is any commandprefaced with a '%' 
# symbol. As an example, you can check the execution time of any Python statement using '%timeit':
#
# In [1]: %timeit f(1, 2, 3)

# Magic commands can be viewed as command-line programs to be run within the IPython system. Many 
# of them have additional options, which can be viewed using '?':
# In [1]: %debug?

# Some magic functions behave like Python functions and their output can be assigned to a variable:
#
# In [1]: foo = %pwd
# In [2]: print(foo)

# You can explore all the possible magic commands with:
#
# In [1]: %quickref

## Matplotlib Integration *************************************************************************

# The '%matplotlib' magic function configures its integration with the IPython shell:
# In [1]: %matplotlib

# For Jupyter Notebooks, the command is a little different:
# In [1]: %matplotlib inline
import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())
plt.show()

### Python Language Basics ########################################################################

## Language Semantics *****************************************************************************

# When assigning a variable in Python, you are creating a reference to the object on the right-hand 
# side. Consider a list of integers:
a = [1, 2, 3]

# Suppose we assign 'a' to a new variable 'b':
b = a

# In some languages, this would cause the data to be copied. In Python, 'a' and 'b' now refer to 
# the same object (the original list):
a.append(4)
print(b)

# When you pass objects as arguments to a function, new local variables are created referencing the 
# original objects without any copying. If you bind a new object to a variable inside a function, 
# that change will not be reflected in the parent scope. It is therefore possible to alter the 
# internals of a mutable argument:
def append_element(some_list, element):
    some_list.append(element)
    
append_element(a, 5)
print(a)

# In Python, object references have no type associated with them (they are dynamically typed):
a = 5
type(a)

a = 'foo'
type(a)

# Variables are names for objects within a particular namespace; the type information is stored
# in the object itself. Python is a strongly typed language, which means that every object has 
# a specific type (or class), and implicit conversions will occur only in certain circumstances.

# A 'float' type: 
a = 4.5   

# An 'int' type:
b = 2

# Natural (implicit) conversion for addition:
a + b

# You can check that an object is an instance of a particular type using the isinstance() function:
isinstance(a, int)

# You can pass a tuple of options to check across:
isinstance(b, (int, float))

# Objects in Python typically have both attributes and methods:
#    1. Attributes: other objects stored inside the object
#    2. Methods: functions associated with an object that can have access to the object's internal 
#       data and attributes
#
# Both of these are accessed via the syntax obj.attribute_name or obj.method_name()

# Often you may not care about the type of an object but rather only whether is has certain methods 
# or behavior. This is sometimes called "duck typing." For example, you can verify that an object 
# is iterable if it implemented the iterator protocol. For many objects, this means it has an 
# __iter__ method. An alternative way to check is:
def is_iterable(obj):
    try:
        iter(obj)
        return True
    
    except TypeError:
        return False

is_iterable('a string')

is_iterable(5)

# In Python, a module is simply a file with the '.py' extension containing Python code. If we 
# wanted to access the variables and functions defined in 'some_module.py' from another file in the
# same directory we could:
import some_module

result = some_module.f(5)
pi = some_module.PI

# Or, equivalently:
from some_module import g, PI

result = g(5, PI)

# By using the 'as' keyword, you can give imports different variable names:
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)

# To check if two references refer to the same object, use the 'is' keyword. 'is not' is also
# perfectly valid if you want to check that two objects are not the same:
a = [1, 2, 3]
b = a
c = list(a)

a is b

a is not c

# A very common use of 'is' and 'is not' is to check if a variable is 'None', since there is only
# one instance of 'None':
a = None
a is None

## Scalar Types ***********************************************************************************

# Python has a small set of built-in types for handling numerical data, strings booleans, and
# dates/times. These single value types are sometimes called 'scalar types' or scalars.

# The primary Python types for numbers are int and float. An int can store arbitrarily large
# numbers:
i = 17239871

# Floating-point numbers are represented with the Python float type. They can also be expressed
# with scientific notation:
f = 7.243
g = 6.78e-5

# You can write string literals using either single or double quotes:
a = 'one way of writing a string'
b = "another way"

# For multiline strings:
c = '''
This is the first line.
And this is the sencond.
'''

# Multiline strings actually contain the newline characters '\n':
c.count('\n')

# Strings are immutable; you cannot modify a string, however there is a method that allows
# you to substitute parts of a string:
a = 'this is a string'
b = a.replace('string', 'longer string')
b

# Many objects can be converted to a string:
str(5)

# Strings are a sequence of Unicode characters and therefore can be treated like other sequences:
for t in 'text':
    print(t)

list('text')

'text'[:3]

# The backslash character is an escape character, meaning that it is used to specify special 
# characters like '\n' for newline. To write a string literal with backslashes, you will need to 
# escape them:
my_string = '\\this\\string\\has\\backslashes'
my_string

# If you have a string with lots of backslashes and no special characters, you can use a raw
# string instead:
my_string = r'\this\string\has\backslashes'
my_string

# Adding two strings together concatenates them and produces a new string:
a = 'this is the first half '
b = 'and this is the second half.'
a + b

# String objects have a format method that can be used to substitute arguments:
#
# {0:.2f} means to format the first argument as a float with two decimal places
# {1:s} means to format the second argument as a string
# {2:d} means to format the third argument as an exact integer
#
template = '{0:.2f} {1:s} are worth US${2:d}'
template.format(4.5560, 'Argentine Pesos', 1)

# In modern Python, Unicode has become the first-class string type to enable more consistent 
# handling of ASCII and non-ASCII text. You can convert to Unicode assuming you know the character 
# encoding:
my_string = 'espa\xf1ol'
    
my_bytes = my_string.encode('utf-8')
type(my_bytes)

my_string = my_bytes.decode('utf-8')
type(my_string)

# Though you may seldom need to do so, you can define your own byte literals by prefixing a string 
# with 'b':
bytes_val = b'this is bytes'
bytes_val

string_val = bytes_val.decode('utf-8')
string_val

# The two boolean values in Python are written as 'True' and 'False'. Comparisons and other 
# conditional expressions evaluate to either True or False. Boolean values are combined with the
# 'and' and 'or' keywords:
True and True

False or True

# The str, bool, int, and float types are also functions that can be used to cast values to those
# types as well:
s = '3.14159'

fval = float(s)

int(fval)

bool(fval)

bool(0)

# None is the Python null value type. If a function does not explicitly return a value, it will
# implicitly return None:
a = None

a is None

b = 5

b is not None

# None is also a common default value for function arguments:
def add_and_maybe_multiply(a, b, c = None):
    result = a + b
    
    if c is not None:
        result = result * c
        
    return result

# While a technical point, it's worth bearing in mind that None is not only a reserved keyword but
# also a unique instance of the NoneType:
type(None)

# The built-in datetime module provides datetime, date, and time types. The datetime object 
# combines information stored in data and time:
from datetime import datetime

# October 29, 2011 at 8:30:21pm
dt = datetime(2011, 10, 29, 20, 30, 21)

# Get the day
dt.day

# Get the minute
dt.minute

# Get the time
dt.time()

# Get the date
dt.date()

# The strftime method formats a datetime as a string:
dt.strftime('%m/%d/%Y %H:%M')

# Strings can be converted (parsed) into datetime objects with the strptime function:
datetime.strptime('20091031', '%Y%m%d')

# You can replace certain fields of a datetime object:
dt.replace(minute=0, second=0)

# Since datetime.datetime is an immutable type, methods like these always produce new objects. The 
# difference of two datetime objects produces a datetime.timedelta type:
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
delta

# Adding a timedelta to a datetime produces a new shifted datetime:
dt + delta

## Control Flow ***********************************************************************************

# The 'if' statement checks a condition that, if true, evaluates the code in the block. It can be 
# optionally followed by one or more 'else if' blocks and a catch-all 'else' block if all of the 
# conditions are false:
x = 7

if x < 0:
    print('Negative')
    
elif x == 0:
    print('Zero')
    
elif 0 < x < 5:
    print('Positive, less that 5')
    
else:
    print('Positive, greater than or equal to 5')

# If any of the conditions are true, no further 'elif' or 'else' blocks will be reached. With a 
# compound condition using 'and' or 'or', conditions are evaluated left to right and will 
# short-circuit (end before finishing if logical conclusion is reached).

a = 5
b = 7
c = 8
d = 4

# In this expression c < d will not get evaluated since the a < b is true:
if a < b or c < d:
    print('Made it')

# for loops are for iterating over a collection/iterator. The syntax is:
#
# for value in collection:
#     block_of_code
#

# You can advance a for loop to the next iteration, skipping the remainder of the block, using the 
# 'continue' keyword:
sequence = [1, 2, None, 4, None, 5]

total = 0

for value in sequence:
    if value is None:
        continue
    total += value
    
total

# A for loop can be exited altogether with the 'break' keyword:
sequence = [1, 2, 0, 4, 6, 5, 2, 1]

total_until_5 = 0

for value in sequence:
    if value == 5:
        break
    total_until_5 += value
    
total_until_5 

# Note that the 'break' keyword only terminates the innermost loop; any outer loops will continue
# to run:
for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))

# If the elements in the collection or iterator are sequences, they can be unpacked into variables 
# in the loop:
# 
# for a, b, c in iterator:
#    # TODO
#

# A while loop specifies a condition and a block of code that is to be executed until the condition 
# evaluates to False or the loop is ended with 'break':
x = 256

total = 0

while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2

total

# 'pass' is the no-op statement in Python. It can be used in blocks where no action is to be taken, 
# or as a placeholder for code not yet implemented:
if x < 0:
    print('negative')
    
elif x == 0:
    # TODO
    pass

else:
    print('positive')

# The range() function returns an iterator that yields a sequence of evenly spaced integers:
range(10)

# Converting to list object:
list(range(10))

# Both start, end, and step can be given:
list(range(0, 20, 2))

# Decreasing order form:
list(range(20, 0, -2))

# A ternary expression in Python allows you to combine an if-else block that produces a value into 
# a single line or expression:
# 
# value = true_expr if condition else false_expr
#
# This is the same as:
# 
# if condition:
#     value = true_expr
# else:
#     value = false_expr
