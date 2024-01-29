'''
     6. Plus mínus to sedí
7 8 9 Sekunda Tercia Kvarta

V Malpere sa pri účtovníctve využívali znamienkové pyramídy. Takáto pyramída je na začiatku prázdna. Do každého políčka v spodnom riadku sa napíše znamienko plus alebo mínus. Zvyšné políčka sa vypĺňajú nasledovne:

    Do políčka, pod ktorým sú dve políčka s rovnakými znamienkami, sa napíše plus.
    Do políčka, pod ktorým sú dve políčka s opačnými znamienkami, sa napíše mínus.

Obrazok

Jedno také vyplnenie pyramídy so štyrmi riadkami je na obrázku. Znamienková pyramída na starostkinom dokumente však mala 9 riadkov. V najvrchnejšom políčku a v políčku, ktoré je najviac vľavo v spodnom riadku, boli znamienka mínus. Aké znamienko bolo v políčku, ktoré je najviac vpravo v spodnom riadku? Nezabudni sa zamyslieť nad oboma možnosťami.


# https://pikomat.sk/ulohy/18#uloha-5
'''

# from itertools import permutations
# from itertools import combinations
# from itertools import combinations_with_replacement

# perm = permutations([1, 2, 3, 4])
# comb = combinations_with_replacement([1, 2, 3], 2)

# for i in list(comb):
#     print(i)

utvar = 8
stas = 0
nestas = 0
for i1 in range(1, utvar+1):
    continue
    for i2 in range(1, utvar+1):
        for i3 in range(1, utvar+1):
            for i4 in range(1, utvar+1):
                for i5 in range(1, utvar+1):
                    sucet = i1 + i2 + i3 + i4 + i5
                    sucet = sucet % 2
                    sucin = i1 * i2 * i3 * i4 * i5
                    sucin = sucin % 2
                    if sucet == 0 and sucin == 1:
                        print(i1, i2, i3, i4, sucet, sucin)
                        stas += 1
                    else:
                        nestas += 1
print(stas, nestas)


# 0:64  0:216   0:512
# 16:240    81:1215 256:3840
# 0:1024    0:7776  0:32768


def bin_transform(s):
    s2 = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s2 += '1'
        else:
            s2 += '0'
    return s2


for i in range(512):  #512
    #print(bin(i))
    foo = bin(i)
    foo = foo.replace('b', '')
    if len(foo) < 9:
        foo = ('0' * (9-len(foo))) + foo
    elif len(foo) == 10:
        foo = foo[1:]
    if foo[-1] == '1':
        continue
    a = foo
    while len(foo) > 1:
        foo = bin_transform(foo)
        a += ' ' + foo
    if foo == '1':
        continue
    print(a)

