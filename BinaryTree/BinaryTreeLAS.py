from typing import List,Optional

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def lowestCommonAncestorOfBS(root:Optional[TreeNode],p:Optional[TreeNode],q:Optional[TreeNode])-> Optional[TreeNode] :
    if root is None :
        return root
    if root.val > p.val and root.val > q.val:
        root.left = lowestCommonAncestorOfBS(root.left,p,q)    
    elif root.val<p.val and root.val< q.val:
        root.right = lowestCommonAncestorOfBS(root.right,p,q)
    else:
        return root
root = None
root = TreeNode(6);
root.left = TreeNode(2);
root.right = TreeNode(8);
root.left.left = TreeNode(0);
root.left.right = TreeNode(4);
root.right.left = TreeNode(7);
root.right.right = TreeNode(9);
root.left.right.left = TreeNode(3);
root.left.right.right = TreeNode(5);
result = lowestCommonAncestorOfBS(root,root.left,root.right);
print(result.val," -> is the lowest common ancestor of BinarySearchTree.\n")