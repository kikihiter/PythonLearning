#!user/bin/env python
# python binaryTree1.py
# kiki 2018/08/16
"""
# 添加了先序遍历和后序遍历
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
        
def inorder_thlinked(thrt):
    root = thrt.left
    #print (root.val)
    while root != None:
        while root.ltag == 0:
            root = root.left
            print (root.val,root.ltag,root.rtag)
        while root.rtag == 1 and root.right != thrt:
            root = root.right
            print (root.val)
        root = root.right
   
def xiansuo(root):
    if root != None:
        if root.left != None and root.ltag == 0:
            forward = xiansuo(root.left)
            forward.rtag = 1
            forward.right = root
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
            return final
        return root

if __name__ == "__main__":
    exmple = ["-","+","/","a","*","e","f","","","b","-","","","","","","","","","","","c","d","","","","","","","",""]
    """
                    -
        +                         /
    a       *               e          f
        b       -
            c       d
    """
    itree = buildTree(exmple)
    #rint (itree)
    print ("DLR:")
    DLR(itree)
    print ("\nLDR:")
    LDR(itree)
    print ("\nLRD:")
    LRD(itree)
    print ("\n")
    #inorder_thlinked(crt_inthlinked(itree))
    xiansuo(itree)
    