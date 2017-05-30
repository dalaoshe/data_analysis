# -*- coding:utf-8 -*-
# SOR JACO 迭代求解方程
import numpy as np
from Hilbert_Cholesky import create_H

raws = 3
cols = 3

data_file = "data.txt"
A = list()
B = list()
x = list()
e = 0

file = open(data_file,"r")


for i in range(raws):
    ai = [float(x) for x in file.readline().strip().split()]
    A.append(ai)

B = [float(x) for x in file.readline().strip().split()]
x = [float(x) for x in file.readline().strip().split()]
e = float(file.readline().strip())

A = np.array(A)
B = np.array(B)
x = np.array(x)
print A, B, A.dtype, B.dtype
#
#
# for i in range(raws):
#     for j in range(cols):
#         print "%d " % A[i][j],
#
#     print ""
#
# for i in range(raws):
#     print "%d " % B[i],
#
# print ""


def get_e(x_k, x_k_1):
    print x_k, " \n", x_k_1
    x = np.max(np.fabs(x_k - x_k_1))
    return x




def jacobi(A, B, x, e):
    k_e = 555555
    k = 0
    while k_e > e:
        y = list()
        for i in range(raws):
            y.append(x[i])
        for i in range(raws):
            first = 0
            second = 0
            for j in range(0, i):
                first = first + A[i][j] * y[j]
                print "i %d " % i, " j %d" % j, " Aij %f" % A[i][j], " first %f" % first
            for j in range(i+1, raws):
                second = second + A[i][j] * y[j]

            x[i] = (B[i] - first - second) / A[i][i]
        k_e = get_e(x, y)
        k = k + 1
        print "k: %d" % k, " k_e: %f" % k_e, " x: ", x

def SOR(A, B, w, x, e):
    k_e = 555555
    k = 0
    while k_e > e:
        y = list()
        for i in range(raws):
            y.append(x[i])
        for i in range(raws):
            first = 0
            second = 0
            for j in range(0, i):
                first = first + A[i][j] * x[j]
                print "i %d " % i, " j %d" % j, " Aij %f" % A[i][j], " first %f" % first
            for j in range(i+1, raws):
                second = second + A[i][j] * x[j]

            x[i] = (1.0 - w) * x[i] + w * (B[i] - first - second) / A[i][i]
        k_e = get_e(x, y)
        k = k + 1
        print "k: %d" % k, " k_e: %f" % k_e, " x: ", x

#SOR(A, B, 0.9, x, e)
jacobi(A, B, x, e)
print "result:"
print np.dot(A,x)