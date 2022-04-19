"""
date: 19/4/2022
no.: 98
topic: depth first search, tree, binary tree

############################################
question:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
############################################

strategy:
1. initialize an array to store value of node.val
2. loop through the node in the correct sequence (top -> left -> right), but if left node has a left node, go into the left node
3. store the value in the array
4. loop through the array, the array must be in ascending order
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Time complexity of inorder traversal is O(n)
        # Fun fact: Inorder traversal leads to a sorted array if it is a Valid Binary Search. Tree.
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                # print(False)
                return False
        # print(True)
        return True

    def inorder(self, root, output):
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


root = TreeNode(2, TreeNode(1), TreeNode(3))
solution = Solution()
solution.isValidBST(root)
