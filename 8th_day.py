case = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""
from typing import List
case = list(map(int, case.split() ))
print(case)

final_case = list(map(int, open('day8_input.txt').read().split()))

class Tree:
    num_children: int 
    num_metadata: int
    children: List['Node']
    metadata: List[int]

    def __init__(self, ns):
        self.i = 0
        self.ns = ns

    def next_int(self):
        self.i += 1
        return self.ns[self.i-1]

    def read_tree(self):
        nn, nm = self.next_int(), self.next_int()
        children = []
        metadata = []
        for _ in range(nn):
            children.append(self.read_tree())
        for _ in range(nm):
            metadata.append(self.next_int())
        return children, metadata


def sum_metadata(children, metadata):
    ans= 0
    if not isinstance(metadata, list):
        metadata = [metadata]
    if not isinstance(children, list):
        children = [children]
    for m in list(metadata):
        ans += m
    for c in list(children):
        ans += sum_metadata(c,m)
    return ans


children, metadata = Tree(case).read_tree()
print(sum_metadata(children, metadata))

children, metadata = Tree(final_case).read_tree()
print(sum_metadata(children, metadata))
