# -*- coding:utf-8 -*-
# SOR JACO 迭代求解方程
import numpy as np
import matplotlib.pyplot as plt
from Hilbert_Cholesky import create_H

# raws = 3
# cols = 3




def get_e(x_k, x_k_1):
    #print "x_k ",x_k, " \nx_k_1", x_k_1
    x = np.max(np.fabs(np.array(x_k) - np.array(x_k_1)))
    return x




def jacobi(A, B, x, e, dimession):
    k_e = 555555
    k = 0
    e_list = list()
    while k_e > e:
        y = list()
        for i in range(dimession):
            y.append(x[i])
        for i in range(dimession):
            first = 0
            second = 0
            for j in range(0, i):
                first = first + A[i][j] * y[j]

            for j in range(i+1, dimession):
                second = second + A[i][j] * y[j]
            #print "i %d " % i, " j %d" % j, " Aij %f" % A[i][j], " first %f" % first, " second %f" %second, " B[i] %f" %B[i]
            x[i] = (B[i] - first - second) / A[i][i]
        k_e = get_e(x, y)
        k = k + 1
        print "iteration_k:: %d" % k, " e: %f" % k_e
        print " x: ", x
        e_list.append(k_e)
        print "k: %d" % k, " k_e: %f" % k_e, " x: ", x
    return e_list, x


def SOR(A, B, w, x, e, dimession):
    k_e = 555555
    k = 0
    e_list = list()
    while k_e > e:
        y = list()
        for i in range(dimession):
            y.append(x[i])
        for i in range(dimession):
            first = 0
            second = 0
            for j in range(0, i):
                first = first + A[i][j] * x[j]
                #print "i %d " % i, " j %d" % j, " Aij %f" % A[i][j], " first %f" % first
            for j in range(i+1, dimession):
                second = second + A[i][j] * x[j]

            x[i] = (1.0 - w) * x[i] + w * (B[i] - first - second) / A[i][i]
        k_e = get_e(x, y)
        k = k + 1
        e_list.append(k_e)
        #print "k: %d" % k, " k_e: %f" % k_e, " x: ", x
    return e_list[-1], x, k

def test_SOR_w(step=0.01):
    A = create_H(10)
    b = [float(1.0/x) for x in range(1,11)]
    e = 1e-4
    x_0 = [float(0.0) for x in range(10)]
    x_a = [float(0.0) for x in range(10)]
    x_a[0] = 1.0
    print "A ",A
    print "b ",b
    print "x ", x_0
    w = step
    w_es = list()
    w_ks = list()
    w_s = list()
    while w < 1.999:
        x_0 = [float(0.0) for x in range(10)]
        e_r, x_p, k = SOR(A, b, w, x_0, e, 10)
        error = (get_e(x_a, x_p))/1.0
        # print "iteration:%d, error:%0.10f " %(k, error)
        # print "p_result:",x_p
        w_s.append(w)
        w_ks.append(k)
        w_es.append(error)
        w += step
        #print w
    plt.plot(w_s, w_ks, "g")
    plt.show()
    plt.plot(w_s, w_es, "r")
    plt.show()

if __name__ == '__main__':
    test_SOR_w(0.001)

    # n = 10
    # A = create_H(n)
    # b = [float(1.0/x) for x in range(1,n+1)]
    # e = 1e-4
    # x_a = [float(0.0) for x in range(n)]
    # x_a[0] = 1.0
    # x_0 = [float(0.0) for x in range(n)]
    # e_r, x_p, k = SOR(A, b, 1.25, x_0, e, 10)
    # print "sor_predict [k:%d, e:%.10f]" %(k, (get_e(x_a, x_p))/1.0)
    # print "1.25_x_p:"
    # for i in x_p:
    #     print "%.5f" % (i),


    # n >= 3, 2*D-H fuding, jacobi bu shou lian

    # e_r, x_p = jacobi(A, b, x_0, e, n)
    # print "sor_predict [k:%d, e:%.10f]" %(1, (get_e(x_a, x_p))/1.0)
    # print "1.25_x_p:"
    # for i in x_p:
    #     print "%.5f" % (i),