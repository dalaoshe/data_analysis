import numpy as np



def f1(x):
    return x**3-x-1.0
def f1_p(x):
    return 3.0*(x**2)-1.0



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
            print i, lamd_k
        k = k + 1
        print "iteration: [k,lamd,x_k,f(x),s] [%d,%.60f,%.60f,%.60f,%.60f]" %(k,lamd_k ,x_k,f(x_k),s)

    print f1(x_k)

print f1_p(2), " " , f1_p(1)," ",f1_p(3)

newton_method(f1,f1_p,np.array(0.6,dtype=np.float64),np.finfo(np.float64).eps,np.finfo(np.float64).eps,1.0)