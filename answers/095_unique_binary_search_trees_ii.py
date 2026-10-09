# 95. unique binary search trees II
# pick each value as root, combine all left/right subtree options

# leetcode provides this:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def build(lo, hi):
            if lo > hi:
                return [None]
            trees = []
            for root_val in range(lo, hi + 1):
                for left in build(lo, root_val - 1):
                    for right in build(root_val + 1, hi):
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n)
