'''
# https://pikomat.sk/ulohy/18#uloha-5

Math problem which I decided to solve with Python.

6. Plus minus it fits

In Malpera, sign pyramids were used for accounting. Such a pyramid is initially empty. A plus or minus sign is written in each box in the bottom row. The remaining fields are filled in as follows:

     A plus is written in the box under which there are two boxes with the same signs.
     A minus is written in the box below which there are two boxes with opposite signs.

One such filling of the pyramid with four lines is shown in the picture.
  -
 + -
- - +  

However, the sign pyramid on the mayor's document had 9 lines. There were minus signs in the topmost box and in the leftmost box in the bottom row. What was the sign in the rightmost box in the bottom row? Don't forget to think about both options.
'''
# Solution: Instead of + and - we will be using 1 and 0. and we filter out everything which doesn't have 0 on bottom left and on top.


def bin_transform(s):
    s2 = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s2 += '1'
        else:
            s2 += '0'
    return s2

# Highest number with lenght of 9 in binary is 511.
for i in range(512): 
    foo = bin(i)
    foo = foo.replace('b', '')
    # Leading 0-es
    if len(foo) < 9:
        foo = ('0' * (9-len(foo))) + foo
    elif len(foo) == 10:
        foo = foo[1:]
    # filter out everything with 1 on bottom left
    if foo[-1] == '1':
        continue
    a = foo
    # Apply rules for higher floors
    while len(foo) > 1:
        foo = bin_transform(foo)
        a += ' ' + foo
    if foo == '1':
        continue
    # Print all correct pyramids
    print(a)

# End Result: Bottom right is always 1 (+)
