import numpy as np
import time
print np.finfo(np.float32)

print np.finfo(np.float64)

print np.finfo(np.float32).epsneg


def can_stop_theory(n, sums, type, count):
    tow_const = np.array([2],dtype=type)
    ratio = (tow_const * n) / sums
    if ratio < np.finfo(type).epsneg:
        return True
    return False


def not_change(last, now, type):
    if now - last < np.finfo(type).eps:
        # print "last:", last
        # print "now :", now
        return True
    return False

def figure_infinite_series(type, max_count=3097155):
    n = np.array([1],dtype=type)
    one_constant = np.array([1],dtype=type)
    sum_result = np.array([0],dtype=type)
    theory_count = 1
    figure_count = 1
    count = 1
    stop = False
    s_time = time.clock()
    while True and count < max_count:
        sum_last = np.copy(sum_result)
        sum_result += one_constant / n
        n = n + one_constant
        stop = True
        if not can_stop_theory(one_constant / n, sum_result, type, theory_count):
            theory_count += 1
            stop = False
        if not not_change(last=sum_last, now=sum_result, type=type):
            figure_count += 1
            stop = False
        # else:
        #     break
        if stop:
            break
        count += 1
    e_time = time.clock()
    return sum_result, theory_count, figure_count, (e_time-s_time)

sum_32,t_count_32,f_count_32,u_time = figure_infinite_series(np.float32)
print "sum_32: ",sum_32, " theory_count_32 ", t_count_32, " firgure_count_32 ", f_count_32,
print "use time:%.10f" % u_time

sum_64,t_count_32,f_count_32,u_time = figure_infinite_series(np.float64,
                                                             2097152)
print "sum_64: ", sum_64, " firgure_count ", f_count_32,
print "use time:%.10f" % u_time

err_64_32 = (sum_32-sum_64)
err_64_32_R = (sum_32-sum_64) / sum_64
print "e: %.10f, e_r: %.10f" % (err_64_32, err_64_32_R)

t_n = u_time / f_count_32
years = ((5e14 / f_count_32)* u_time) / (60.0*60.0*24.0*365.0)
print "float64 need %d years" % years