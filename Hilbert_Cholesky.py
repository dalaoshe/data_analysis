import numpy as np

def create_H(dimession):
    H = np.ones([dimession,dimession],dtype=np.float64)
    for i in range(1,dimession+1):
        for j in range(1,dimession+1):
            H[i-1][j-1] = 1.0 / float(i+j-1)

    return H


def Cholesky_L(H, dimession):
    for j in range(dimession):
        for k in range(j):
            H[j][j] = H[j][j] - (H[j][k]**2)
        H[j][j] = np.sqrt(H[j][j])
        #print H[j][j]
        for i in range(j+1, dimession):
            for k in range(j):
                H[i][j] = H[i][j] - H[i][k] * H[j][k]
            H[i][j] = H[i][j] / H[j][j]
    L = np.zeros([dimession,dimession],dtype=np.float64)
    for i in range(dimession):
        for j in range(i+1):
            L[i][j] = H[i][j]

    for i in range(dimession):
        for j in range(i+1, dimession):
            H[i][j] = H[j][i]
    return H,L


def aft_generation(L, b , dimession):
    x = np.zeros([dimession],dtype=np.float64)
    for i in range(dimession):
        k = i
        i = dimession-1-i
        x[i] = b[i]
        for j in range(k):
            j = dimession-1-j
            x[i] = x[i] - L[i][j] * x[j]
        x[i] = x[i] / L[i][i]
    return x


def pre_generation(L, b, dimession):
    x = np.zeros([dimession],dtype=np.float64)
    for i in range(dimession):
        x[i] = b[i]
        for j in range(i):
            x[i] = x[i] - L[i][j]*x[j]
        x[i] = x[i] / L[i][i]
    return x


def figure_x(A, b, dimession):
    H, L = Cholesky_L(A, dimession)
    L_t = np.transpose(L)
    y = pre_generation(L, b, dimession)
    x = aft_generation(L_t, y, dimession)


    return x


def do_experiment(dimession, eps):
    H = create_H(dimession)
    s_1 = np.max(abs(np.sum(H,1)))
    H_I = np.mat(H).I
    s_2 = np.max(abs(np.sum(H_I,1)))

    x_f = np.ones([dimession], dtype=np.float64)
    b = H.dot(x_f)

    b_eps = b + eps
    x_L = figure_x(H, b_eps, dimession)
    b_L = H.dot(x_L)

    r_b = b - b_L
    r_x = x_f - x_L
    print "cond(H)=", s_1 * s_2, " ||H||=", s_1, " ||H-1||=", s_2
    print "r_b:",r_b, "\nr_b_00:",np.max(abs(r_b))
    print "r_x:",r_x, "\nr_x_00:",np.max(abs(r_x))
    print ""

if __name__ == '__main__':
    do_experiment(10, 0.0)


    do_experiment(10, 10e-7)
    do_experiment(8,0.0)
    do_experiment(12,0.0)