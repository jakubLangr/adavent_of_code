file_object = open('day3_input.txt', 'r')

from collections import Counter, defaultdict
from functools import reduce

import pandas as pd


loaded = file_object.read()
split_s = loaded.split('\n')
format_string = lambda arg: arg.split(' ')
formated_list = [ format_string(x) for x in split_s]
df = pd.DataFrame.from_records(formated_list,
                              columns=['Id', '@', 'start','dims'])

def start_to_list(start: str):
    return start[:-1].split(',')

df['start_list'] = df.start.apply(lambda x: start_to_list(x))
df['dims_list'] = df.dims.apply(lambda x: x.split('x'))

def enumerate_area(dim_list: list) -> set:
    """ Currently no offset """
    num_rows = int(dim_list[0])
    num_cols = int(dim_list[1])

    return_list = []
    assert isinstance(num_rows, int) 
    assert isinstance(num_cols, int)
    for i in range(num_rows):
        row_all_coords = list(zip([i] * num_cols, range(num_cols)))
        return_list.append(row_all_coords)
    
    return_list = reduce(lambda x,y: x+y, return_list)
    return set(return_list)


test_start = [1, 3]
test_dims = [4, 2]
expected_result = [(0, 0), (1, 0), (2, 0), (3, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1)]

test_var = enumerate_area(test_dims)
assert enumerate_area(test_dims) == set(expected_result)

def adjust_by_offset(area: set, start_list: list) -> set:
    h_offset = int(start_list[0])
    v_offset = int(start_list[1])
    adjusted_area = [(x + h_offset, y + v_offset) for x, y in area]
    return adjusted_area

interim_result = adjust_by_offset(test_var, test_start)
expected_adjusted_area = [(1, 4), (1, 3), (4, 3),
                          (4, 4), (3, 4), (3, 3), (2, 3), (2, 4)]

assert interim_result==expected_adjusted_area

df['tuple_of_lists'] = pd.Series(list(zip(df.start_list, df.dims_list)))

def lambdable_area(tuple_of_lists):
    start_list = tuple_of_lists[0]
    dims_list = tuple_of_lists[1]

    # import ipdb; ipdb.set_trace()
    area = enumerate_area(dims_list)
    adjusted_area = adjust_by_offset(area, start_list)
    return adjusted_area


df['area'] = df.tuple_of_lists.apply(lambda x: lambdable_area(x))

countable_list = []
for el in df.area:
    for x in el:
        countable_list.append(str(x))

data = Counter(countable_list)
df2 = pd.DataFrame(data, index=['new']).T
df2.new.value_counts()
sum(df2.new.value_counts()) - 249150

df['set_area'] = df.area.apply(lambda x: set(x))

### PART TWO
overlap_list = list()

for e1 in df.iterrows():
    for e2 in df.iterrows():
        overlap_list.append([e1[1].Id, e2[1].Id, len(
            e1[1].set_area.intersection(e2[1].set_area))])

df3 = pd.DataFrame(overlap_list)
df3.columns = [  "id1", "id2", "overlap_num"]

unique_ids = df3.id1.unique()

results_dict = defaultdict(lambda: str)

for id in unique_ids:
    number = df3[df3.id1 == id].overlap_num.sum()
    results_dict[str(id)] = number

df4 = pd.DataFrame(results_dict, index=['num_overlap']).T]
# we can do this as same dimensions of df and df4 
df4['num_area'] = df.dims_list.apply(lambda x: int(x[0])*int(x[1])).values
df4['overlap_amount'] = df4.num_overlap - df4.num_area
