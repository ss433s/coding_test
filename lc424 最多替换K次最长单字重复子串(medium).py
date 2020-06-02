# 参考资料 https://www.cnblogs.com/grandyang/p/5999050.html
from common_file import random_char_list


class Solution(object):

    # 遍历 依然需要判断最多次数字符及其次数
    def solve(self, chars, k):
        max_length = 0

        def get_max_count_char(chars):
            max_length = 0
            max_char = ''
            char_length_dict = {}
            for char in chars:
                if char in char_length_dict:
                    char_length_dict[char] += 1
                else:
                    char_length_dict[char] = 1

                if char_length_dict[char] > max_length:
                    max_length = char_length_dict[char]
                    max_char = char

            return max_char, char_length_dict[char]

        if len(chars) <= k:
            return len(chars)

        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                sub_chars = chars[i:j+1]
                _, max_char_count = get_max_count_char(sub_chars)
                if max_char_count + k >= len(sub_chars):
                    if len(sub_chars) > max_length:
                        max_length = len(sub_chars)
        return max_length

    # 递归 以后再试 todo
    def solve2(self, chars, k):

        def get_max_count_char(chars):
            max_length = 0
            max_char = ''
            char_length_dict = {}
            for char in chars:
                if char in char_length_dict:
                    char_length_dict[char] += 1
                else:
                    char_length_dict[char] = 1

                if char_length_dict[char] > max_length:
                    max_length = char_length_dict[char]
                    max_char = char

            return max_char

        a = get_max_count_char(chars)
        print(a)

        max_length = 0
        left = 0
        char_length_dict = {}
        for right in range(1, len(chars)):
            if chars[right] in char_length_dict:
                char_length_dict[chars[right]] += 1
            else:
                char_length_dict[chars[right]] = 1

            while len(char_length_dict) + k < right-left:
                left += 1
                char_length_dict[chars[right]] -= 1
                if char_length_dict[chars[right]] == 0:
                    char_length_dict.pop(chars[right])

            char = chars[right]  # 当前字符
            this_k = k  # 本轮的K
            this_max_length = 1  # 本轮最大长度
            for j in range(right+1, len(chars)):
                if chars[j] == char:
                    this_max_length += 1
                else:
                    if this_k > 0:
                        this_max_length += 1
                        this_k -= 1
            max_length = max(max_length, this_max_length)

        return max_length

    # 滑动窗口 不每次更新max_char_count是否ok？
    def solve3(self, chars, k):
        max_length = 0
        start = 0
        char_dict = {}

        def get_max_char(char_dict):
            max_char = ''
            max_char_count = 0
            for char in char_dict:
                if char_dict[char] > max_char_count:
                    max_char = char
                    max_char_count = char_dict[char]
            return max_char, max_char_count

        for end in range(len(chars)):
            if chars[end] in char_dict:
                char_dict[chars[end]] += 1
            else:
                char_dict[chars[end]] = 1
            _, max_char_count = get_max_char(char_dict)
            while end-start+1-max_char_count > k:
                char_dict[chars[start]] -= 1
                start += 1
            # print(max_length, start, end)
            max_length = max(max_length, end-start+1)

        return max_length


s = Solution()
# random_char_list = 'ababab'
k = 2
print(random_char_list)
result = s.solve3(random_char_list, k)
print(result)
