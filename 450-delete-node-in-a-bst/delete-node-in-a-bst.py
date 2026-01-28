# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            minVal = self.min_val(root.right) 
            root.val = minVal
            root.right = self.deleteNode(root.right, minVal)
        return root

    def min_val(self, curr):
        while curr.left:
           curr = curr.left 
        return curr.val


            

        