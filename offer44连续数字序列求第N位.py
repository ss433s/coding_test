asked_number = 1000000000

import time

print(time.time())
start_number = 0
number_count = 0
while number_count < asked_number:
    start_number += 1
    number_count += len(str(start_number))

print(start_number, number_count)

result = str(start_number)[asked_number-number_count-1]
print(result)
print(time.time())

import math

number_length = 1
number_count = 0
while number_count < asked_number:
    if number_length == 1:
        this_length_count = 10
    else:
        this_length_count = math.pow(10, number_length) - math.pow(10, number_length-1)
    last_length_count = number_count
    number_count += this_length_count * number_length
    # print(number_length, this_length_count, number_count)
    number_length += 1

# 需要注意1位数时候的特殊处理
print(number_length, number_count, last_length_count)
this_num = int((asked_number - last_length_count) // (number_length - 1) + math.pow(10, number_length - 2))
this_num_site = int((asked_number - last_length_count) % (number_length - 1))
print(this_num, this_num_site)
result = str(this_num)[this_num_site]
print(result)
print(time.time())
