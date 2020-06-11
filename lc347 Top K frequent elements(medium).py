from common_file import random_number_list


class Solution(object):
    def solve(self, nums, k):
        num_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        result = []
        buckets = [[] for count in range(len(nums))]
        for num in num_dict:
            buckets[num_dict[num]].append(num)

        for i in range(len(buckets))[::-1]:
            if len(result) < k:
                result += buckets[i]

        return result


s = Solution()
result = s.solve(random_number_list, 2)
print(random_number_list)
print(result)
