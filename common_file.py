random_number_list = [-6, -6, -5, 1, 10, -4, 4, -9, 3, -9, -2, -5, -6, 4, -9, -10, 7, -6, 9, -5]
random_positive_int_list = [1, 10, 18, 4, 3, 191, 4, 9, 5, 2222]
random_char_list = 'ababbadqbwbeqbeqweqasdaqwe'

import random
random_float_list = []
for i in range(20):
    # a = random.random()
    # random_float_list.append(a)
    a = random.randint(-100, 100)
    random_float_list.append(a/100)


class TreeNode:
    '''二叉搜索树节点的定义'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
