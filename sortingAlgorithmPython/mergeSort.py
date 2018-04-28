#!user/bin/env python
#python mergeSort.py
#kiki 18/04/27
#https://www.cnblogs.com/Lin-Yi/p/7309143.html 参考

#合并两个序列（不论是不是有序，因为segmentation函数会把序列分到不可再分，也就是一个元素时），比较两个序列的头元素，小的放入新序列中。
def mergeList(left,right):
    sortedList = []
    #i=0
    while left and right: #当左右两序列同时存在时
        if left[0] >= right[0]:
            sortedList.append(right[0])
            del right[0]
        elif left[0] < right[0]:
            sortedList.append(left[0])
            del left[0]
        #print(i)
        #i+=1
        
    while left and right==[]: #当右序列没有元素时
        sortedList = sortedList + left
        left = []
    
    while right and left==[]: #当左序列没有元素时
        sortedList = sortedList + right
        right = []
        #print ("ok")
    
    return sortedList #返回合并序列
    
#将序列分到不可再分，并且实现并归排序。
def segmentation(sortingList):
    if len(sortingList) == 1: #判断是否分到不可再分，当只有一个元素时不需再分，返回这个元素
        return sortingList
        
    n = len(sortingList)//2 #从中间将序列切分成两段
    left = segmentation(sortingList[:n]) #调用切分函数不断切分
    right = segmentation(sortingList[n:])

    return mergeList(left,right) #返回合并序列
    

if __name__ == "__main__":
    leftTest = [3,7,2,6,8,1,67,64] #测试用例，检测合并函数是否正常
    rightTest = [4,461,46,55,3,23]
    testList = [1,35,3,5,453,3,67,2,98,64] #最终测试序列，3出现了两次
    print (mergeList(leftTest,rightTest)) #输出合并结果
    print (segmentation(testList)) #输出排序结果
    
    
"""
上面网址内的代码，供参考
def merge_sort( li ):
 2     #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
 3     if len(li) == 1:
 4         return li
 5 
 6     #取拆分的中间位置
 7     mid = len(li) // 2
 8     #拆分过后左右两侧子串
 9     left = li[:mid]
10     right = li[mid:]
11 
12     #对拆分过后的左右再拆分 一直到只有一个元素为止
13     #最后一次递归时候ll和lr都会接到一个元素的列表
14     # 最后一次递归之前的ll和rl会接收到排好序的子序列
15     ll = merge_sort( left )
16     rl =merge_sort( right )
17 
18     # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
19     # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
20     return merge(ll , rl)
21 
22 #这里接收两个列表
23 def merge( left , right ):
24     # 从两个有顺序的列表里边依次取数据比较后放入result
25     # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
26     result = []
27     while len(left)>0 and len(right)>0 :
28         #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
29         if left[0] <= right[0]:
30             result.append( left.pop(0) )
31         else:
32             result.append( right.pop(0) )
33     #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
34     result += left
35     result += right
36     return result
37 
38 if __name__ == '__main__':
39     li = [5,4 ,3 ,2 ,1]
40     li2 = merge_sort(li)
41     print(li2)
"""
