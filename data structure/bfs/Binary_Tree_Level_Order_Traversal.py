"""
No.102
Topic: tree, bfs, binary tree

###############################
Question:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Contraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
###############################

Approach:
1. when looping through the root:
    -remove the first node of the root
    -append the rest to a temp, then continue with the loop
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            print([])
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])

            # for node in level:            cant really use this approach even though it look almost the same as the code above, why, run it through the compiler to find out more
            #     ans.append([node.val])

            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        print(ans)
        return ans


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
solution.levelOrder(root)
