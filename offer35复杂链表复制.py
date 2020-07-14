class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def __init__(self):
        self.cloned_node_id_list = []

    # 网传的递归解法 random指向原节点 根本不是复制
    # 直接递归无法复制有环的链表
    # 尝试自己写一个失败，递归无法解决random和next指向同一节点的问题

    def Clone2(self, pHead):
        if pHead is None:
            return None
        if id(pHead) in self.cloned_node_id_list:
            return pHead
        new_head = RandomListNode(pHead.label)  # 新建一个链表的头结点
        self.cloned_node_id_list.append(id(pHead))
        new_head.random = self.Clone2(pHead.random)
        # new_head.next = pHead.next  令头结点的next等于原来头结点的next;
        # 直接让new_head.next等于递归后的pHead.next)
        new_head.next = self.Clone2(pHead.next)  # 递归处理new_head.next
        return new_head

    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return None

        # 为每一个结点复制一个node，并插入到原链表中
        pTemp = pHead
        while pTemp:
            node = RandomListNode(pTemp.label)
            node.next = pTemp.next
            pTemp.next = node
            pTemp = node.next

        # 实现新建node的random指向
        pTemp = pHead
        while pTemp:
            if pTemp.random:  # 如果random指针存在
                pTemp.next.random = pTemp.random.next
            pTemp = pTemp.next.next

        # 断开 原来node 和新 node 间 的链接
        pTemp = pHead
        newHead = pHead.next  # 这个是新链表的头，到最后返回，一般要保留
        pNewTemp = pHead.next  # 再新建一个中间变量来存储新的node
        while pTemp:
            pTemp.next = pTemp.next.next  # 改变前一个node的指向，让它不要指向新建的node
            if pNewTemp.next:
                pNewTemp.next = pNewTemp.next.next
                pNewTemp = pNewTemp.next
            pTemp = pTemp.next
        return newHead


n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n5 = RandomListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.random = n3
n2.random = n1
n3.random = n3


raw = n1
print(id(raw), id(n1))
print('-------raw------')
while raw:
    next_value = raw.next.label if raw.next else 'none'
    random_value = raw.random.label if raw.random else 'none'
    random_id = id(raw.random) if raw.random else 'none'
    print(raw.label, next_value, random_value, id(raw), random_id)
    raw = raw.next


s = Solution()
new_head = s.Clone2(n1)
res = new_head
print('------clone-----')
while res:
    next_value = res.next.label if res.next else 'none'
    random_value = res.random.label if res.random else 'none'
    random_id = id(res.random) if res.random else 'none'
    print(res.label, next_value, random_value, id(res), random_id)
    res = res.next
