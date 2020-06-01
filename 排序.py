# 十大常见排序算法的python3实现
# 其中9和10有适用范围限制，所有也有8大排序的说法
# 参考了两篇文档：
# https://www.cnblogs.com/onepixel/articles/7674659.html
# https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg
# 代码为了方便，每一种算法内都重建了一份待排序的列表（raw_list -> tmp_list），避免直接修改原列表

from common_file import random_number_list, random_positive_int_list
import math


class Solution(object):

    # 1. 冒泡排序
    def bubblesort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)
        for i in range(length-1):
            for j in range(length-i-1):
                if tmp_list[j] > tmp_list[j+1]:
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
                    # temp = tmp_list[j]
                    # tmp_list[j] = tmp_list[j+1]
                    # tmp_list[j+1] = temp
        return tmp_list

    # 2. 选择排序
    def selectionsort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)
        for i in range(length-1):
            min_index = i
            for j in range(i+1, length):
                if tmp_list[j] < tmp_list[min_index]:
                    min_index = j
            tmp_list[min_index], tmp_list[i] = tmp_list[i], tmp_list[min_index]
        return tmp_list

    # 3. 插入排序
    def insertionsort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)
        for i in range(1, length):
            cur_num = tmp_list[i]
            pre_index = i - 1
            while pre_index > -1 and tmp_list[pre_index] > cur_num:
                tmp_list[pre_index+1] = tmp_list[pre_index]
                pre_index = pre_index - 1
            tmp_list[pre_index+1] = cur_num
        return tmp_list

    # 4. 希尔排序
    def shellsort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)
        gap = length

        # 方案2 自己写的 高度借鉴上面的插入排序 感觉更好理解点
        while gap > 0:
            gap = gap//2
            for i in range(gap):
                for j in range(i, length, gap):
                    cur_num = tmp_list[j]
                    pre_index = j - gap
                    while pre_index > -1 and tmp_list[pre_index] > cur_num:
                        tmp_list[pre_index + gap] = tmp_list[pre_index]
                        pre_index -= gap
                    tmp_list[pre_index + gap] = cur_num

        # 方案1 网上找的
        # gap = gap // 2
        # while gap >= 1:
        #     for j in range(gap, length):
        #         i = j
        #         while (i - gap) >= 0:
        #             if tmp_list[i] < tmp_list[i - gap]:
        #                 tmp_list[i], tmp_list[i - gap] = tmp_list[i - gap], tmp_list[i]
        #                 i -= gap
        #             else:
        #                 break
        #     gap //= 2

        return tmp_list

    # 5. 归并排序 to do
    def mergesort(self, raw_list):
        tmp_list = [element for element in raw_list]

        def merge(arr_left, arr_right):
            result = []
            while len(arr_left) > 0 and len(arr_right) > 0:
                if arr_left[0] <= arr_right[0]:
                    result.append(arr_left[0])
                    del arr_left[0]
                else:
                    result.append(arr_right[0])
                    del arr_right[0]
            result += arr_left + arr_right
            return result

        def __mergesort__(arr):
            if len(arr) < 2:
                return arr
            middle = len(arr) // 2
            arr_left = arr[0: middle]
            arr_right = arr[middle:]
            rst = merge(__mergesort__(arr_left), __mergesort__(arr_right))
            return rst

        rst = __mergesort__(tmp_list)
        return rst

    # 6. 快速排序
    def quicksort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)

        # arr[] --> 排序数组
        # low  --> 起始索引
        # high  --> 结束索引
        def partition(arr, low, high):
            i = (low-1)         # 最小元素索引
            pivot = arr[high]
            for j in range(low, high):
                # 当前元素小于或等于 pivot
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)

        # 快速排序函数
        def __quick_sort__(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                __quick_sort__(arr, low, pi-1)
                __quick_sort__(arr, pi+1, high)

        __quick_sort__(tmp_list, 0, length-1)

        return tmp_list

    # 7. 堆排序
    # 二叉树遍历的问题，没看懂是什么遍历方式
    def heapsort(self, raw_list):
        tmp_list = [element for element in raw_list]
        length = len(raw_list)

        def buildMaxHeap(arr, length):
            for i in range(math.floor(length/2), 0, -1):
                heapify(arr, i, length)
            return

        def heapify(arr, i, length):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < length and arr[left] > arr[largest]:
                largest = left
            if right < length and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, largest, length)
            return

        buildMaxHeap(tmp_list, length)
        for i in range(length-1, 0, -1):
            tmp_list[0], tmp_list[i] = tmp_list[i], tmp_list[0]
            length -= 1
            heapify(tmp_list, 0, length)

        return tmp_list

    # 8. 计数排序
    def countingsort(self, raw_list):

        # 方案1 代码简单 复杂度似乎高
        length = len(raw_list)
        tmp_list = [None] * length
        for i in range(length):
            p = 0
            q = 0
            for j in range(length):
                if raw_list[i] > raw_list[j]:
                    p += 1
                elif raw_list[i] == raw_list[j]:
                    q += 1
            for k in range(p, p+q):  # q表示 相等的次数,就表示, 从 P 开始索引后, 连续 q 次,都是同样的 数
                tmp_list[k] = raw_list[i]

        # 方案2 不靠谱 只能算整数
        # def get_max_value(arr):
        #     max_value = arr[0]
        #     for i in arr:
        #         if i > max_value:
        #             max_value = i
        #     return max_value

        return tmp_list

    # 9. 桶排序
    # 迭代了插入排序，对小于1的数字来说就是插入排序，桶数量是1， buckets注意不要形成浅拷贝
    def bucketsort(self, raw_list):
        # 超参
        bucket_size = 5

        if len(raw_list) == 0:
            return raw_list
        min_value = raw_list[0]
        max_value = raw_list[0]
        for value in raw_list:
            if value < min_value:
                min_value = value
            elif value > max_value:
                max_value = value

        bucket_count = int(math.floor(max_value-min_value) / bucket_size) + 1
        buckets = [[] for count in range(bucket_count)]

        for i in range(len(raw_list)):
            index = int(math.floor(raw_list[i] - min_value) / bucket_size)
            buckets[index].append(raw_list[i])

        result = []
        for sub_raw_list in buckets:
            sub_raw_list = self.insertionsort(sub_raw_list)
            result += sub_raw_list

        return result

    # 10. 基数排序
    # 按位排序 只适合正整数
    def radixsort(self, raw_list):

        def get_num_length(positive_int):
            if positive_int == 0:
                return 1
            length = 1
            while positive_int // 10 != 0:
                positive_int = math.floor(positive_int // 10)
                length += 1
            return length

        def get_max_value(arr):
            max_value = arr[0]
            for i in range(len(arr)):
                if arr[i] > max_value:
                    max_value = arr[i]
            return max_value

        def get_max_num_length(arr):
            max_value = get_max_value(arr)
            max_num_length = get_num_length(max_value)
            return(max_num_length)

        tmp_list = [element for element in raw_list]
        max_num_length = get_max_num_length(tmp_list)
        mod = 10  # 除以10取余数
        dev = 1  # 余数再取整用

        for i in range(max_num_length):
            counter = [[] for count in range(10)]
            for j in range(len(tmp_list)):
                bucket = int(tmp_list[j] % mod / dev)
                counter[bucket].append(tmp_list[j])
            position = 0
            for count in counter:
                for num in count:
                    tmp_list[position] = num
                    position += 1
            mod *= 10
            dev *= 10
        return tmp_list


s = Solution()

# from common_file import random_float_list
# random_number_list = random_float_list

print('------------This is raw list-------------')
print(random_number_list)
print()

# print('---------Bubble Sort (1,冒泡排序)-----------')
# result = s.bubblesort(random_number_list)
# print(result)
# print()

# print('-------Selection Sort (2,选择排序) ---------')
# result = s.selectionsort(random_number_list)
# print(result)
# print()

# print('-------Insertion Sort (3,插入排序) ---------')
# result = s.insertionsort(random_number_list)
# print(result)
# print()

# print('---------Shell Sort (4,希尔排序) -----------')
# result = s.shellsort(random_number_list)
# print(result)
# print()

# print('---------Merge Sort (5,归并排序) -----------')
# result = s.mergesort(random_number_list)
# print(result)
# print()

# print('---------Quick Sort (6,快速排序) -----------')
# result = s.quicksort(random_number_list)
# print(result)
# print()

print('---------Quick Sort (7,堆排序) -----------')
result = s.heapsort(random_number_list)
print(result)
print()

print('---------Counting Sort (8,计数排序) -----------')
result = s.countingsort(random_number_list)
print(result)
print()

print('---------Bucket Sort (9,桶排序) -----------')
result = s.bucketsort(random_number_list)
print(result)
print()

print('---------Radix Sort (10,基数排序) -----------')
result = s.radixsort(random_positive_int_list)
print(result)
print()

# 计时
# from timeit import Timer
# def test():
#     s.countingsort(random_number_list)

# name = test.__name__
# t = Timer(name+'()','from __main__ import '+name)
# print(t.timeit(1))
