import numpy as np
from numpy import *

def can_stop(u1 , u2):
    return (u1-u2) < 0.0001 and u1-u2 > -0.0001


def get_u(A, v):
    u = v
    l_1 = 0
    l_2 = 10.0
    while not can_stop(l_1,l_2):
        l_1 = l_2
        v = np.dot(A, u)
        print"v: ", v
        l_2 = v.max()
        u = v / l_2
        print "l_2: ",l_2
        print "u: ",u
    return u, l_2

def get_u_r(A, v):
    u = v
    l_1 = 0
    l_2 = 10.0
    A = np.linalg.inv(A)
    print A

    while not can_stop(l_1,l_2):
        l_1 = l_2
        v = np.dot(A, u)
        print"v: ", v
        l_2 = 1.0 / v.max()
        u = v * l_2
        print "l_2: ",l_2
        print "u: ",u
    return u, l_2


A = np.array([
    [7,3,-2],
    [3,4,-1],
    [-2,-1,3]
],dtype=np.float64)

B = np.array([
    [6, 2, 1],
    [2, 3, 1],
    [1, 1, 1]
],dtype=np.float64)
S = B - 7*np.eye(3)
v = np.array([1,0.5,0.2],dtype=np.float64)
t = np.array([ 1,0.5228998,0.24219153],dtype=np.float64)
print B.dot(t)
get_u_r(S,v)