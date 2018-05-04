#!user/bin/env python
#python quickSort.py
#kiki 18/05/02
#https://blog.csdn.net/razor87/article/details/71155518 参考

"""
编写过并归排序后，这个变得简单多了，几乎一次成功，但是我意识到我编写的这些代码其实测试的并不够多，以后应该编写多一些的测试样例，帮助测试算法健壮性。
"""

#快速排序算法，主要思想是选择一个标准，将小于这个数的放到这个数左边，右边放大的。
def quickSort(ilist):
    if len(ilist) <= 1: #判断是否分到最小了
        return ilist
    medium = ilist[0] #选择列表第一个数为标准，标准的选择与最终的运行时间有很大的相关性，网上说可以选择开始中间结尾三个数的中位数作为基准
    mediumList = [] #建立新列表存放于标准数相同的元素
    leftList = [] #新列表放小的数
    rightList = [] #新列表放大的数
    for i in ilist:
        if i < medium:
            leftList.append(i) #当小于s时存放到leftList中
        elif i == medium:
            mediumList.append(i)
        elif i >medium:
            rightList.append(i)
    leftList = quickSort(leftList) #将左边的序列继续调用函数自身排序
    rightList = quickSort(rightList) #右侧的也是
    return leftList + mediumList + rightList #返回排好序的序列
    
    
if __name__ == "__main__":
    testList = [12,3,5,32,234,43,45,5,4,5,87,9,2] #测试用例
    print (testList) #打印测试用例
    print (quickSort(testList)) #打印排好序的序列
    #[2, 3, 4, 5, 5, 5, 9, 12, 32, 43, 45, 87, 234] #输出结果
    
    
"""
def quick_sort(array, left, right):  
    if left >= right:  
        return  
    low = left  
    high = right  
    key = array[low]  
    while left < right:  
        while left < right and array[right] > key:  
            right -= 1  
        array[left] = array[right]  
        while left < right and array[left] <= key:  
            left += 1  
        array[right] = array[left]  
        print (array)
    array[right] = key  
    quick_sort(array, low, left - 1)  
    quick_sort(array, left + 1, high)  
    

if __name__ == "__main__":
    testList = [23,5,2,7,56,5]
    quick_sort(testList,0,5)
    print (testList)
"""
