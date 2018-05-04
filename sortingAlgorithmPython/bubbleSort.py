#!user/bin/env python
#python bubbleSort.py
#kiki 18/05/04

"""
testList
[]
[0]
[1,5,2,5,6,7,4,6,3]
"""

#冒泡排序
def bubbleSort(list):
    if len(list) <= 1: #只有一个元素或者没有元素时，直接返回
        return
    for i in range(len(list)-1): #设置循环次数n-1
        for j in range(len(list)-1): #从头开始比较
            if list[j] > list[j+1]: #当后者大于前者时
                list[j],list[j+1] = list[j+1],list[j] #交换这两个元素的位置
                
                
if __name__ == "__main__":
    testList = [1,5,2,5,6,7,4,6,3] #测试用例
    bubbleSort(testList) #冒泡排序
    print (testList) #打印排序完成的序列
    #[1, 2, 3, 4, 5, 5, 6, 6, 7]
