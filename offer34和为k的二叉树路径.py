from 二叉树遍历todo import tree1


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        if not root:
            return []

        result = []

        def FindPathCore(root, path, currentNum):
            currentNum += root.val
            path.append(root)
            # 判断是否达到叶子节点
            flag = (root.left == None and root.right == None)

            # 如果到达叶子节点且当前值等于期望值
            if currentNum == expectNumber and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)

            if currentNum < expectNumber:
                if root.left:
                    FindPathCore(root.left, path, currentNum)
                if root.right:
                    FindPathCore(root.right, path, currentNum)
            path.pop()

        FindPathCore(root, [], 0)
        return result


s = Solution()

result = s.FindPath(tree1, 10)
print(result)
