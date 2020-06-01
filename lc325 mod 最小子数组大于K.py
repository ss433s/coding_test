# 搜到一份答案用双指针移动做的，不支持负数序列 todo
from common_file import random_number_list


class Solution(object):
    def smallestSubWithSum(self, arr, x):

        # Initialize current sum and minimum length
        curr_sum = 0
        n = len(arr)
        min_len = len(arr)

        # Initialize starting and ending indexes
        start = 0
        end = 0
        while (end < n):

            # Keep adding array elements while current
            # sum is smaller than x
            while (curr_sum <= x and end < n):
                curr_sum += arr[end]
                end += 1

            # If current sum becomes greater than x.
            while (curr_sum > x and start < n):

                # Update minimum length if needed
                if (end - start < min_len):
                    min_len = end - start

                # remove starting elements
                curr_sum -= arr[start]
                start += 1

        return min_len


s = Solution()
print(random_number_list)
result = s.smallestSubWithSum(random_number_list, 10)
print(result)
