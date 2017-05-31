import numpy as np
from numpy import *

def can_stop(u1 , u2, e):
    return abs(u1-u2) < e


def get_u(A, v, e):
    u = v.copy()
    l_1 = 0
    l_2 = 100000000000000.0
    k = 0
    while not can_stop(l_1, l_2, e):
        l_1 = l_2
        v = np.dot(A, u)
        l_2 = np.abs(v).max()
        #print l_2
        u = v / l_2
        k += 1
    return u, l_2, k


def get_u_r(A, v, e):
    u = v
    l_1 = 0
    l_2 = 10.0
    A = np.linalg.inv(A)
    print A

    while not can_stop(l_1, l_2, e):
        l_1 = l_2
        v = np.dot(A, u)
        print"v: ", v
        l_2 = 1.0 / np.abs(v).max()
        u = v * l_2
        print "l_2: ",l_2
        print "u: ",u
    return u, l_2


if __name__ == '__main__':
    A = np.array([
        [5, -4, 1],
        [-4, 6, -4],
        [1, -4, 7]
    ], dtype=np.float64)
    V_a = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    B = np.array([
        [25, -41, 10, -6],
        [-41, 68, -17, 10],
        [10, -17, 5, -3],
        [-6, 10, -3, 2]
    ], dtype=np.float64)
    V_b = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float64)
    er = 0.00001
    print er
    u, l, k = get_u(A, V_a, er)
    print "iteration:%d, l:%0.20f " %(k, l), "x:",u
    u, l, k = get_u(B, V_b, er)
    print "iteration:%d, l:%0.20f " % (k, l), "x:", u

# A = np.array([
#     [7,3,-2],
#     [3,4,-1],
#     [-2,-1,3]
# ],dtype=np.float64)
#
# B = np.array([
#     [6, 2, 1],
#     [2, 3, 1],
#     [1, 1, 1]
# ],dtype=np.float64)
# S = B - 7*np.eye(3)
# v = np.array([1,0.5,0.2],dtype=np.float64)
# t = np.array([ 1,0.5228998,0.24219153],dtype=np.float64)
# print B.dot(t)
# get_u_r(S,v)
