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

def figure_infinite_series(type, max_count=2097155):
    n = np.array([1],dtype=type)
    one_constant = np.array([1],dtype=type)
    sum_result = np.array([0],dtype=type)
    theory_count = 1
    figure_count = 1
    count = 1
    stop = False
    s_time = time.clock()
    while True and count < max_count:
        sum_last = np.array(sum_result, dtype=type)
        sum_result += one_constant / n
        n = n + one_constant
        # if figure_count > 2097120:
        #     print figure_count, " ",sum_result
      #  print sum_result
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
print sum_32, " theory_count ", t_count_32, " firgure_count ", f_count_32,
print "use time:%.10f" % u_time

sum_32,t_count_32,f_count_32,u_time = figure_infinite_series(np.float64,
                                                             2097152)
print sum_32, " theory_count ", t_count_32, " firgure_count ", f_count_32,
print "use time:%.10f" % u_time