from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#Manually Create a Tree
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.left=Node(4)
root.right.right=Node(5)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

 
#First Tree Recursion
#Preorder Traversal
'''Traversal	Order
Preorder	    Node → Left → Right
Inorder	        Left → Node → Right
Postorder	    Left → Right → Node'''

def Preorder_Traversal(root):
    if root == None:
        return
    print(root.val)
    Preorder_Traversal(root.left)
    Preorder_Traversal(root.right)

Preorder_Traversal(root)

print("inorder")

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(root)

print("postorder")


def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

postorder(root)

def countNodes(root):
    if root is None:
        return 0
    
    return 1 + countNodes(root.left) + countNodes(root.right)

print("count of Nodes - ",countNodes(root))


#Level Order Traversal (BFS) Prt
print("Level Order Traversal ")
def levelOrder(root):
    if root is None:
        return
    
    q = deque([root])
    
    while q:
        node = q.popleft()
        print(node.val)
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

levelOrder(root)

#🌳 Question: Height of Tree
#👉 Find maximum depth of tree
print("Find maximum depth of tree")

def Height_Tree(root):
    if root is None:
        return 0
    Height_left = 1+ Height_Tree(root.left)
    Height_right = 1+ Height_Tree(root.right)
    return max(Height_left , Height_right)

print(Height_Tree(root))

#🌳 Question: Check if Tree is Balanced
print("Check if Tree is Balanced")
def isBalanced(root):
    if root is None:
        return True
    
    left =   Height_Tree(root.left)
    right = Height_Tree(root.right)
    
    if abs(left - right) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

print(isBalanced(root))