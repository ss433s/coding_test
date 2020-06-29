class Solution:

    # 官方答案
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows < 0 or cols < 0 or path == None:
            return False
        markmatrix = [0] * (rows * cols)
        pathIndex = 0

        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path,
                                    pathIndex, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathIndex,
                    markmatrix):
        if pathIndex == len(path):
            return True
        hasPath = False
        if row >= 0 and \
           row < rows and \
           col >= 0 and \
           col < cols and \
           matrix[row * cols + col] == path[pathIndex] and \
           not markmatrix[row * cols + col]:

            pathIndex += 1
            markmatrix[row * cols + col] = True
            hasPath = self.hasPathCore(matrix, rows, cols, row+1, col, path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row-1, col, path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row, col+1, path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row, col-1, path, pathIndex, markmatrix)
            if not hasPath:
                pathIndex -= 1
                markmatrix[row * cols + col] = False
        return hasPath

    # 遍历试试
    def hasPath2(self, matrix, rows, cols, path):

        def check_next(self, matrix, rows, cols, cur_row, cur_col, pathIndex):
            this_match_sites = []
            if path[pathIndex] == matrix[cur_row*cur_col + cur_col + 1]:
                this_match_sites.append(cur_row*cur_col + cur_col + 1)
            if path[pathIndex] == matrix[(cur_row+1)*cur_col + cur_col]:
                this_match_sites.append((cur_row+1)*cur_col + cur_col)
            if path[pathIndex] == matrix[(cur_row+1)*cur_col + cur_col + 1]:
                this_match_sites.append((cur_row+1)*cur_col + cur_col + 1)
            return this_match_sites

        hasPath = False
        match_sites = []
        for i in range(len(matrix)):
            char = matrix[i]
            if char == path[0]:
                cur_row = i // cols
                cur_col = i - cur_row * cols
                match_sites = [[i]]
                #for index in range(1, len(path)-1):

                return hasPath




        return


matrix = [
    ['a', 'b', 't', 'g'],
    ['c', 'f', 'c', 's'],
    ['j', 'd', 'e', 'h']
]
matrix_list = []
for i in matrix:
    matrix_list += i

s = Solution()
result = s.hasPath2(matrix_list, 3, 4, 'bfce')
print(result)
