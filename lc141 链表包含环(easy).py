# 参考资料 https://www.cnblogs.com/hiddenfox/p/3408931.html
# 重点是要算出来a=c
from common_file import random_char_list


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pfast, pslow = head, head
        while(pfast != None and pfast.next != None):
            pslow = pslow.next
            pfast = pfast.next.next
            if pslow == pfast:
                return True
        return False


s = Solution()
# random_char_list = 'ababab'
k = 2
print(random_char_list)
result = s.solve3(random_char_list, k)
print(result)
