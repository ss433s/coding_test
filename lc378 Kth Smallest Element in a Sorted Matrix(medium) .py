matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 3


class Solution(object):
    def solve(self, matrix, k):
        left = matrix[0][0]
        right = matrix[len(matrix)-1][len(matrix[0])-1]
        while left < right:
            mid = int(left + (right - left) / 2)
            cnt = 0
            for i in range(len(matrix)):
                tmp_cnt = len(matrix[i])
                for j in range(len(matrix[i])):
                    if matrix[i][j] > mid:
                        tmp_cnt = j
                        break
                cnt += tmp_cnt
            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left


s = Solution()
result = s.solve(matrix, k)
print(result)
