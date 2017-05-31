import numpy as np



def f1(x):
    return x**3-x-1.0
def f1_p(x):
    return 3.0*(x**2)-1.0

def f2(x):
    return -x**3 + 5.0*x
def f2_p(x):
    return -3.0*(x**2)+5.0


def newton_method(f, f_p, x_0, eps_1, eps_2, lamd):
    k = 0
    x_k = x_0
    x_k_pre = x_0
    while abs(f(x_k)) > eps_1 or abs(x_k - x_k_pre) > eps_2:
        s = f(x_k) / f_p(x_k)
        x_k_pre = x_k
        x_k = x_k_pre - s
        i = 0
        lamd_k = lamd
        while abs(f(x_k)) > abs(f(x_k_pre)):
            x_k = x_k_pre - lamd_k * s
            lamd_k = lamd_k / 2.0
            i = i + 1
            #print i, lamd_k
        k = k + 1
        print "iteration: %d\n" \
              "lamd_%d: %.10f\n" \
              "x_%d: %.10f\n" \
              % (k, k, lamd_k, k, x_k)
    print f1(x_k)
    return k, x_k
#print f1_p(2), " " , f1_p(1)," ",f1_p(3)

def test_newton(f, f_p, step, accuracy=0):
    lamd0_list = list()
    k_list = list()
    lamd_0 = step
    x_list = list()
    while lamd_0 < 1.0:
        lamd0_list.append(lamd_0)
        k, x_k = newton_method(f, f_p,
                               np.array(1.2, dtype=np.float64),
                               0.001,
                               0.001,
                               #np.finfo(np.float64).eps,
                               #np.finfo(np.float64).eps,
                               lamd_0)
        k_list.append(k)
        x_list.append(x_k)
        lamd_0 += step
    print lamd0_list
    print k_list
    print x_list
# newton_method(f1,f1_p,
#               np.array(0.6,dtype=np.float64),
#               np.finfo(np.float64).eps,
#               np.finfo(np.float64).eps,
#               1.0)

if __name__ == '__main__':
    #test_newton(f=f1, f_p=f1_p, step=0.1, )

    test_newton(f=f2, f_p=f2_p, step=0.1, )