"""
    Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # invert left and right recursively
        # assign left root to inverted right root and right to inverted left root
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root
