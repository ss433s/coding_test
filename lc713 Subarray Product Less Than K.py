# 参考资料 https://blog.csdn.net/fuxuemingzhu/article/details/83047699
# https://www.cnblogs.com/grandyang/p/7753959.html
from common_file import random_positive_int_list


class Solution(object):

    # 暴力
    def solve(self, int_list, k):
        count = 0
        for i in range(len(int_list)):
            cur_product = int_list[i]
            if cur_product < k:
                count += 1
            for j in range(i+1, len(int_list)):
                cur_product *= int_list[j]
                if cur_product < k:
                    count += 1
        return count

    # 双指针
    def solve2(self, int_list, k):
        count = 0
        if k <= 1:
            return count

        cur_product = 1
        left = 0
        for right in range(len(int_list)):
            cur_product *= int_list[right]
            while left <= right and cur_product >= k:
                cur_product /= int_list[left]
                left += 1
            count += right-left+1

        return count


s = Solution()
random_int_list = [10, 5, 2, 6]
k = 100
print(random_int_list)
result = s.solve2(random_int_list, k)
print(result)
