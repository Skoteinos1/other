import os
os.system('clear') # Cisti Terminal
os.system('spd-say Done')

# DataFrame --------------------------------------------------------------------
# https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp
import pandas
import numpy

df = pandas.DataFrame() # Creates empty df
# if df.empty: checks if df is empty
df = pandas.DataFrame(numpy.random.rand(10,10)*100)  # Creates random df

d = {'A1': [1, 2, float('NaN')], 'A2': [3, float('NaN'), float('NaN')], 'A3': [4, 5, float('NaN')], 'A4': [float('NaN'), float('NaN'), float('NaN')]}       # 2 simple dataframes for testing
d1 = pandas.DataFrame(data=d)
d = {'A1': [float('NaN'), 12], 'A2': [13, 14], 'B3': [14, 15], 'B4': [14, 15], 'B5': [float('NaN'), float('NaN')]}
d2 = pandas.DataFrame(data=d)
d3 = pandas.DataFrame({'rating': [90, 85, 82, 88, 94, 90, 76, 75],
                   'points': [25, 20, 14, 16, 27, 20, 12, 15]},
                   index=list('abcdefgh'))

df.loc[:,'A'] = None    # Ads 'A' column with None values

# df.set_value(2,'A', 100)  # Sets Value, could be fastest if it would work
df.loc[1,'A'] = 200         # Sets Value
df.at['ROW', 'COLUMN'] = 10  # Sets Value

pandas.set_option('display.max_rows', None) # Zobrazuje cely DataFrame
d1 = 'Dictionary'

d2 = { "points": [100, 120, 114],
       "total": [350, 340, 402]}
d2 = pandas.DataFrame(d2)

d1 = pandas.DataFrame.from_dict(d1, orient='index') # Converts Dictionary to DataFrame

d1 = d1.rename(columns={0: 'datum'}) # Renames First Column

dfNew = d1.merge(d2, left_index=True, right_index=True,how='outer', suffixes=('', '_y'))  # Joins 2 Dataframes
# dfNew = pandas.merge(d1, d2, on='Attribute')  # Other way to merge
dfNew.drop(dfNew.filter(regex='_y$').columns, axis=1, inplace=True)

df = pandas.concat([d1, d2], ignore_index=False) # Joins 2 df's

len(df.index)  # fastest wat to count rows


# print(df.head(10))
# new_df = df[(df['doRecommend'] != True) & (df['doRecommend'] != False )]
# print(df.isnull().sum())
# df[df.Cards == 4]
# df.sort_values(by='Income',ascending=False).head()
# new_df = df['doRecommend'] != True
# between_30_and_35 = insurance_df[(insurance_df['age'] > 30) & (insurance_df['age'] < 35 )]
# new_df = df[df.doRecommend != True].sample(10)


df = df.dropna(axis=1, how='all') # Drops Nan columns
df = df.dropna(inplace=True, axis=0)
df = df.dropna(subset=['reviews.text'])

df = df.loc[:,~df.apply(lambda x: x.duplicated(),axis=1).all()].copy()  # Removes Duplicated columns. 1st col priority

df = df.sum(level=0)  # Joins duplicated indexes

print(df.mul(10)) # multiplies df by 10
print(df.div(10)) # divides df by 10
df['COLUMN'] += 'string'  # adds string to every value in column
df.index = df.index + "string" # adds string to every value in index

df = pandas.read_csv("Advertising.csv")
df_results = pandas.DataFrame(columns=['Predictor', 'R2 Train', 'R2 Test'])
# e = {'Predictor': ['TV', 'Radio', 'Newspaper', 'Multi'], 'R2 Train': [a[0], b[0], c[0], d[0]], 'R2 Test': [a[1], b[1], c[1], d[1]]}
# df_results = pandas.DataFrame(data=e)
# df_results = df_results.set_index(['Predictor'])

# MATRIX ------------------------------------
# Code: Transposing a Matrix
# You can perform transpose over numpy objects by calling np.transpose() or ndarray.T.
#  Code: Inverting a Matrix
# numpy.linalg.inv() is used to calculate the inverse of a matrix, if it exists.


# Inline if -------------------------------------------------------------------
print("YES") if 5 == 3 else print("NO")

# Date time -------------------------------------------------------------------
import time
current_time = time.strftime("%H_%M", time.localtime())

import datetime
cas = '2000-01-01 10:00:00'

cas = datetime.datetime.strptime(cas, '%Y-%m-%d %H:%M:%S') # String na datetime

cas = cas.strftime("%Y-%m-%d")  # Datetime na string

# Measure speed of code
import time  # Put in beginning
st_ex = time.time() # get the start time
st_cpu = time.process_time() # get the start time
print('Real time:', time.time() - st_ex, 's    CPU time:', time.process_time() - st_cpu, 's') # get the execution time  # Put in the end


# Dictionary -------------------------------------------------------------------
dic1 = {'a': 3}
dic2 = {}
dic_join = {**dic1, **dic2} # Spaja dictionaries

for key in sorted(dic1):  # Sort Dictionary
    dic2[key] = dic1[key]

dic1['new'] = dic1.pop('old')  # Rename key
dic1.get('a')
dic1.get('b', 'not in dic1')


# Exceptions -------------------------------------------------------------------
'''
Import Error - import fails
Index Error - out of range index
Name Error - unknown variable
Syntax Error - code can't be parsed properly
Type Error
Value Error'''
# Exception Handling
try:
    pass
except ZeroDivisionError:
    pass # if 3/0
except (ValueError, TypeError):
    pass  # only ony those 2 errors
except:
    pass  # on rest of errors
finally:
    pass  # this code always runs, no matter if there was or wasn't error

# Raising exceptions
pass
# raise ValueError
pass
# raise NameError("Invalid Name!")

try:
    pass
except Exception as e: print(e)

try:
    pass
except:
    print('Error')
    raise  # re-raise whatever exception occured

try:
    pass
except ZeroDivisionError:
    pass # if 3/0
else:
    pass # runs if there was no error

# Assertions - sanity check - expression is tested, when false, exception is raised
x = "welcome"
#if condition returns False, AssertionError is raised:
assert x != "hello", "x should be 'hello'"  # AssertionError: x should be 'hello'

# File -------------------------------------------------------------------------
os.path.isfile('file.txt')  # Checks if file exists
os.path.isdir('new_folder')  # Checks if directory exists
# modes: r - read, w - write, a - append, b - binary(for non-text files, image and audio), r+ - read and write, wb-

# Method1
f = open("file.txt", "w")
f.write('Hello')
f.close()

# Method2: With ensures file is properly closed
with open("movies.txt", "w") as f:
    f.write('Hello')

# Method3
try:
    file1 = open("file.txt", "r")
finally:
    file1.close()  # file is closed even if error occures


file1 = open("file.txt", "r")
read_content = file1.read(1)  # reads first char
read_content = file1.read(10)  # reads next 10 chars
read_content = file1.read()  # reads until EOF
read_content = file1.readlines()  # list with lines
# with for loop:
for line in file1:
    print(line)
f.close()

file_created = os.path.getmtime('file.txt')
os.utime('file.txt', (file_created, file_created))
file_created = datetime.datetime.utcfromtimestamp(file_created).strftime('%Y-%m-%d')

os.rename('file.txt', 'file2.txt')
size = os.path.getsize('file.txt')


# For loop ---------------------------------------------------------------------
lst = ['a', 'b', 'c']
for i, row in enumerate(lst, start=0):
    print(lst[i], row)
    if i == 50:
        break
else:
    print('Unbroken')  # Runs if there is no break, same in while loop


# Functional Programing ----------------------------------------------------------------------------------------------------------------

# Generators 
# They don't allow indexing, but can be iterated through with for loop. Can be created with function and yeald statement.
# They generate 1 item at a time, so they don't have the memory restrictions of lists, can be infinite
def inf_fives():
    while True:
        yield 5
for i in inf_fives():
    print(i)
# Finite generators can be converted into lists by passing them as arguments to the list function
def nums(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(nums(11)))  # [0,2,4,6,8,10]
# Better performance, lower memory usage because of lazy(on demand) generation of values. We don't have to wait until all elements
# have been generated before we can start use them.

# Lambda 
# Anonymous function
lambda x: x+5,7  # lambda arguments: vyraz, hodnota na dosadenie
my_list = ['dddd','a','bb','ccc']
my_list.sort(key=lambda s: len(s))  # sorts list by length of words
# lambdas can be assigned to variables like normal functions

# Decorators 
# Modify function with other function. When you don't want to modify first function.
def decor(func):
    def wrap():
        func()
    return wrap

@decor
def wrap():
    pass

# Recursion - self reffence. Indirect recurion when 2 functions point at each other
def factorial(x):
    if x == 1:      # base case, without it it will run forever
        return 1
    else: 
        return x * factorial(x-1)

# Sets - similar to lists, unordered, can't be indexed, can't have duplicate values, faster to check if element is in set than in list
foo = {1,2,3}
bar = {3,4,5}
foo.add(x)
foo.remove(x)
foo.pop()  # removes an arbitrary element
foo | bar  # {1, 2, 3, 4, 5}
foo & bar  # {3}
foo - bar  # {1, 2}
foo ^ bar  # {1, 2, 4, 5}

# itertools - counts up infinetely from a value
#     cycle - ifinetely iterates through iterable
#     repeat - repats object infinetely or specified number of times
#     takewhile - takes items from iterable while predicate functionsremains True
#     chain - combines several iterables ine one long one
#     accumulate - returns a running total of values in an iterable


# List -------------------------------------------------------------------------
# Tuples are faster than lists, but can't be changed
lst = [5, '2', 'nan']
lst2 = [3, 5]
# List can be add and multiplied same way as strings
lst + lst2  # [5, '2', 'nan', 3, 5]
lst2*2  # [3, 5, 3, 5]

c = list(lst2)  # creates copy of a list
range # creates a list of sequential numbers
list(range(2,9,2)) # [2, 4, 6, 8]
tab = [[[0 for k in range(9)] for j in range(9)] for i in range(10)]
lst = [float(x) for x in lst] # Converts List of numbers to float
lst = [float(x) for x in lst if float(x) == float(x)] # Converts List of numbers to float and drops nan's
lst = [5] * 3  # [5, 5, 5]
lst = [i for i in range(5)]  # [0, 1, 2, 3, 4]
lst = [i**3 for i in range(5)]  # [0, 1, 8, 27, 64]
lst = [i**2 for i in range(10) if i**2 % 2==0]  # [0,4,16,36,64] with enforced condition
lst = [2*i for i in range(10**100)]  # too big range will cause memory error. It is solved by Generators
lst = [[] for i in range(5)]  # [[], [], [], [], []]
lst = [[j for j in range(3)] for i in range(5)]  # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
lst = [i for i in range(5) if i % 2 == 0]  # [0, 2, 4]
all(i >= 30 for i in lst)  # Checks if all values in list are bigger than 30
#  if any(x == 'some_val' for x in lst):
max(lst)  # maximalna hodnota
min(lst)  # minimalna hodnota
lst.count('item')  # how many times is item in list
lst.sort()  # Sort list
lst = list(dict.fromkeys(lst))  # Removes duplicates from list
lst = list(set(lst) & set(lst2)) # List intersection
lst.reverse() 
total = sum(lst)

groceries = ["apples", "milk", "cheese", "bread"]
groceries.append("coffee") 	# ["apples", "milk", "cheese", "bread", "coffee"] append dava na koniec
groceries.insert(0, "carrots") # ["carrots","apples", "milk", "cheese", "bread", "coffee"] insert dava na zaciatok alebo vybranu poziciu
groceries.insert(1, "peas") # ["carrots","peas","apples", "milk", "cheese", "bread", "coffee"]
groceries.pop() # ["carrots", "peas", "apples", "milk", "cheese", "bread"]
groceries.pop(0) # ["peas","apples", "milk", "cheese", "bread"]
groceries.remove("cheese") # ["peas","apples", "milk", "bread"]
groceries = [ele for ele in groceries if ele not in ['cheese', 'peas']]  # ["apples", "milk", "bread"]

# Slicing is same as with strings, works on tuples
nums = [0, 1, 2, 3, 4, 5]
nums[0:1]  # [0]  - same as with range, first number is in, second is not
nums[2:4]  # [2,3] 
nums[:3]  # [0,1,2] - from start to 3
nums[3:]  # [3,4,5] - 3 to end
nums[0:4:2]  # [0,2] - third number is step
nums[1:-1]  # [1,2,3,4]
nums[::-1]  # Easy reverse list


# Magic Methods ----------------------------------------------------------------
# have __ at begining and end, common use is operator overloading
'''
sub -
mul *
truediv /
floordiv //
mod % 
pow **
and &
xor ^
or |
lt <
le <=
eq ==
ne !=
gt >
ge >=
len len()
getitem  indexing
setitem  assign value
delitem  delete values
iter    iteration
contain     in
'''


# Map & Filter------------------------------------------------------------------
# map - takes a function and iterable as arguments and returns a new iterable with function applied to each argument
# filter - removes itterable which don't match a predicate
nums = [11,22]
res = list(filter(lambda x: x%2 == 0, nums))


# Math -------------------------------------------------------------------------
print(divmod(5, 5))  # (1, 0)
print(5 // 5)  #  1
print(5 % 5)  #  0
print(10**3)  # 1000
print(9**1/2)  # 3

# ------------ OOP -------------------------------------------------
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
    def miau(self):
        print('Miau')

felix = Cat('ginger', 4)
stumpy = Cat('brown',3)
felix.miau()

# Inheritance
class Animal:   # Animal is superclass
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):  # Cat is subclass
    def purr(self):
        print('purr')
class Dog(Animal):
    def bark(self):
        print('bark')
fido = Dog('Fido', 'brown')

# Data Hiding
# Key part of OOP is encapsulation, packaging variables and functions into single objects
# _variable - weakly private
# __variable - strongly private
# In python only a convention. from module import * will not import them, but they can still be called
class Spam:
    __egg = 7
s = Spam()
foo = s._Spam__egg
s.__egg # will not work

# Class & Static Methods
# Class methods are passed with cls parameter, marked with @classmethod
@classmethod
def something(cls, variable):
    return cls(variable*5)
# Nothing special about staticmethods, marked with @staticmethod

#Properties - way of customizing access to instance attributes
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return True
pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = False  # shouldn't work because property is read only

class Pizza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter   # Use setter function to edit property
    def pineapple_allowed(self, value):
        self._pineapple_allowed = value
pizza2 = Pizza2(['cheese', 'tomato'])
pizza2.pineapple_allowed = 'Yes'


# Precedence ----------
False == False or True # True
False == (False or True) # False
# == before OR
""" Highest to lowest precedence
**      exponent
~ + -   Complement, unary plus and minus (method names for last two +@ and -@)
* / % //
+ -
>> <<   Right and left bitwise shift
&       Bitwise and
^ |     Bitwise exclusive 'OR' and regular 'OR'
<= < > >= Comparison operators
<> == != equality operators
= %= /= //= -= += Assignment operators
is, is not identify operators
in, not in membership operators
not and or logical operators
"""

# Pickle -----------------------------------------------------------------------
import pickle
pth = 'Path/to/file'  # Has to be defined because of debug bug
def save_pickle(file, data1):
    if '.pkl' not in file:
        file += '.pkl'
    pkl_file = open(pth + file, 'wb')
    pickle.dump(data1, pkl_file)
    pkl_file.close()

def load_pickle(fl_nm):
    if '.pkl' not in fl_nm:
        fl_nm += '.pkl'
    try:
        pkl_file = open(pth + fl_nm, 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
    except:
        print('Missing pickle table:', fl_nm)
        # pkl_file = open(file, 'wb')
        data1 = ''
    return data1


# Print in color ---------------------------------------------------------------------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING +'Some Text'+ bcolors.ENDC)    


# Regular Expresions - RegEx --------------------------------------------------------------------
# Verify string patterns and perform substitutions in string
import re
re.match # matches begining of string
re.search # checks if there is a match and returns object with methods 
re.findall  # returns list of matches
re.group()  # what was matched
re.start()  # starting position
re.end()    # ending position
re.span()  # tuple (re.start, re.end)
pattern = r'xxx'
replace_with = 'foo'
what_string = 'axxxa'
re.sub(pattern, replace_with, what_string, count=0) # count how many replacements max

pattern = r'spam'
if re.match(pattern, 'spamspam'):
    print('Match')

re.match(r'spam', 'eggspam')  # False
re.match(r'spam', 'spamegg')  # True
re.search(r'spam', 'eggspam')  # True
re.findall(r'spam', 'eggspamsausagespam') # ['spam', 'spam']

match = re.search(r'spam', 'eggspamsausage')
match.group()  # spam
match.start()  # 4
match.end()     # 7
match.span()    # (4,7)

s = "My name is David. Hi David."
s2 = re.sub(r'David', 'Amy', s)

# Metacharacters
# . matches everything except \n
# ^ matches start of string
# $ matches end
# if you want match metacharacters, you have to use \$ \.

re.match(r'gr.y', 'grey')  # True  # matches grXy
re.match(r'gr.y', 'gray')  # True
re.match(r'gr(a|e)y', 'gray')  # matches gray or grey
re.match(r'^gr.y$', 'gray')  # True
re.match(r'^gr.y$', 'graya')  # False

re.search(r'[aeiou]', 'grey') # True
re.search(r'[aeiou]', 'myth') # False
r'[a-z]' # matches lowercase
r'[A-Z]' # matches uppercase
r'[^A-Z]' # matches everything except uppercase
r'[0-9]' # matches numbers
r'[a-zA-Z]' # matches all letters

re.search(r'[A-Z][A-Z][0-9]', 'AB5') # True
re.search(r'[A-Z][A-Z][0-9]', 'A5') # False

# * 0-n reps
# + 1-n reps
# ? 0-1 reps
# {a, b}  a-b reps
# {5} 5+ reps
re.match(r'a(b)*', 'a')  # True
re.match(r'a(b)*', 'abbbc')  # True

match = re.match(r'a(bc)(de)(f(g)h)i', 'abcdefghijklmno')
match.group()  # abcdefghi
match.group(0)  # abcdefghi
match.group(1)  # bc
match.group(2)  # de
match.groups()  # ('bc', 'de', 'fgh', 'g')

match = re.match(r'(?P<first>abc)(?:def)(ghi)', 'abcdefghijklmno')
match.group('first')  # abc
match.groups()  # ('abc', 'ghi')  # ?: group is skipped, ?P<group_is_named>

re.match(r'(.+) \1', 'word word')  # True  # matches 2 same words with space between them # \1 is 1 repetition
# \d matches digits
# \w matches word characters
# \s matches whitespace
# \D \S \W - opposite of lowercase version
# \A match beginning of a string
# \Z match end of a string
# \b matches empty string between \w a \W
# \B matches empty string anywhere else

# email extraction
s = 'Contact me on some@mail.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)', s)
match.group()  # some@mail.com


# String -------------------------------------------------------------------------------------------------------------------------------
# String can be indexed like list. each character is like single element
s = ''
s = 'Brian\'s mother'  # Brian's mother
print('spam'*3)  # spamspamspam
s = s.replace("a", 'b')
s = s.split('\n')
s = s.split(";", 1) # Splits on first occurance
s = ' '.join(s) # list to string
s = s[1:]  # removes first
s = s[:1]  # keeps first
s = s[:-1]  # removes last
s = s[-1:]  # keeps last
s = s[0::2]  # Every second character
s = s[::-1]  # Reversed string
s = s.lower()
s = s.upper()
s.startswith("a")  # True if first char is a
s.endswith('.')  # True if last char is .
x = s.count('apple')  # counts number of occurances
s = s.strip('=')  # Strips = from end and beginning
s = s.replace('1', '2')
# search_list = [lambda s: [p.strip() for p in s.split('\n')]]
s = [i.strip() for i in s] # Strip List of strings
s = [i.lower() for i in s] # List of strings to lower chars
s = [i for i in s if i]  # Removes '' from list
s = list(dict.fromkeys(s))  # Removes duplicates from list
num = 3
s = f'hanning{num}.pdf' # add variable to string

print(s, num)
print("{} is {} years old!".format(s, num))  # prints message with variables
print(s, "is", num, "years old!")

# insert values using index references
print("You worked {0} this month and earned ${1} per day".format(num_days = 22, pay_per_day = 50))
# insert values using empty placeholders
print("You worked {} this month and earned ${} per day".format(num_days = 22, pay_per_day = 50))
# also works with named a rguments
print("{x}").format(x=5)


# Code speed, execution duration -------------------------------------------------------------------
import time
start_time = time.time()
# TIMED CODE GOES HERE
print("--- %s seconds ---" % (time.time() - start_time))


# Variables -------------------------------------------------------------------
foo = float('nan')
if not isinstance(foo, str):  # Checks if foo is string
    pass
foo = input('press Enter...')  # Enter value to terminal
del foo  # deletes variable


# Ternary Operator ------------------------------------------------------------
a = 7
b = 1 if a > 5 else 42
if a > 5:
    b = 1
else:
    b = 42

# Theory -------------------------------------------------------------------
# Immutable: str, int, float, bool, bytes, tuple - you can't change them after being defined.
# Mutable: list set dict
x = (1, 2)
y = x  # Make copy of immutable
y is x  # False because they point to different objects
x = (1, 2, 3)
print(x, y)  # (1, 2, 3) (1, 2)

x = [1, 2]
y = x  # Make refference to Mutable
x[0] = 100
print(x, y)  # [100, 2] [100, 2]
y is x  # true because they reference to each other

# Python evaluates NOT first, than AND than OR 

None # represents absence of value, it is False when converted to boolean and is returned by def which doesn't return anything

# defs -------------------------------------------------------------------
def aaa(x, y):
    print(x, y)  # 1  2

aaa(1, 2)
aaa(y = 2, x = 1)
aaa(*[1, 2])

def bbb(x, y, z=True, w=False):
    print(x, y)  # 1  2
    print(z, w)  # 3  4

bbb(*[1, 2], **{'z':3, 'w':4})


def ccc(x, y, *args):
    print(args)  # Tuple: (3, 'sadsad')
    pass

ccc(1, 2, 3, 'sadsad')


def ddd(*args, **kwargs):
    print(args, kwargs)  # () {'y': 2, 'x': 1}
    print(kwargs['x'])  # 1
    pass

ddd(y = 2, x = 1)


# Running directly vs import -------------------------------------------------------------------

if __name__ == "__main__":
    print('Running directly')  # This part will not run if you import from different module


# Major 3rd party lib's ------------------------------------------------------------------------
'''
Django - Most frequent web framework, used by instagram, disqus
CherryPy, Flask - popular web frameworks
BeautifulSoup - Webscraping
matplotlib - graphs
NumPy - multidimensional arrays
SciPy - upg on numpy
Panda3D - 3D games
pygame - 2D games
'''

# Packages ---------------------------------------------------------------------------------------
# If you want to create package for PyPl which could be installed by pip, this is folder structure
'''
MyPackage/
    LICENSE.txt
    README.txt
    setup.py
    mypackage/
        __init__.py
        mypackage.py
        mypackage2.py
'''
# If you want to create executable file
# For Win: py2exe, PyInstaller, cx_Freeze
# for Mac: py2app, PyInstaller, cx_Freeze