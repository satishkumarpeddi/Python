from typing import List,Optional
class TreeNode:
    def __init__(self,data,left=None,right=None,height=0):
        self.data=data
        self.left=left
        self.right=right
        self.height = height
class Construction:
    def height(self,root:TreeNode) ->Optional[int]:
        if root is None:
            return 0
        return root.height
    def balanceFactorMethod(self,root:TreeNode) ->Optional[int]:
        if root is None: 
            return 0
        return self.height(root.left)-self.height(root.right)
    def minValueNode(self,root:TreeNode) -> Optional[TreeNode]:
        if root is None :
            return None
        curr : TreeNode = root
        while curr is not None:
            curr = curr.left
        return curr
    def rightRotation(self,x: TreeNode) -> Optional[TreeNode]:
        y: TreeNode = x.left
        T2: TreeNode = y.right
        y.right = x
        x.left=T2
        x.height = 1+max(self.height(x.left),self.height(x.right))
        y.height = 1+max(self.height(y.left),self.height(y.right))
        return y
    def leftRotation(self,y: TreeNode) -> Optional[TreeNode]:
        x:TreeNode = y.right
        T2:TreeNode = x.left
        y.right= T2
        x.left= y
        x.height = 1+max(self.height(x.left),self.height(x.right))
        y.height = 1+max(self.height(y.left),self.height(y.right))
        return x
    
    def insertMethod(self,root:TreeNode,data:int) -> Optional[TreeNode]:
        if root is None: 
            return TreeNode(data)
        if data < root.data:
            root.left = self.insertMethod(root.left,data)
        elif data > root.data:
            root.right = self.insertMethod(root.right,data)
        else:
            return root
        root.height = 1+max(self.height(root.left),self.height(root.right))
        balanceFactor = self.balanceFactorMethod(root)
        if root.left is not None and balanceFactor > 1 and data < root.left.data :
            return self.rightRotation(root)
        if root.right is not None and balanceFactor <-1 and data > root.right.data :
            return self.leftRotation(root)
        if root.left is not None and balanceFactor < 1 and data < root.left.data :
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        if root.right is not None and  balanceFactor <-1 and data> root.right.data :
            root.right=  self.rightRotation(root.right)
            return self.leftRotation(root)
        return root
class Traversal:
    def preorder(self,root: TreeNode) -> Optional[TreeNode]:
        if root is None :
            return None
        print(root.data, end=" -> ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root: TreeNode) -> Optional[TreeNode]:
        if root is None :
            return None
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" -> ")
    def inorder(self,root: TreeNode) -> Optional[TreeNode]:
        if root is None :
            return None
        self.inorder(root.left)
        print(root.data, end=" -> ")
        self.inorder(root.right)
    def levelorder(self,root: TreeNode) -> Optional[TreeNode]:
        if root is None :
            return None
        queue:List[TreeNode] = [root]
        front=0
        while front < len(queue): 
            curr = queue[front]
            front+=1
            print(root.data, end=" -> ")
            if curr.left is not None : 
                queue.append(curr.left)
            if curr.right is not None :
                queue.append(curr.right)
                
root : TreeNode = None      
list_of_elements = [11,4,5,1,2,0,9,8,7,4,3]
for x in list_of_elements:
    root = Construction().insertMethod(root,x)

print("Pre-Order Traversal : ")
Traversal().preorder(root)
print("NULL\n")
print("Post-Order Traversal : ")
Traversal().postorder(root)
print("NULL\n")
print("In-Order Traversal : ")
Traversal().inorder(root)
print("NULL\n")
print("Level-Order Traversal : ")
Traversal().levelorder(root)
print("NULL\n")