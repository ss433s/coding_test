# n进制转k进制
n = 10
k = 16
number = 378172

import math

current_sys = n
target_sys = k

target_list = []
number_str = str(number)

# 先转10进制
if current_sys != 10:
    ten_sys_number = 0

    length = len(number_str)
    for i in range(length):
        ten_sys_number += int(int(number_str[length-1-i]) * math.pow(current_sys, i))
else:
    ten_sys_number = number

# 再转数组
site = 1
while True:
    mod = ten_sys_number % target_sys
    ten_sys_number = int((ten_sys_number - mod) / target_sys)
    site += 1
    # print(mod)
    # print(site)
    # print(ten_sys_number)
    # print('-----------')
    target_list.append(mod)
    if ten_sys_number // target_sys == 0:
        target_list.append(ten_sys_number)
        break

target_list = target_list[::-1]
print(target_list)
