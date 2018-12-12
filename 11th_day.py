#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:06:09 2018

@author: jakublangr
"""
from collections import namedtuple
import numpy as np
from scipy.signal import convolve2d

cell = namedtuple('Cell',['rack_id','y_coordinate','serial_n'])

def sum_cell(cell: tuple):
    rack_id = cell[0] + 10 
    count = rack_id * cell[1]
    count += cell[2]
    count = count * rack_id
    hundred_digit = str(count)[-3]
    count = int(hundred_digit) - 5 
    return count


assert sum_cell((3,5,8))==4
assert sum_cell((122,79,57))==-5
assert sum_cell((217,196,39))==0
assert sum_cell((101,153,71))==4

def find_greatest(grid: np.array ):
    max_val = grid.max()
    coords = np.where(grid == max_val)
    if len(coords[0])!=1:
        coords = coords[0][0], coords[1][0]
    return coords


def generate_grid(serial_n: int):
    arr = np.zeros((300,300), dtype=np.int8)
    for x in range(1, 301):
        for y in range(1,301):
            arr[x-1,y-1] = sum_cell((x,y, serial_n))
    return arr
            
# 
def part_one(serial_n: int, filter_size: tuple = (3,3)):
    offset_adj = int(filter_size[0] - 2)
    grid = generate_grid(serial_n)
    conv_filter = np.ones(filter_size)
    new_grid = convolve2d(grid, conv_filter, fillvalue=-99999)
    coords = find_greatest(new_grid)
    x,y = int(coords[0]), int(coords[1])
    while x in [0,300] or y in [0,300]:
        new_grid[x,y] = 0 
        coords = find_greatest(new_grid)
        x,y = int(coords[0]), int(coords[1])
    
    final_max = new_grid.max()
    return x-offset_adj, y-offset_adj, final_max


assert part_one(42)[:2]==(21,61)
assert part_one(18)[:2]==(33,45)
assert part_one(9995)[:2]==(33,45)

def part_two(serial_n):
    total_power = []
    values = {}
    for i in range(1,50):
        filter_size = (i,i)
        info = part_one(serial_n, filter_size)
        total_power.append(info[2])
        values[str(filter_size)] = info
    
    highest_powa = max(total_power)
    print(highest_powa)
    for k in values.keys():
        if values[k][2]==highest_powa:
            print(values[k])
            print(k)


#part_two(18)
#part_two(42) 
part_two(9995)
    
    
