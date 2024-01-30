# https://pikomat.sk/ulohy/22#uloha-3
'''
4. Breakfast

Ten people sat down at a round table. Each of them received breakfast with their name tag. Then they all stood up and shuffled randomly so that no one was sitting in front of their breakfast. Everyone tasted it and decided they wanted their food back. However, they remained seated and instead of replanting, they turned the table so that as many people as possible had their food in front of them again.
    Prove that we can always turn the table so that at least two people have their food in front of them. Prove that we don't always have to know how to turn the table so that at least three people have their food in front of them.
'''

import itertools

# def which checks most matches for "Random" alocation of seats
def tab_test(tabl):

    mx = 0
    # positions of food
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Turns table and prints if there are 2 or more matches
    for k in range(10):
        foo = [i for i, j in zip(tabl, tab) if i == j]
        if len(foo) > mx:
            mx = len(foo)
        if len(foo) > 2:
            print(foo)
            print(tabl)
            print(tab, '\n')
            break

        tab.append(tab[0])
        del tab[0]
    return mx


# Guess this is a proof that we can't always turn table, so that there are 3 people with their original brakfast    
tab_test([1, 10, 9, 8, 7, 5, 4, 3, 2, 6])
tab_test([1, 6, 2, 7, 3, 8, 4, 9, 5, 10])

results=[0,0,0,0,0,0,0,0,0,0,0]

for perm in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    results[tab_test(perm)] += 1

print(results)  # [0, 0, 1183200, 1825900, 494950, 103440, 18450, 2400, 450, 0, 10]

# There are 1183200 positions where max 2 matches can be achieved


