class Solution:

    # 动态规划
    def solve(self, length):

        # 特殊处理的
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        # 后续序列 小于4的一刀不切最大
        products = {}
        # products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, length+1):
            max_product = 0
            for j in range(1, i//2+1):
                this_product = products[j] * products[i-j]
                if this_product > max_product:
                    max_product = this_product
                    products[i] = max_product
        return products[length]

    def solve2(self, length):

        # 特殊处理的
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        timesOf3 = length//3
        if length - timesOf3*3 == 1:
            timesOf3 -= 1

        timesOf2 = (length - timesOf3 * 3)//2
        return (3**timesOf3) * (2**timesOf2)


s = Solution()
result = s.solve2(8)
print(result)
