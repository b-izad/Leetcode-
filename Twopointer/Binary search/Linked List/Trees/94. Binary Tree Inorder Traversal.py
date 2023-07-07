''' Remember in context of recursive calles we cant have a list in the function since each recursive call will make a new variable for that list and it doesnt work unless we use a list like the first solution, the second solution define a list variable in a seperate function
here is explanation according to chat gpt:
The primary reason we need a nonlocal variable in this scenario is because we're dealing with recursion. In recursion, the function calls itself and the recursion may happen multiple levels deep. We want to have a way of accumulating results across all of these levels of recursion.

If we defined the result variable inside the recursive function and it's not nonlocal, each recursive call would get its own separate copy of the result variable. Modifying the result variable in one recursive call wouldn't affect the result variable in another recursive call. This is not what we want. We want all recursive calls to share the same result variable, so that they can all contribute to the final result.

By making the result variable nonlocal (or a class attribute, in the case of a method inside a class), we ensure that all recursive calls share the same result variable. This allows them to collectively build up the final result.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result
