case = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""
from typing import List
case = list(map(int, case.split() ))
print(case)



i = 0 

def next_int():
    global i 
    global case 
    i += 1
    return case[i-1]

def read_tree():
    nn, nm = next_int(), next_int()
    children = []
    metadata = []
    for _ in range(nn):
        children.append(read_tree())
    for _ in range(nm):
        metadata.append(next_int())
    return (children, metadata)


def sum_metadata(tuple):
    children, metadata = tuple
    ans= 0
    if not isinstance(metadata, list):
        metadata = [metadata]
    if not isinstance(children, list):
        children = [children]
    for m in list(metadata):
        ans += m
    for c in list(children):
        ans += sum_metadata(c)
    return ans

def value(tuple):
    children, metadata = tuple
    if not children:
        return sum(metadata)
    else:
        ans = 0
        for m in metadata:
            if 1 <= m <= len(children):
                ans += value(children[m-1])

        return ans


root = read_tree()
print(sum_metadata(root))
print(value(root))

i = 0 
case = list(map(int, open('day8_input.txt').read().split()))
 
root = read_tree()
print(sum_metadata(root))
print(value(root))
