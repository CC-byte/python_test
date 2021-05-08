# @Time : 2021/5/8 21:03 
# @Author : cc
# @File : 判断数组是否存在重复元素.py 
# @Software: PyCharm
'''
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
'''
#第一种思路，直接列表去重，比较去重之后列表和原列表的长度，一样则元素都不相同，返回false，反之返回true
def containsDuplicate(demo_list):
    print(set(demo_list))
    if len(demo_list) == len(set(demo_list)):
        return False
    else:
        return True

demo_list = [1,2,3,4,5]
print(containsDuplicate(demo_list))

#第二种思路，对数组进行排序，然后判断相邻两个元素是否相等,如果相等则有相同元素返回true，反之不相同返回false
def containsDuplicate(demo_list):
    demo_list = sorted(demo_list)
    for i in range(len(demo_list)):
        if demo_list[i] != demo_list[i+1]:
            return False
        else:
            return True

demo_list = [1,2,2,4,5]
print(containsDuplicate(demo_list))

#第三种解题思路，使用一个哈希表来存储遍历的值，当遍历到的值已经存在哈希表中，则说明存在重复

def containsDuplicate(demo_list):
    dic = {}  #字典就是哈希表的一种
    for i in demo_list:
        if i not in dic:
            dic[i] = 1
        else:
            return True
    return False

demo_list = [1,2,3,4,5]
print(containsDuplicate(demo_list))