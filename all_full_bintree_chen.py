# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        # Base case, when a tree has only 1 node
        if (N == 1):
            return [TreeNode(0)]
        for i in range(N-2, 0, -2):
            # Get the two children (sub trees) of a node
            tree1 = self.allPossibleFBT(i)
            tree2 = self.allPossibleFBT(N-1-i)
            # Iterate over all the sub trees and append a full tree to "res"
            for i in tree1:
                for j in tree2:
                    root = TreeNode(0)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res