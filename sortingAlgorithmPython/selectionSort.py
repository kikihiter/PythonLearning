#!user/bin/env python
#python selectionSort.py
#kiki 18/05/04

"""
testList
[]
[0]
[5,2]
[1,5,2,5,6,7,4,6,3]
[3,-4,5,8]
[-3,-4]
"""

#选择排序
def selectionSort(list):
    if len(list) <= 1:
        return
    relist = []
    #min = list[0]
    for i in range(len(list)-1): #从左侧开始提取比较元素
        for j in range(len(list[i+1:])): #从比较元素右侧开始寻找比比较元素更小的元素
            if list[i] > list[i+j+1]: #当有比比较元素更小的元素时
                list[i],list[i+j+1] = list[i+j+1],list[i] #交互比较元素与较小元素，在这里我们每次发现较小数都进行交互，实际上应该是搜索出比较元素及比较元素右侧序列中的最小元素进行交换，有可能可以提高算法效率。但是我不大清楚，python中列表交换元素的工作机制，在此选择较为简单的写法。


if __name__ == "__main__":
    testList = [1,5,2,5,6,7,4,6,3]
    selectionSort(testList)
    print (testList)
