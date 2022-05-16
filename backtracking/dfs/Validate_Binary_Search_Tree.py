"""
No.: 98
Topic: depth first search, tree, binary tree

############################################
Question:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
############################################

Approach:
1. write an inorder traversal function to traverse the node, why, inorder traversal will make a sorted array if it is a Valid Binary Search Tree
2. loop through the array after the traversal, if it is sorted (aka ascending), it is valid 
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
        # Fun fact: Inorder traversal leads to a sorted array if it is a Valid Binary Search Tree.
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                print(False)
                return False
        print(True)
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
