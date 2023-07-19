
#### Chapter 3: Built-in Data Structures, Functions, and Files ####################################

### Data Structures and Sequences #################################################################

## Tuple ******************************************************************************************

# A tuple is a fixed-length, immutable sequence of objects.

# Can be formed with no parentheses:
tup = 4, 5, 6
tup

# Or with parentheses:
alt_tup = (4, 5, 6)
alt_tup

# You can convert any sequence or iterator to a tuple:
tuple([1, 2, 3, 4])

# Elements can be accessed with square brackets:
tup[0]

# While the objects stored in a tuple may be mutable themselves, once a tuple is created it's not 
# possible to modify which object is stored in each slot:
tup = ('foo', [1, 2], True)

# Append an element to nested list:
tup[1].append(3)
tup

# You can concatenate tuples using the + operator:
(4, None, 'foo') + (6, 0) + ('bar',)

# Multiplying a tuple by an integer has the effect of concatenating together that many copies of 
# the tuple:
('foo', 'bar') * 4

# If you try to assign to a tuple-like expression of variables, Python will attempt to unpack the 
# values:
tup = (4, 5, 6)
a, b, c = tup
c

# Even sequences with nested tuples can be unpacked:
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d

# Using this functionality, you can easily swap variable names, a task which in many languages
# might look like:
a, b = 1, 2
tmp = a 
a = b
b = tmp

# But in Python, it's as simple as:
a, b = 1, 2
b, a = a, b

# A common use of variable unpacking is iterating over sequences of tuples/lists:
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')

# You can also just pluck the first few elements from a sequence using *rest:
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a, b, rest)

# The 'rest' bit is sometimes something you want to discard; there is nothing special about the 
# 'rest' name. By convention, programmers will use '_' to indicate values that are to be discarded:
a, b, *_ = values

# Since the size and contents of a tuple cannot be modified, it is very light on instance methods. 
# A useful one is count, which counts the number of occurrences of a value:
a = (1, 2, 2, 2, 3, 4, 2)
a.count(2)

## List *******************************************************************************************

# In contrast to tuples, lists are variable length and their contents can be modified in-place. You 
# can define them with square brackets:
a = [2, 3, 7, None]

# Lists and tuples are semantically similar and can be used interchangeably in many functions. The 
# list function is frequently used in data processing as a way to materialize an iterator or 
# generator expression:
gen = range(10)

gen

list(gen)

# Elements can be appended to the end of the list with the append method:
b = ['foo', 'peekaboo', 'baz']
b.append('dwarf')
b

# Using insert you can insert an element at a specific location in the list:
b.insert(1, 'red')
b

# Warning: 'insert' is computationally expensive compared with 'append', because references to 
# subsequent elements have to be shifted internally to make room for the new element.

# If you need to insert elements at both the beginning and end of a sequence, try exploring 
# collections.deque, a double-ended queue

# The inverse operation to insert is pop, which removes and returns an element at a particular 
# index:
b.pop(2)
b

# By default, 'pop' will remove the last element:
b.pop()
b

# Elements can be removed by value with 'remove', which locates the first such value and removes it 
# from the list:
b.append('foo')
b.remove('foo')
b

# You can check if a list contains a value using the 'in' keyword:
'dwarf' in b

# Warning: checking whether a list contains a value is a lot slower than doing so with a dictionary 
# or set, as Python makes a linear scan across the values of the list, whereas it can check the 
# others (based on hash tables) in constant time.

# Similar to tuples, adding two lists together with + concatenates them:
[4, None, 'foo'] + [7, 8, (2, 3)]

# If you have a list already defined, you can append multiple elements to it using the 'extend' 
# method:
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
x

# Note that list concatentation by addition is a comparatively expensive operation since a new list 
# must be created and the objects copied over. Using 'extend' to append elements to an existing 
# list, especially if you are building up a large list, is usually preferred:
#
# # Slower
# everything = []
# for chunk in list_of_lists:
#     everything = everything + chunk
# 
# # Faster
# everything = []
# for chunk in list_of_lists:
#     everything.extend(chunk)

# You can sort a list in-place (without creating a new object) by calling its sort method:
a = [7, 2, 5, 1, 3]
a.sort()
a

# 'sort' has a few options that will occasionally come in handy. One is the ability to pass a 
# secondary sort key (a function that produces a value to use to sort the objects):
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
b

# The built-in bisect module implements binary search and insertion into a sorted list. 
# 'bisect.bisect' finds the location where an element should be inserted to keep it sorted, while 
# 'bisect.insort' actually inserts the element into that location:
import bisect
c = [1, 2, 2, 2, 3, 4, 7]

bisect.bisect(c, 5)

bisect.insort(c, 5)

c

# You can select sections of most sequence types by using slice notation, which in its basic form 
# consists of start:stop passed to the indexing operator:
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]

# Slices can also be assigned to with a sequence:
seq[3:4] = [6, 3]
seq

# While the element at the 'start' index is included, the 'stop' index is not included, so that the 
# number of elements in the result is stop - start

# Either the start or stop index can be omitted, in which case they default to the start of the 
# sequence and the end of the sequence, respectively:
seq[:5]

seq[3:]

seq[:]

# Negative indices slice the sequence relative to the end:
seq[-4:]

seq[-6:-2]

# A step can also be used after a second colon:
seq[::2]

# A clever use of this is to pass -1, which has the effect of reversing a list/tuple:
seq[::-1]

## Built-in Sequence Functions ********************************************************************

# It's common when iterating over a sequence to want to keep track of the index of the current 
# item. Python has a built-in function enumerate() which returns a sequence of (i, value) tuples:
some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
mapping

# The sorted() function returns a new sorted list from the elements of any sequence:
sorted([7, 1, 2, 6, 0, 3, 2], key=lambda x: -x)

# The 'zip' function pairs up the elements of a number of lists, tuples, or other sequences to 
# create a list of tuples:
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
list(zipped)

# A very common use of zip is simultaneously iterating over multiple sequences:
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print(f'{i}: {a}, {b}')

# Given a zipped sequence, zip can be applied to unzip the sequence:
pitchers = [('Nolan', 'Ryan'), ('Randy', 'Johnson'), ('Curt', 'Schilling')]
first_names, last_names = zip(*pitchers)

first_names

last_names

# 'reversed' iterates over the elements of a sequence in reverse order:
list(reversed([1, 2, 3, 4, 5]))

# Keep in mind that reversed() is a generator, so it does not create the reversed sequence until 
# materialized (with list() or a for loop)

## Dictionaries ***********************************************************************************

# Dictionaries are likely the most important built-in Python data structure. A more common name for 
# it is 'hash map' or 'associtative array'. It is a flexibly sized collection of key-value pairs, 
# where key and value are Python objects. 
dict1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
dict1

# You can access, insert, or set elements using the same syntax for lists/tuples:
dict1[7] = 'an integer'

dict1

dict1['b']

# You can check if a dict contains a key using the same syntax used for checking whether a 
# list/tuple contains a value:
'b' in dict1

# You can delete values either using the del keyword or the pop method (which simultaneously
# returns the value and deletes the key):
dict1[5] = 'some value'
dict1['dummy'] = 'another value'
dict1

del dict1[5]
dict1

# For dicts, pop() has no default behavior (as it did with lists):
ret = dict1.pop('dummy')
dict1

# The popped value:
ret

# You can access the keys and values with iterator methods:
list(dict1.keys())

# While the key-value pairs are not in any particular order, these functions output the keys and 
# values in the same order
list(dict1.values())

# You can merge one dict into another using the update method:
dict1.update({'b': 'foo', 'c': 12})

# The update method changes dicts in-place, so any existing keys in the data passed to update() 
# will have their old values discarded
dict1

# It's common to end up with two sequences that you want to pair up element-wise in a dict:
#
# mapping = {}
# for key, value in zip(key_list, value_list):
#     mapping[key] = value
#

# Since a dict is essentially a collection of 2-tuples, the dict function accepts a list
# of 2-tuples:
# 
mapping = dict(zip(range(5), reversed(range(5))))
mapping 

# It's also common to have logic like:
# 
# if key in some_dict:
#     value = some_dict[key]
# else:
#     value = default_value
# 

# Thus, the dict methods get and pop can take a default value to be returned, so that
# the above if-else block can be written simply as:
# 
# value = some_dict.get(key, default_value)

# Sometimes the default value is another collection, like a list:
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter

# The setdefault() method returns the value of the item with the specified key. If the
# the specified key does not exist, it'll return a default value:
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
by_letter

# The built-in collections module has a useful class for defaultdict, which makes this
# even easier. To create one, you pass a type or function for generating the default
# value for each slot in the dict:
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
by_letter

# While the values of a dict can be any Python object, the keys generally have to be immutable
# objects like scalar types (int, float, string) or tuples (all objects within need to be 
# immutable too). The technical term here is hashability, which you can check with hash():
hash('some string')

hash((1, 2, (2, 3)))

## Sets *******************************************************************************************

# A set is an unordered collection of unique elements. You can think of them as dicts, but with 
# keys only (no values). A set can be created in two ways:
a = set([2, 2, 2, 1, 3, 3])
b = {1, 2, 3}

# Sets support mathematical set operations like union, intersection, difference, and 
# symmetric difference:
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

a.union(b)

a.intersection(b)

# Like dicts, set elements must be immutable (hashable). You can also check if a set is a subset 
# (or superset) of another set:
{1, 2, 3}.issubset(a)

a.issuperset({1, 2, 3})

# Sets are equal iff their contents are equal:
{1, 2, 3} == {3, 2, 1}

## Comprehensions *********************************************************************************

# List comprehensions allow you to concisely form a new list by filtering the elements of a 
# collection, transforming the elements passing the filter, in one expression:
# 
# result = [expression for value in collection if condition]
# 
# # Equivalent for loop:
# result = []
# for value in collection:
#     if condition:
#         result.append(expression)
# 

# For example, given a list of strings, we could filter out strings with length 2 or less and also
# convert them to uppercase like so:
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

# Set and dictionary comprehensions are natural extensions, producing sets and dicts in an
# idiomatically similar way instead of lists:
# 
# dict_comp = {key_expr: value_expr for value in collection if condition}
#
# set_comp = {expr for value in collection if condition}

# Now suppose we wanted a set containing just the lengths of the strings contained in the 
# collection:
unique_lengths = {len(x) for x in strings}
unique_lengths

# We could also express this more formally using the map function:
set(map(len, strings))

# Suppose we have a list of lists containing some English and Spansih names:
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

# Now suppose we wanted to get a single list of all names with two or more
# e's in them. We could do this with a for loop:
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
names_of_interest

# However, you can actually wrap this whole operation up in a single nested list comprehension. The 
# for parts of the comprehension are arranged according to the order of nesting, and any filter 
# condition is put at the end as before:
result = [name for names in all_data for name in names if name.count('e') >= 2]
result

# Another example where we flatten a list of tuples of integers into a simple list of integers:
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened

### Functions #####################################################################################

# Functions are the primary and most important method of code organization and reuse in Python. If 
# you anticipate needing to repeat the same or very similar code more than once, if may be worth 
# writing a function

# To declare a function in Python:
def my_function(x, y, z = 1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)

# Note that there is no issue with having multiple return statements. If Python reaches the end of 
# a function without encountering a return statement, None is returned.

# Each function can have positional arguments and keyword arguments. Keyword arguments are used to 
# specify default values or optional arguments. The main restriction here is that keyword arguments 
# must follow positional arguments, but you can specify the keyword arguments in any order.

## Namespaces, Scope, and Local Functions *********************************************************

# Functions can access variables in two different scopes: global and local. An alternative and more
# descriptive name describing a variable scope is a namespace. Any variables that are assigned 
# within a function by default are assigned to the local namespace. The local namespace is created 
# when the function is called and immediately populated by the function's arguments. After the 
# function is finished, the local namespace is destroyed. 

# Assigning variables outside of the function's scope is possible, but they must be declared as 
# global:
def bind_a_variable():
    global a
    a = []
bind_a_variable()
a

# You can return multiple values from a function:
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c
a, b, c = f()

# What's happening here is that the function is actually just returning one object, a tuple, which
# is then being unpacked into the result variables:
returned_tuple = f()
returned_tuple

# An alternative approach is to return a dictionary:
def f():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}
returned_dict = f()
returned_dict

## Functions are Objects **************************************************************************

# Since Python functions are objects, many constructs can be easily expressed that are difficult to
# do in other languages. Consider the following list:
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 
          'West virginia?']

# Suppose we wish to clean these list items. One way to do this is to use built-in string methods 
# along with the re standard library module for regular expressions. 
import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
result = clean_strings(states)
result

# An alternative approach is to make a list of the operations you want to apply to a particular set 
# of strings:
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

# Make a list of the functions (treat as objects)
clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

# A more functional pattern like this enables you to easily modify how the strings are transformed 
# at a very high level:
result = clean_strings(states, clean_ops)
result

## Anonymous (Lambda) Functions *******************************************************************

# Python also has support for so-called anonymous or lambda functions, which are a way of writing 
# functions consisting of a single statement:

# Using a regular function definition
def short_function(x):
    return x * 2

# Equivalent action with a lambda function
equiv_anon = lambda x: x * 2

# Lambda functions are especially useful in data analysis because there are many cases where data 
# transformations will take functions as arguments. It's often less typing to pass a lambda 
# function as opposed to writing out a full function:
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)

# As another example, suppose you wanted to sort a collection of strings by the number of unique 
# letters:
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
strings

## Currying: Partial Argument Application *********************************************************

# Currying is computer science jargon that means deriving new functions from existing ones by 
# partial argument applications:

# Define a function that takes two inputs
def add_numbers(x, y):
    return x + y

# Curry up a new function that calls the previous function with partial inputs. The second 
# argument to add_numbers() is said to be curried:
add_five = lambda y: add_numbers(5, y)
add_five(7)

# The built-in functools module can simplify this process using the partial function:
from functools import partial
add_five = partial(add_numbers, 5)

## Generators *************************************************************************************

# Having a consistent way to iterate over sequences is accomplished by means of the iterator 
# protocol, a generic way to make objects iterable. For example, iterating over a dict yields the
# dict keys:
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)

# When you write the above, the Python interpreter first attempts to create an iterator out of 
# some_dict:
dict_iterator = iter(some_dict)
dict_iterator

# An iterator is any object that will yield objects to the interpreter when used in a context like 
# a loop. Most methods expecting a list or list-like object will also accept any iterable object:
list(dict_iterator)

# A generator is a concise way to construct a new iterable object. Whereas normal functions execute 
# and return a single result at a time, generators return a sequence of multiple results lazily, 
# pausing after each one until the next one is requested. To create a generator, use the 'yield' 
# keyword instead of 'return':
def squares(n=10):
    print(f'Generating squares from 1 to {n ** 2}')
    for i in range(1, n + 1):
        yield i ** 2

# When you actually call the generator, no code is immediately executed:
gen = squares()
gen

# It is not until you request elements from the generator that it begins executing the code:
for x in gen:
    print(x, end=' ', flush=False)

# Another even more concise way to make a generator is by using a generator expression. This is a 
# generator analogue to list, dict, and set comprehensions:
gen = (x ** 2 for x in range(100))
gen

# This is completely equivalent to the following:
def _make_gen():
    for x in range(100):
        yield x ** 2
        
gen = _make_gen()
gen

# Generator expressions can be used instead of list comprehensions as function arguments in many
# cases:
sum(x ** 2 for x in range(100))

dict((i, i**2) for i in range(5))

# The standard library itertools module has a collection of generators for many common data 
# algorithms. For example, groupby takes any sequence and a function, grouping consecutive elements 
# in the sequence by return value of the function:
import itertools

first_letter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))

## Exception Handling *****************************************************************************

# Handling errors or exceptions gracefully is an important part of building robust programs. In 
# data analysis, many functions only work on certain kinds of input. Suppose we wanted a version of 
# float() that fails gracefully, returning the input argument:
def attempt_float(x):
    try:
        return float(x)
    except:
        return x

# The code in the except part of the block will only be executed if float(x) raises an exception:
attempt_float('1.2345')

attempt_float('not a number')

# You might want to only suppress ValueError, since a TypeError (the input was not a string or 
# numeric value) might indicate a legitimate bug in your program:
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x
    
# You can catch multiple exception types by writing a tuple of exception types instead (parentheses 
# are required):
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

# In some cases, you may not want to suppress an exception, but you want some code to be executed 
# regardless of whether the code in the try block succeeds:
f = open('some_file.txt', 'w')

try:
    f.write('Hello World!')
finally:
    f.close()    # Here the file handle f will always get closed

# Similarly, you can have code that executes only if the try block succeeds:
f = open('another_file.txt', 'w')
try:
    f.write('Hello World')
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()

### Files and Operating System ####################################################################

# To open a file for reading and writing, use the built-in open() function with either a relative 
# or absolute path:
path = r'C:\Users\nazri\Desktop\book_code\python_for_data_analysis\segismundo.txt'

# Modes: 'r' for read (default), 'w' for write, and 'a' for append
f = open(path, 'r')

# We can treat the file handle f like a list and iterate over the lines:
for line in f:
    pass

# The lines come out of the file with the EOL markers intact, so you'll often see code to get an 
# EOL-free list of lines:
lines = [line.rstrip() for line in open(path)]
lines

# When you use open to create file objects, it's important to explicitly close the file when you're 
# finished with it. Closing the file releases its resources back to the operating system:
f.close()

# One way to make it easier to clean up open files is to use the with statement, which will 
# automatically close the file f when exiting the with block:
with open(path, encoding='utf8') as file_object:
    lines = [line.rstrip() for line in file_object]
lines

# When using write mode, a new file would have been created, overwriting any one in its place. 
# There is also the 'x' file mode, which creates a writable file but fails if the file path already 
# exists. 

# For readable files, the most common methods are 'read', 'seek', and 'tell'. 'read' returns a 
# certain number of characters from the file. What constitutes a character is determined by the 
# file's encoding:
file_object = open(path, encoding='utf8')
file_object.read(10)

# The read method advances the file handle's position by the number of bytes 'read'. 'tell' gives 
# you the current position:
file_object.tell()

# 'seek' changes the file position to the indicated byte in the file:
file_object.seek(3)

file_object.read(1)

file_object.close()

# The default behavior for Python files is 'text mode', which means that you intend to work with 
# Python strings (i.e., Unicode). This contrasts with 'binary mode', which you can obtain by 
# appending 'b' onto the file mode. 

# If you open the file in 'rb' mode instead, 'read' requests exact number of bytes:
with open(path, 'rb') as file_object:
    data = file_object.read(10)
data

# Depending on the text encoding, you may be able to decode the bytes to a str object, but only if 
# each of the encoded Unicode characters is fully formed:
data.decode('utf8')

# Beware using seek when opening files in any mode other than binary. If the file position falls in 
# the middle of the bytes defining a Unicode character, then subsequent reads will result in an 
# error:
file_object = open(path, encoding='utf8')
file_object.read(5)
file_object.seek(4)
file_object.read(1)
