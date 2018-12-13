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

rules_dict = {}

rules = rules.split('\n')

for r in rules:
    p,r = r.split(' => ')
    rules_dict[p] = r

def find(s, ch="#"):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def evolve(init_state: str, rules: dict):
    next_state = '..'
    for i, p in enumerate(init_state):
        if i>1:
            to_match = init_state[i-2:i+3]
            if to_match in rules.keys():
                ipdb.set_trace()
                target = rules[to_match]
                next_state += target
            else:
                next_state += p
    
    return next_state[2:]

s1 = evolve(init_state, rules_dict)
print(s1)
print('Init state : ', find(init_state, "#"))
print('S1 : ', find(s1, '#'))
target_s1 = '...#...#....#.....#..#..#..#...........'
print('Target S1 : ', find(target_s1,'#'))
