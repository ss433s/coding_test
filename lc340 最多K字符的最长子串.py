# 参考资料 https://www.cnblogs.com/grandyang/p/5351347.html
# https://www.cnblogs.com/grandyang/p/5185561.html
# solve4同方法一
from common_file import random_char_list


class Solution(object):

    # 解k个字符 时间复杂度为n 本质是双指针滑动窗口 right为指针1， left是指针2
    def solve4(self, chars):

        k = 3
        max_length = 0
        left = 0
        char_length_dict = {}
        for right in range(len(chars)):
            char = chars[right]
            if char in char_length_dict:
                char_length_dict[char] += 1
            else:
                char_length_dict[char] = 1

            while len(char_length_dict) > k and left < len(chars):
                if chars[left] in char_length_dict:
                    char_length_dict[chars[left]] -= 1
                    if char_length_dict[chars[left]] == 0:
                        char_length_dict.pop(chars[left])
                left += 1

            max_length = max(max_length, right-left+1)

        return max_length


s = Solution()
# random_char_list = 'baece'
print(random_char_list)
result = s.solve4(random_char_list)
print(result)
