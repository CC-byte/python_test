class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j< len(nums):
            # print(nums[i])
            # print(nums[j])
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        # print(str(i+1)+','+str(nums[0:i+1]))
        return i+1

'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
来源：力扣（LeetCode）
'''