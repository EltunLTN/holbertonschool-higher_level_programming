#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    count = 0
    for i in range(len(my_list)):
        sum += my_list[i][0] * my_list[i][1]
        count += my_list[i][1]
    return sum / count
