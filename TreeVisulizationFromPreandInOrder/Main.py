from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Main:
    def build(self,preorder: List[int],inorderLeft:int,inorderRight:int,inorderSize:int,preorderSize:int,hashMap:dict):
        if inorderLeft > inorderRight:
            return None
        rootValue : int = preorder[self.preorderIndex]
        self.preorderIndex+=1
        root:TreeNode = TreeNode(rootValue)
        rootIndexValue : int =  hashMap[rootValue]
        root.left = self.build(preorder,inorderLeft,rootIndexValue-1,inorderSize,preorderSize,hashMap)
        root.right = self.build(preorder,rootIndexValue+1,inorderRight,inorderSize,preorderSize,hashMap)
        return root
    def buildTree(self,preorder: List[int],inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {}
        for i in range(len(inorder)):
            hashMap[inorder[i]] = i
        self.preorderIndex = 0
        return self.build(preorder,0,len(inorder)-1,len(inorder),len(preorder),hashMap)

class Traversal:
    def postorder(self,root:TreeNode) ->Optional[None]:     
        if root is None:
            return None
        print(root.val,end=" ")
        self.postorder(root.left)
        self.postorder(root.right)
preorder = [1,2,4,5,3,6,7]
inorder = [4,2,5,1,6,3,7]
root:TreeNode = Main().buildTree(preorder,inorder)
Traversal().postorder(root)
