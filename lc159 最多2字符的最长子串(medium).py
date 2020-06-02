# 参考资料 https://www.cnblogs.com/grandyang/p/5185561.html
# 自己的写法solve3同方法四
# solve4同方法一
from common_file import random_char_list


class Solution(object):

    # 遍历
    def solve(self, chars):
        max_length = 0
        for i in range(len(chars)-1):
            char_list = [chars[i], chars[i+1]]
            this_max_length = 1
            for j in range(i+1, len(chars)):
                if chars[j] in char_list:
                    this_max_length += 1
                else:
                    break
            max_length = max(max_length, this_max_length)
        return max_length

    # 连续同字符出错 无法使用
    def solve2(self, chars):
        max_length = 0
        tmp_max_length = 2
        for i in range(2, len(chars)):
            if i == 5:
                pass
            char_list = [chars[i-2], chars[i-1]]
            if chars[i] in char_list:
                tmp_max_length += 1
            else:
                tmp_max_length = 2
            max_length = max(max_length, tmp_max_length)
            print(i, chars[i], max_length)
        return max_length

    # 只能解2个字符 自己写的
    def solve3(self, chars):

        tmp_max_length = 0
        max_length = 0
        char_length_dict = {}
        for i in range(len(chars)):
            char = chars[i]
            if char in char_length_dict:
                if i > 0 and char == chars[i-1]:
                    char_length_dict[char] += 1
                tmp_max_length += 1
                max_length = max(max_length, tmp_max_length)
            else:
                if i > 0:
                    char_length_dict = {chars[i-1]: char_length_dict[chars[i-1]]}
                char_length_dict[char] = 1
                tmp_max_length = sum([char_length_dict[key] for key in char_length_dict.keys()])

        return max_length

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
