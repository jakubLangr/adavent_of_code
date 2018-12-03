file_object = open('day2_input.txt', 'r')

loaded = file_object.read()
split_s = loaded.split('\n')


from collections import Counter

def day_two(list_of_strings: list):
    eval_list = [ Counter(x) for x in list_of_strings]
    num_two = 0
    num_three = 0 
    #import ipdb; ipdb.set_trace()
    for el in eval_list:
        if sum([x for x in  el.values() if x==2 ])>=2:
            num_two += 1
        if sum([x for x in  el.values() if x==3 ])>=3:
            num_three += 1
        # print(num_two, num_three)
    
    print(num_three, num_two)
    return num_three * num_two


test_case = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab"]


# print(day_two(split_s))
import Levenshtein
from collections import defaultdict
import pandas as pd

test_case2 = [
"abcde",
"fghij",
"klmno",
"pqrst",
"fguij",
"axcye",
"wvxyz"
]

def chars_apart(str1, str2):
    edit_list = Levenshtein.editops(str1, str2)
    return len(edit_list)

def part_two(str_list: list):
    dd = defaultdict(lambda: int)
    for s in str_list:
        for t in str_list:
            dd[f'({s},{t})'] = chars_apart(s, t)

    df = pd.DataFrame(dd, index=[0]).T
    df = df[df.values==1]
    return df.index



test = part_two(test_case2)
soln = part_two(split_s)
print(soln)
edits = Levenshtein.editops(soln[0],soln[1])
target= Levenshtein.apply_edit(edits,soln[0], soln[1])
print(target)
# part_two(test_case2)=='fgij'