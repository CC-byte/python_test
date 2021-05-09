# @Time : 2021/5/9 16:42 
# @Author : cc
# @File : 数组中只出现一次的数字.py 
# @Software: PyCharm

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''

#解题思路，题目要求线性时间复杂度，并且不使用额外空间，考虑用异或来解决问题，两个相同的数异或结果为0,0和任何一个数异或结果为它本身
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        let = 0  #构建一个示例0，和数组的第一个元素进行异或
        for i in nums:
            let = let^i
        return let