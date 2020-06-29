
class Solution:
    # 返回构造的TreeNode根节点
    def find_min(self, nums):
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while right-left > 1:
            mid = right - (right - left) // 2

            # 左中右相等则顺序查找
            if nums[mid] == nums[right] and nums[mid] == nums[left]:
                for i in range(left, right):
                    if nums[i+1] < nums[i]:
                        return nums[i+1]

            if nums[left] > nums[right]:
                # 中间数大于左，旋转点在后半
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid
        return nums[right]


nums = [3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 3]
# nums = [3, 4, 5, 6]
s = Solution()
result = s.find_min(nums)
print(result)
