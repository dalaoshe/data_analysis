import numpy as np
from Hilbert_Cholesky import Cholesky_L, pre_generation, aft_generation, figure_x
import matplotlib.pyplot as plt


def read_date(file_name):
    with open(file_name, "r") as f:
        ti = [float(x) for x in f.readline().strip().split()]
        yi = [float(x) for x in f.readline().strip().split()]
    return np.array(ti, dtype=np.float64), np.array(yi, dtype=np.float64)


def t_0(ti, lens):
    return np.ones([lens], dtype=np.float64)

def t_1(ti, lens):
    return ti

def t_2(ti, lens):
    return ti * ti

ti, yi = read_date("curve_data.txt")


def get_polynomial_A(ti, lens):
    A_t = np.concatenate((t_0(ti, lens),
                    t_1(ti, lens),
                    t_2(ti, lens)))
    A_t = np.reshape(A_t,[3, lens])
    print A_t
    A = np.transpose(A_t)
    H = A_t.dot(A)
    return H, A_t

def get_exp_y(yi):
    return np.log(yi)

def get_exp_A(ti, lens):
    A_t = np.array([t_0(ti, lens),
                    t_1(ti, lens)],
                   dtype=np.float64)
    A = np.transpose(A_t)
    H = A_t.dot(A)
    return H, A_t


def exp_fitting(a, b, ti):
    y_i = a * np.exp((b*ti))
    return y_i


def polynomial_2(a, b, c, ti):
    y_i = a + b*ti + c*ti*ti
    return y_i


def fitting_polynomial(ti, yi):
    lens = np.shape(ti)[0]
    H, A_t = get_polynomial_A(ti, lens)
    dim = np.shape(H)[0]
    y_t = A_t.dot(yi)
    x = figure_x(H, y_t, dim)
    print x
    y_pred = polynomial_2(x[0],x[1],x[2],ti)
    plt.plot(ti,y_pred,"g")
    plt.scatter(ti,y_pred,marker="o")
    plt.scatter(ti,yi,edgecolors="r",marker="*")


def fitting_exp(ti, yi):
    lens = np.shape(ti)[0]
    H, A_t = get_exp_A(ti, lens)
    dim = np.shape(H)[0]
    y_t = A_t.dot(get_exp_y(yi))
    x = figure_x(H, y_t, dim)
    print x
    y_pred = exp_fitting(np.exp(x[0]), x[1], ti)
    plt.plot(ti, y_pred, "b")
    plt.scatter(ti, y_pred, marker="o")

fitting_polynomial(ti, yi)
fitting_exp(ti, yi)
plt.show()
