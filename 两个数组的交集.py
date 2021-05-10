# @Time : 2021/5/10 19:48 
# @Author : cc
# @File : 两个数组的交集.py 
# @Software: PyCharm
'''
给定两个数组，编写一个函数来计算它们的交集。
'''
#解题思路，双指针，先将两个数组排序，两个指针放于两个数组的首位，比较两指针的大小
def intersect(nums1,nums2):
    nums1.sort()
    nums2.sort()
    i,j = 0,0
    box = []
    lengh1,lengh2 = len(nums1),len(nums2)
    while lengh1 > i and lengh2> j: #确保两个指针小于数组长度，防止指针长度长于数组长度而报错
        if nums1[i] == nums2[j]:
            box.append(nums1[i]) #如果两指针相等，将指针的值放入一个空列表中，同时两个指针后移一位
            i += 1
            j += 1
        elif nums1[i] > nums2[j]: #若两指针不相等，则将值小的指针后移一位
            j += 1
        else:
            i += 1
    print(box)

nums1 =[4,9,5]
nums2 =[9,4,9,8,4]
intersect(nums1,nums2)

