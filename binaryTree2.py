#!user/bin/env python
# python binaryTree1.py
# kiki 2018/08/17
"""
# 线索二叉树线索化尝试中(中序、先序遍历已成功，后续遍历先不写了)
# 增加节点检测函数jiance(),可以以中序遍历的序列输出全部节点
# 修改了先序遍历线索化过程中的递归操作，减少了不必要的递归操作
"""

#定义树节点
class treenode(object):
    def __init__(self, x):
        self.val = x
        self.ltag = 0
        self.left = None
        self.rtag = 0
        self.right = None

#以列表建树
def buildTree(nodeList):
    maxsize = len(nodeList)
    def transRoot(root,n):
        #root.val =  nodeList[n-1]
        if 2*n < maxsize + 1 and nodeList[2*n-1] != "":
            leftChild = treenode(nodeList[2*n-1])
            root.left = leftChild
            transRoot(leftChild,2*n)
        if 2*n + 1 < maxsize + 1 and nodeList[2*n] != "":
            rightChild = treenode(nodeList[2*n])
            root.right = rightChild
            transRoot(rightChild,2*n+1)
        return root
    if maxsize == 0:
        return None
    elif maxsize > 0:
        if nodeList[0] == "":
            return None
        else:
            firstRoot = treenode(nodeList[0])
            return transRoot(firstRoot,1)

#先序遍历
def DLR(root):
    print (root.val)
    if root.left != None:
        DLR(root.left)
    if root.right != None:
        DLR(root.right)#

#中序遍历
def LDR(root):
    if root.left != None:
        LDR(root.left)
    print (root.val)
    if root.right != None:
        LDR(root.right)

#后序遍历
def LRD(root):
    if root.left != None:
        LRD(root.left)
    if root.right != None:
        LRD(root.right)#
    print (root.val)

#书本上的算法（P131算法6.5以及算法6.6），我用python实现了一下，发现并不能够完美运行，这里的想法是时刻保留一个pre指针用于指向上一个节点（遍历序列中的上一个节点）
#可能是不同语言作用域的问题，原算法中的pre并不有效，在这里，我为它设置了一个全局变量
global pre
def crt_inthlinked(root):
    thrt = treenode("")
    thrt.ltag = 0
    thrt.rtag = 1
    thrt.right = thrt
    if root ==None:
        thrt.left = thrt
    else:
        thrt.left = root
        global pre
        pre = thrt
        #我将算法6.6内嵌其中，本来是为了解决pre的问题，但是用了全局变量之后，这样做已经没有什么意义
        def inthread(iroot):
            if iroot != None:
                inthread(iroot.left)
                if iroot.left == None:
                    global pre
                    iroot.ltag,iroot.left = 1,pre
                    if pre.right == None:
                        pre.rtag,pre.right = 1,iroot
                ipre = iroot
                inthread(iroot.right)
        
        inthread(root)
        pre.right,pre.rtag = thrt,1
        thrt.right = pre
    return thrt

#对线索二叉树进行中序遍历，传入值为头结点（头结点内容应为None，python我不知道如何实现，这里用的“”，它的节点结构为【指向树的根节点，被序列第一个节点所指为其前驱|0|“”|1|指向序列最后一个节点，被序列最后一个节点所指为其后继】）    
def inorder_thlinked(thrt):
    root = thrt.left
    #print (root.val)
    while root != None and root != thrt:
        while root.ltag == 0:
            root = root.left
        print (root.val)
        while root.rtag == 1 and root.right != thrt:
            root = root.right
            print (root.val)
        root = root.right
   
#书上的算法总是实现不了，我按自己的想法写了一个线索化的函数，这个函数返回的是当前根节点下中序遍历序列的最后一个节点
def xiansuo(root):
    #当前根节点不为空的情况下进行操作
    if root != None:
        #对当前根节点的左子树进行操作
        if root.left != None and root.ltag == 0:
            #返回的是左子树的最后一个序列，将其指向当前根节点，更改其右指示域
            forward = xiansuo(root.left)
            forward.rtag = 1
            forward.right = root
        #对当前根节点的右子树进行操作，找到后继元素（即右子树中序遍历序列的第一个节点）
        if root.right != None and root.rtag == 0:
            behind,final = root.right,root.right
            while behind.left != None and behind.ltag == 0:
                behind = behind.left
            behind.ltag = 1 
            behind.left = root
            xiansuo(root.right)
            while final.right != None and final.rtag == 0:
                xiansuo(final)
                final = final.right
            #右子树不为空的情况下，返回右子树的最后一个节点，也就是当前节点的遍历序列的最后一个节点
            return final
        #右子树为空的情况，返回当前节点，也就是当前节点的遍历序列的最后一个节点
        return root

#遍历序列的第一个节点和最后一个节点需要进行处理，建立一个头结点，返回这个头结点
def buildHead(root):
    #好吧，直接设成None就行了
    thrt = treenode(None)
    thrt.ltag = 0
    thrt.rtag = 1
    thrt.right = thrt
    if root ==None:
        thrt.left = thrt
    else:
        thrt.left,first = root,root
        while first.left != None and first.ltag == 0:
            first = first.left
        first.ltag,first.left = 1,thrt
        final = xiansuo(root)
        final.right,final.rtag = thrt,1
        thrt.right = final
    return thrt

#利用中序遍历，输出各个节点的各项数据，传入节点可以是根节点也可以是头结点,主要用于显示各个节点信息
def jiance(root):
    if root.left != None and root.ltag == 0:
        jiance(root.left)
    print(root.val,root.ltag,root.rtag)
    if root.right != None and root.rtag == 0:
        jiance(root.right)

def DLRthread(root):
    if root != None:
        if root.left != None:
            forward = DLRthread(root.left)
            if root.right != None and root.rtag == 0:
                forward.rtag,forward.right = 1,root.right
                final = root.right
                DLRthread(root.right)
                while final.right != None and root.rtag == 0:
                    final = final.right
                if final.left != None:
                    final = DLRthread(final.left)
                return final
            return forward
        if root.right != None and root.rtag == 0:
            DLRthread(root.right)
        while root.right != None and root.rtag == 0:
            root = root.right
        if root.left != None:
            root = DLRthread(root.left)
        return root
    
def DLRshow(root):
    while root != None:
        print (root.val)
        while root.left != None:
            print (root.left.val)
            root = root.left
        root = root.right
    
    
if __name__ == "__main__":
    exmple = ["-","+","/","a","*","e","f","","","b","-","","","","","","","","","","","c","d"]
    """
                    -
        +                         /
    a       *               e          f
        b       -
            c       d
    DLR:-+a*b-cd/ef
    LDR:a+b*c-d-e/f
    LRD:abcd-*+ef/-
    """
    exmple1 = ["a","b","c","d","e","f","g","","i","j","k","l","m","","o","","","r","","","u","","","x","y","z"]
    """
                                    a
                      b                          c
              d              e             f           g
                  i      j      k      l      m           o
                r         u          x  y    z
    DLR:abdirejukcflxymzgo
    LDR:dribjuekaxlyfzmcgo
    LRD:ridujkebxylzmfogca
    """
    itree = buildTree(exmple1)
    #rint (itree)
    print ("DLR:")
    DLR(itree)
    print ("\nLDR:")
    LDR(itree)
    print ("\nLRD:")
    LRD(itree)
    print ("\n")
    print ("先序遍历线索化中......")
    DLRthread(itree)
    #inorder_thlinked(buildHead(itree))
    #print ("\n")
    print ("线索化成功")
    jiance(itree)
    DLRshow(itree)
    