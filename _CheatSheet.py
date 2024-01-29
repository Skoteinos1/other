import os
os.system('clear') # Cisti Terminal


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

df = df.dropna(axis=1, how='all') # Drops Nan columns

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


# File -------------------------------------------------------------------------
os.path.isfile('file.txt')  # Checks if file exists
f = open("file.txt", "w")
f.write('Hello')
f.close()

file1 = open("file.txt", "r")
read_content = file1.read()
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


# List -------------------------------------------------------------------------
lst = [5, '2', 'nan']
lst2 = [3, 5]
c = list(lst2)  # creates copy of a list
tab = [[[0 for k in range(9)] for j in range(9)] for i in range(10)]
lst = [float(x) for x in lst] # Converts List of numbers to float
lst = [float(x) for x in lst if float(x) == float(x)] # Converts List of numbers to float and drops nan's
lst = [5] * 3  # [5, 5, 5]
lst = [i for i in range(5)]  # [0, 1, 2, 3, 4]
lst = [[] for i in range(5)]  # [[], [], [], [], []]
lst = [[j for j in range(3)] for i in range(5)]  # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
lst = [i for i in range(5) if i % 2 == 0]  # [0, 2, 4]
all(i >= 30 for i in lst)  # Checks if all values in list are bigger than 30
#  if any(x == 'some_val' for x in lst):
lst.sort()  # Sort list
lst = list(dict.fromkeys(lst))  # Removes duplicates from list
lst = list(set(lst) & set(lst2)) # List intersection
lst.reverse() 
total = sum(lst)

groceries = ["apples", "milk", "cheese", "bread"]
groceries.append("coffee") 	# ["apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(0, "carrots") # ["carrots","apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(1, "peas") # ["carrots","peas","apples", "milk", "cheese", "bread", "coffee"]
groceries.pop() # ["carrots", "peas", "apples", "milk", "cheese", "bread"]
groceries.pop(0) # ["peas","apples", "milk", "cheese", "bread"]
groceries.remove("cheese") # ["peas","apples", "milk", "bread"]


# Math -------------------------------------------------------------------------
print(divmod(5, 5))  # (1, 0)
print(5 // 5)  #  1
print(5 % 5)  #  0
print(10**3)  # 1000


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


# String -----------------------------------------------------------------------
s = ''
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

# Variables -------------------------------------------------------------------
foo = float('nan')
if not isinstance(foo, str):  # Checks if foo is string
    pass
foo = input('press Enter...')  # Enter value to terminal


os.system('spd-say Done')

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


# Runninc directly vs import -------------------------------------------------------------------

if __name__ == "__main__":
    print('Running directly')  # This part will not run if you import from different module