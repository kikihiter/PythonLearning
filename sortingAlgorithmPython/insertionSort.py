#!user/bin/env python
#python insertionSort.py
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

#插入排序(直接插入)
def insertionSort(list):
    if len(list) <= 1: #不说了
        return list
    relist = [] #创建一个空列表，用于储存已排序序列
    for i in range(len(list)): #不断从原序列中取出元素
        if i == 0: #取出的第一个元素
            relist.append(list[i]) #在返回序列中储存第一个元素
        elif i >0: #取出后面的元素
            for j in range(len(relist)): #从左侧开始与返回序列进行比较
                if list[i] < relist[j]: #返回序列中比取出元素大的第一个元素
                    relist = relist[:j] + [list[i]] + relist[j:] #插入取出元素
                    break #打破循环，不必与返回序列的后续元素进行比较
            else: #当返回序列中没有元素比取出元素大时
                relist.append(list[i]) #将取出元素置入返回序列末端
    return relist #返回已完成排序的返回序列
                    
if __name__ == "__main__":
    testList = [1,5,2,5,6,7,4,6,3]
    print(insertionSort(testList))
    #[1, 2, 3, 4, 5, 5, 6, 6, 7]
