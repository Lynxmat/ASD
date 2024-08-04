#You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
#The binary tree has the following definition:
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#Initially, all next pointers are set to NULL.
#Queue could be used also

class Node:
    def __init__(self,val=0,left=None,right=None,next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if root is None:
        return

    lvl = []
    def dfs_visit(point,level=0):
        if len(lvl)-1 < level:
            lvl.append([])
        lvl[level].append(point)

        if point.left is not None:
            dfs_visit(point.left,level+1)
        if point.right is not None:
            dfs_visit(point.right,level+1)
    
    dfs_visit(root)
    
    for element in lvl:
        for i in range(len(element)-1):
            element[i].next = element[i+1]
    return root

def print_tree(point):
    print(point.val)

    if point.next is not None:
        print(point.next.val)
    else:
        print(None)
    

    if point.left is not None:
        print_tree(point.left)
    if point.right is not None:
        print_tree(point.right)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

connect(a)
print_tree(a)