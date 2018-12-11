import pandas as pd
import numpy as np
import string
import matplotlib.pylab as plt
from scipy import sparse

from pylab import rcParams
rcParams['figure.figsize'] = 10, 15

TESTING = False
REAL = not TESTING

test_input = [
"position=< 9,  1> velocity=< 0,  2>",
"position=< 7,  0> velocity=<-1,  0>",
"position=< 3, -2> velocity=<-1,  1>",
"position=< 6, 10> velocity=<-2, -1>",
"position=< 2, -4> velocity=< 2,  2>",
"position=<-6, 10> velocity=< 2, -2>",
"position=< 1,  8> velocity=< 1, -1>",
"position=< 1,  7> velocity=< 1,  0>",
"position=<-3, 11> velocity=< 1, -2>",
"position=< 7,  6> velocity=<-1, -1>",
"position=<-2,  3> velocity=< 1,  0>",
"position=<-4,  3> velocity=< 2,  0>",
"position=<10, -3> velocity=<-1,  1>",
"position=< 5, 11> velocity=< 1, -2>",
"position=< 4,  7> velocity=< 0, -1>",
"position=< 8, -2> velocity=< 0,  1>",
"position=<15,  0> velocity=<-2,  0>",
"position=< 1,  6> velocity=< 1,  0>",
"position=< 8,  9> velocity=< 0, -1>",
"position=< 3,  3> velocity=<-1,  1>",
"position=< 0,  5> velocity=< 0, -1>",
"position=<-2,  2> velocity=< 2,  0>",
"position=< 5, -2> velocity=< 1,  2>",
"position=< 1,  4> velocity=< 2,  1>",
"position=<-2,  7> velocity=< 2, -2>",
"position=< 3,  6> velocity=<-1, -1>",
"position=< 5,  0> velocity=< 1,  0>",
"position=<-6,  0> velocity=< 2,  0>",
"position=< 5,  9> velocity=< 1, -2>",
"position=<14,  7> velocity=<-2,  0>",
"position=<-3,  6> velocity=< 2, -1>"
        ]


def parse_file(inputs: list):
    update_dict = {}
    list1 = string.ascii_uppercase
    list2 = string.ascii_lowercase
    ids = [ str(p1 + p2) for p1 in list1 for p2 in list2]
    max_n = min_n = 0
    for i in range(len(inputs)):
        p, v  = inputs[i].split("> ")
        p = p.split('=')[1][1:].strip()
        v = v.split("=")[1][1:-1].strip()
        
        x, y = p.split(', ')
        d_x, d_y = v.split(', ')
        
        if int(x) > max_n:
            max_n = int(x)
        if int(x) < min_n:
            min_n = int(x)
        
        update_dict[ids[i]] = int(x), int(y), int(d_x), int(d_y)
        
        
        target_range = max_n - min_n
    return update_dict, target_range



def construct_mat(ud, target_range):
    msg_matrix = np.zeros((int(target_range), target_range), dtype=np.uint8)
    for k in ud.keys():
        x,y,d_x,d_y = ud[k]
        try:
            msg_matrix[x,y] = 1
        except IndexError:
            pass
    sparse_df = pd.DataFrame(msg_matrix).to_sparse()
    # sparse_mat = sparse_df.as_matrix()
    return sparse_df



def plot_matrix(ud, target_range): 
    mat = construct_mat(ud, target_range)
    to_int = lambda x: 1 if isinstance(x, str) else x
    vto_int = np.vectorize(to_int)
    num_array = vto_int(mat)
    plt.imshow(num_array)
    plt.show()
    return num_array
    


# print(msg_matrix)

def update_matrix(ud, target_range):
    for k in ud.keys():
        x,y,d_x,d_y = ud[k]
        new_x = x + d_x
        new_y = y + d_y
        if new_x == 0:
            exit()
        if new_y == 0:
            exit()
        ud[k] = new_x, new_y, d_x, d_y
        # msg_matrix = construct_mat(ud, target_range)
    return ud
    

def find_msg(ud, target_range, num_iter=int(5e4)):
    for i in range(num_iter):
        ud = update_matrix(ud, target_range)
        if i > 10000:
            global curr_n
            curr_n = plot_matrix(ud, target_range)
        print(i)
            
if TESTING:
    ud, target_range = parse_file(test_input)
    msg_matrix = construct_mat(ud, target_range)
    find_msg(msg_matrix, ud, target_range)

if REAL:
    real_input = open('day10_input.txt','r').read().split('\n')
    ud, target_range = parse_file(real_input)
    target_range = int(target_range / 256)
    # curr_epoch = construct_mat(ud, target_range)
    find_msg( ud, target_range)