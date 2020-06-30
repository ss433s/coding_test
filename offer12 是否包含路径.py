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

        def check_next(matrix, rows, cols, cur_row, cur_col, pathIndex):
            this_match_sites = []
            if path[pathIndex] == matrix[cur_row*cols + cur_col + 1]:
                this_match_sites.append(cur_row*cols + cur_col + 1)
            if path[pathIndex] == matrix[(cur_row+1)*cols + cur_col]:
                this_match_sites.append((cur_row+1)*cols + cur_col)
            if path[pathIndex] == matrix[(cur_row+1)*cols + cur_col + 1]:
                this_match_sites.append((cur_row+1)*cols + cur_col + 1)
            return this_match_sites

        hasPath = False
        match_sites = []
        for i in range(len(matrix)):
            char = matrix[i]
            if char == path[0]:
                this_has_path = False
                match_sites = [[i]]
                for index in range(1, len(path)):
                    this_match_sites = []
                    for last_site in match_sites[index-1]:
                        cur_row = last_site // cols
                        cur_col = last_site - cur_row * cols
                        this_match_sites += check_next(matrix, rows, cols, cur_row, cur_col, index)
                    if this_match_sites == []:
                        break
                    else:
                        match_sites.append(this_match_sites)
                        if index == len(path)-1:
                            this_has_path = True
                if this_has_path:
                    return this_has_path

        return hasPath


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
