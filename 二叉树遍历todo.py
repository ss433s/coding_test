# 四种遍历方式 参考资料https://www.cnblogs.com/lliuye/p/9143676.html
from common_file import TreeNode


class OperationTree:
    '''二叉树操作'''
    def create(self, List):
        '''二叉搜索树插入操作'''
        root = TreeNode(List[0])
        lens = len(List)
        if lens >= 2:
            root.left = self.create(List[1])
        if lens >= 3:
            root.right = self.create(List[2])
        return root

    def query(self, root, data):
        '''二叉树查找操作'''
        if root is None:
            return False
        elif not isinstance(root, TreeNode):
            return 'Not tree'

        if root.val == data:
            return True
        else:
            return any([self.query(root.left, data), self.query(root.right, data)])

    def PreOrder(self, root):
        '''打印二叉树(先序)'''
        if root == None:
            return
        print(root.val, end=' ')
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self, root):
        '''中序打印'''
        if root == None:
            return
        self.InOrder(root.left)
        print(root.val, end=' ')
        self.InOrder(root.right)

    def BacOrder(self, root):
        '''后序打印'''
        if root == None:
            return
        self.BacOrder(root.left)
        self.BacOrder(root.right)
        print(root.val, end=' ')


List1 = [1, [2, [4, [8], [9]], [5]], [3, [6], [7]]]
op = OperationTree()
tree1 = op.create(List1)
query_result = op.query('123', 7)
# op.InOrder(tree1)
