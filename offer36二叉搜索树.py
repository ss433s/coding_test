# from common_file import TreeNode
from 二叉树遍历todo import OperationTree


class Solution:

    def get_right(self, node):
        if node.right:
            return self.get_right(node.right)
        else:
            return node

    def get_left(self, node):
        if node.left:
            return self.get_left(node.left)
        else:
            return node

    def tree2node_core(self, node):

        if node.left is None and node.right is None:
            return
        if node.left:
            most_right = self.get_right(node.left)
            self.tree2node_core(node.left)
            most_right.right = node
            node.left = most_right
        if node.right:
            most_left = self.get_left(node.right)
            self.tree2node_core(node.right)
            most_left.left = node
            node.right = most_left

    def tree2node(self, root):

        if not root:
            return

        pHead = self.get_left(root)
        self.tree2node_core(root)
        return pHead

    # 网上找到的写法
    # def Core(self, root):
    #     if not root.left and not root.right:
    #         return
    #     if root.left:
    #         preRoot = root.left
    #         self.Core(root.left)
    #         while preRoot.right:
    #             preRoot = preRoot.right
    #         preRoot.right = root
    #         root.left = preRoot
    #     if root.right:
    #         nextRoot = root.right
    #         self.Core(root.right)
    #         while nextRoot.left:
    #             nextRoot = nextRoot.left
    #         nextRoot.left = root
    #         root.right = nextRoot


List1 = [10, [6, [4], [8]], [14, [12], [18]]]
op = OperationTree()
tree1 = op.create(List1)

s = Solution()

result = s.tree2node(tree1)
print(result)
