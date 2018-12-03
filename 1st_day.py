file_object = open('day1_input.txt', 'r')

loaded = file_object.read()
split_s = loaded.split('\n')

num_list = [ int(x) for x in split_s ]

def day_one_b(num_list: list):
    # sum(num_list)

    from collections import defaultdict

    reached_vals = defaultdict(lambda: 0)

    reached_vals[0] = 1
    current_val = 0 

    while True:
        for n in num_list:
            current_val += n
            reached_vals[current_val] += 1
            # import ipdb; ipdb.set_trace()
            if reached_vals[current_val] == 2:
                print(n, current_val, reached_vals)
                return current_val


# assert 0==day_one_b([+1, -1])
# assert day_one_b([+3, +3, +4, -2, -4])==10
assert day_one_b([-6, +3, +8, +5, -6])==5
print(day_one_b(num_list))