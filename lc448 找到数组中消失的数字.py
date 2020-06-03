# 参考资料 官方
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。

# 输入:
# [4,3,2,7,8,2,3,1]

# 输出:
# [5,6]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):

    def solve(self, number_list):
        result = []
        num_dict = {}
        for i in number_list:
            num_dict[i] = 1
        for i in range(1, len(number_list)+1):
            if i not in num_dict:
                result.append(i)
        return result

    def solve2(self, number_list):
        for i in range(len(number_list)):
            new_index = abs(number_list[i]) - 1
            if number_list[new_index] > 0:
                number_list[new_index] *= -1

        result = []
        for i in range(1, len(number_list) + 1):
            if number_list[i - 1] > 0:
                result.append(i)

        return result

s = Solution()
test_list = [4, 3, 2, 7, 8, 2, 3, 1]
print(test_list)
result = s.solve2(test_list)
print(result)
