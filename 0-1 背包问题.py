# 01背包问题


# Returns the maximum value that
# can be put in a knapsack of Total_capacity
def knapSack(Total_capacity, weight_list, value_list, n):

    # Base Case
    if n == 0 or Total_capacity == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity Total_capacity,
    # then this item cannot be included
    # in the optimal solution
    if (weight_list[n - 1] > Total_capacity):
        return knapSack(Total_capacity, weight_list, value_list, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            value_list[n - 1] + knapSack(Total_capacity - weight_list[n - 1],
                                         weight_list, value_list, n - 1),
            knapSack(Total_capacity, weight_list, value_list, n - 1))


# 好复杂，不是很懂，空间效率太低
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
# We initialize the matrix with -1 at first.
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]


# 注意区分函数名大小写
def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n - 1] <= W:
        t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
                      knapsack(wt, val, W, n - 1))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = knapsack(wt, val, W, n - 1)
        return t[n][W]


print(knapsack(wt, val, W, n))

value_list = [60, 100, 120]
weight_list = [10, 60, 20]
Total_capacity = 50
n = len(value_list)
print(knapSack(Total_capacity, weight_list, value_list, n))
