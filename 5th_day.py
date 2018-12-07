

from builtins import IndexError


def naive_shrink(polymer: str) -> str:
    while True:
        no_reactions = 0
        new_polymber = ''
        skip_next_iter = False 
        for i in range(len(polymer)):
            if not skip_next_iter:
                fp = polymer[i]
                try:
                    sp = polymer[i+1]
                except IndexError:
                    pass
                if fp.upper()==sp.upper() and fp!=sp:
                    no_reactions += 1
                    skip_next_iter = True 
                else:
                    new_polymber += polymer[i]
        
        polymer = new_polymber
        if no_reactions==0:
            return new_polymber


test_case = 'dabAcCaCBAcCcaDA'
print(naive_shrink(test_case) == 'dabCBAcaDA') 
print(naive_shrink(test_case))
