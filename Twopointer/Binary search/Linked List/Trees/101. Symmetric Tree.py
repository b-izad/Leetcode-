'''101. Symmetric Tree
Easy

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100'''

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
            
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
            
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False
