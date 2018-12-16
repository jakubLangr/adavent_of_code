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


def evolve(init_state: str, rules: dict, offset: int = 0):
    if '#' in init_state[:3]:
        init_state = '00' + init_state + '00'
        offset += 1
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
    return next_state, offset


target_s1 = '.#...#....#.....#..#..#..#'
target_s3 = '...#.#...#..#.#....#..#..#...#'
s1, o = evolve(init_state, rules_dict)
s2, o = evolve(s1, rules_dict, o)
s3, o = evolve(s2, rules_dict, o)
print(s3)
print(target_s3)
print('S1 : ', find(s1, '#'))
print('Target S1 : ', find(target_s1,'#'))

                           
assert find(target_s1) == find(s1)

def part_one(init_state, rules, n_evol=20):
    offset = 0
    full_rules = {}
    for r in rules:
        p,r = r.split(' => ')
        full_rules[p] = r
    
    next_step = init_state
    for i in range(n_evol):
        next_step, offset = evolve(next_step, full_rules, offset)
        
    ans = [x for x in find(next_step) ]
    return sum(ans)



test_ans = part_one(init_state, rules)
print(test_ans)
# assert test_ans==325

rules = open('day12_rules_input.txt').read().split('\n')

ans = part_one(working_state, rules)
print(ans)
assert ans==3061

prev_guesses = [705, 3059, 3115, 3003] # 3115 too high 

ans = part_one(working_state, rules, 15000)
print(ans)
