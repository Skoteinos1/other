'''6. Zvláštny list
V liste bolo napísané:
„Dve prirodzené čísla. Obe zaokrúhlite na desiatky. Podiel zaokrúhlených čísel je rovnaký ako podiel pôvodných.
Súčin zaokrúhlených je o 295 väčší než súčin pôvodných.
Súčet zaokrúhlených je o 6 väčší než súčet pôvodných. Viete, čo máte robiť.“
Atarka
Aké mohli byť dve počiatočné prirodzené Atarkine čísla? Nájdi všetky možnosti.'''

import itertools

nums = [k for k in range(300)]

# Developing a function to round to a multiple
def round_to_multiple(number, multiple):
    division = (number / multiple) + 0.01 
    division = round(division,0)
    # return multiple * round(number / multiple)
    return multiple * division

for subset in itertools.combinations_with_replacement(nums, 2 ):
    a = subset[0]
    b = subset[1]

    a1 = round_to_multiple(a, 10)
    b1 = round_to_multiple(b, 10)

    
    try:
        if a1*b1 == (a*b)+295:
            if a1+b1 == a+b+6:
                if b/a == b1/a1:
                    print(a, b, a1, b1, )
    except:
        pass

# for subset in itertools.product(stuff, repeat=4):
