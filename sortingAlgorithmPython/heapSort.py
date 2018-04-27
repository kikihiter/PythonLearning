#!user/bin/env python
#python heapSort.py
#kiki 18/04/27

#保证根节点为最大的
def maxChange(heap,size,i): #分别有三个参数，heap为传入的列表，size为列表长度，i为当前根节点索引号
    root = i
    left = i*2+1 #左子节点
    right = i*2+2 #右子节点
    """
    if left<size and heap[root]<heap[left]:
        heap[root],heap[left] = heap[left],heap[root]
        left,root = root,left
    if right<size and heap[root]<heap[right]:
        heap[root],heap[right] = heap[right],heap[root]
        right,root = root,right
    """
    if left<size and right<size: #当左右子节点存在时，选择其中最大的
        if heap[left]<=heap[right] and heap[root]<heap[right]: 
            heap[root],heap[right] = heap[right],heap[root]
            root,right = right,root
        elif heap[left]>heap[right] and heap[root]<heap[left]:
            heap[root],heap[left] = heap[left],heap[root]
            root,left = left,root
    elif left<size and right>=size: #左子节点存在而右子节点不存在时
        if heap[root]<heap[left]:
            heap[root],heap[left] = heap[left],heap[root]
            root,left = left,root
    elif right<size and left>=size: #右子节点存在而左子节点不存在时，讲道理，完全二叉树不存在这种情况，以防万一还是写了
        if heap[root]<heap[right]:
            heap[root],heap[right] = heap[right],heap[root]
            root,right = right,root
            
    if root != i: #当发生交换时，将索引向下传递，继续比较下一级
        maxChange(heap,size,root)
    
#创建堆，在这里调用的是maxChange，所以产生的是最大堆
def buildHeap(heap):
    size = len(heap)
    for i in range((size+1)//2-1)[::-1]: #从倒数第二层的最后一个节点开始进行比较
        maxChange(heap,size,i)
        
#堆排序，将列表由小到大排序，说实话，python自带序列排序，直接List.sort（）就行了。
def heapSort(heap):
    buildHeap(heap) #首先生成一个最大堆
    size = len(heap)
    for i in range(size-1,0,-1): #从最后一个元素开始，不断把堆中最后一个元素与第一个元素（堆中最大的数）进行调换，调换后，最后的元素进入排序完成区，利用前面的元素再次生成最大堆
        heap[0],heap[i] = heap[i],heap[0]
        maxChange(heap,i,0)
        
if __name__ == "__main__":
    a = [145, 65, 342, 341, 56, 7, 3, 56, 75, 73, 97] # 测试样例，其中65有两个
    print (a)
    buildHeap(a) #实际上，这里已经生成一个堆了，在下面堆排序的时候，重复了一次，但是这里是为了测试用的，去除后不影响
    print (a)
    heapSort(a) #时间复杂度O(nlogn)
    print (a)
