#!user/bin/env python
#python shellSort.py
#kiki 18/05/04
from insertionSort import insertionSort
#引入直接插入排序，另一个py文件里

"""
testList
[]
[0]
[5,2]
[1,5,2,5,6,7,4,6,3]
[592,401,874,141,348,72,911,887,820,283]
[5,4,3,2,1]
[3,-4,5,8]
[-3,-4]
"""

#希尔排序，这段函数居然一次通过，我tnd真是个天才，我智商肯定有160（今天电影艺术课上看到阿甘有160）！
def shellSort(ilist):
    if len(ilist) <= 1:
        return ilist
    n = len(ilist)//2 #取增量长短为总数一半，向下取正，增量的选取很大程度上影响运行时间
    while n > 0: #增量减少到0之前
        for i in range(n): #从头开始，进行分组
            tempList = [] #缓存列表，用于存储获得的分组
            k = i #从第i个开始，增量为n
            t = 0 #计数，用来标记缓存列表中的数据
            while k < len(ilist): #分组，为分组的列表获得要求的元素
                tempList.append(ilist[k]) #获得指定增量的元素
                k = k + n #索引增加指定增量
                t += 1 #计数
            tempList = insertionSort(tempList) #对缓存序列进行直接插入排序
            while k > i:
                k = k - n
                t -= 1
                ilist[k] = tempList[t] #将原序列中的元素
        n //= 2 #将增量减半
    #return insertionSort(ilist)
    

if __name__ == "__main__":
    testList = [592,401,874,141,348,72,911,887,820,283]
    shellSort(testList)
    print (testList)

"""
参考
def shellSort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists

    
if __name__ == "__main__":
    testList = [1,5,2,5,6,7,4,6,3]
    print (shellSort(testList))
"""
