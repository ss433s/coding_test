from common_file import random_number_list


class Solution(object):
    def maxSubArrayLength(self, nums, k):
        cur_sum = 0
        sums = {0: -1}
        max_length = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum not in sums:
                sums[cur_sum] = i
            if cur_sum - k in sums:
                max_length = max(i - sums[cur_sum - k], max_length)
        return max_length


s = Solution()
result = s.maxSubArrayLength(random_number_list, 10)
print(random_number_list)
print(result)
