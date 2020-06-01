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

    # 连续同字符出错
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

    def solve3(self, chars):
        max_length = 0
        char_length_dict = {}
        for i in range(len(chars)):
            char = chars[i]
            if char in char_length_dict:
                if char == chars[i-1]:
                    char_length_dict[char] += 1
                max_length += 1
            else:
                char_length_dict[char] = 1
                max_length = max(max_length, sum([char_length_dict[key] for key in char_length_dict.keys()]))
                if i > 0:
                    char_length_dict = {chars[i-1]: char_length_dict[chars[i-1]]}
                char_length_dict[char] = 1

        return max_length


s = Solution()
random_char_list = 'baece'
print(random_char_list)
result = s.solve3(random_char_list)
print(result)
