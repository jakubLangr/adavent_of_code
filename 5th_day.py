


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

polymer = test_case = 'dabAcCaCBAcCcaDA'
stack = []
for c in polymer[1:]:
    if len(stack)!=0: pp = stack[-1]
    if stack and c.upper()==pp.upper() and c!=pp:
        stack.pop()
    else:
        stack.append(c)

ss = ''.join(stack)
print(ss.endswith('abCBAcaDA'))
# print(naive_shrink(test_case) == 'dabCBAcaDA') 
polymer = open('day5_input.txt').read().strip()


stack = []
for c in polymer[1:]:
    if len(stack)!=0: pp = stack[-1]
    if stack and c.upper()==pp.upper() and c!=pp:
        stack.pop()
    else:
        stack.append(c)

print(len(stack))