"""
date: 1/5/2022
no.: 100
topic: depth first search, tree, binary tree

############################################
question:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

example:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
############################################

strategy:
1. use a stack to store the tuples, why tuples, binary tree has 2 node only
2. pop the two trees and compare
    if one of them are nodes, continue, 
    if they are null value in either, its a false
    else, if their value is not the same, its a false
3. append the next node and continue the loop
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True


p = TreeNode(None, TreeNode(1))
q = TreeNode(None, TreeNode(2), TreeNode(1))
# p = None
# q = None
solution = Solution()
solution.isSameTree(p, q)
