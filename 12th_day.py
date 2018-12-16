#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:05:03 2018

@author: jakublangr
"""
import ipdb

init_state = '#..#.#..##......###...###' 
rules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""" 

working_state = '##.##..#.#....#.##...###.##.#.#..###.#....##.###.#..###...#.##.#...#.#####.###.##..#######.####..#.'

rules_dict = {}
rules = rules.split('\n')

for r in rules:
    p,r = r.split(' => ')
    rules_dict[p] = r

def find(s, ch="#"):
    return [i for i, ltr in enumerate(s) if ltr == ch]


mapped_repr = find(init_state)


def evolve(init_state: str, rules: dict):
    init_state = '00' + init_state + '00'
    next_state = ''
    for i, p in enumerate(init_state):
        if i>0:
            to_match = init_state[i-2:i+3]
            to_match = to_match.replace('0','.')
            if to_match in rules.keys():
                target = rules[to_match]
                next_state += target
            else:
                next_state += '.'
    
    next_state = next_state.replace('0','')
    return next_state[0:-1]


target_s1 = '.#...#....#.....#..#..#..#'
target_s3 = '...#.#...#..#.#....#..#..#...#'.ljust(35, '.')
s1 = evolve(init_state, rules_dict)
s2 = evolve(s1, rules_dict)
s3 = evolve(s2, rules_dict)
print(s3.rjust(35, '.'))
print(target_s3)
print('S1 : ', find(s1, '#'))
print('Target S1 : ', find(target_s1,'#'))

                           
assert find(target_s1) == find(s1)

next_step = init_state
for i in range(20):
    next_step = evolve(next_step, rules_dict)
    
ans = [x - 20 for x in find(next_step) ]
print(sum(ans))


rules = open('day12_rules_input.txt').read().split('\n')
full_rules = {}
for r in rules:
    p,r = r.split(' => ')
    full_rules[p] = r

next_step = working_state
for i in range(20):
    next_step = evolve(next_step, full_rules)
    # print(find(next_step[i:-i]))
    
ans = [x - 20 for x in find(next_step) ]
print(sum(ans))
assert sum(ans)==3061

prev_guesses = [705, 3059, 3115, 3003] # 3115 too high 


