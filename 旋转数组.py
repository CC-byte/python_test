'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''
#第一种解题思路，借助空数组进行旋转
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    box = []
    k = k % len(nums) #防止出现k大于数组长度，无法操作
    for i in nums[len(nums)-k:]:
        box.append(i)
    box.extend(nums[0:len(nums)-k])
    return box
# test = rotate([1,2,3,4,5,6,7],3)
# print(test)
#第二种解题思路：三次翻转，先翻转整个数组，然后以k为节点，进行局部翻转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k]) #直接将逆序后的局部元素赋值给原来的数组
        nums[k:] = reversed(nums[k:])
        return nums
