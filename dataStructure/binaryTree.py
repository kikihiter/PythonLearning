#!user/bin/env python
# python binaryTree.py
# kiki 2018/08/15

#定义树节点
class treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
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
    print ("DLR/n")
    DLR(itree)
    print ("LDR/n")
    LDR(itree)
    
    
