"""
No.: 100
Topic: depth first search, tree, binary tree

############################################
Question:
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

Approach:
1. use a stack to store the [root node] in tuples, why tuples, binary tree has 2 node only
2. loop through the stack, how:
    pop both of the trees and compare
        Condition A: if any of them has a value (meaning one of them is a tree), continue, 
        Condition B: if neither of them have a value (meaning both of the inputs are not tree), its a false
        Condition C: else, if their value is not the same (meaning the trees are not the same), its a false
3. append the [left and right node ] (aka child node) of both the tree, how:
    append both the right node of each Tree Node into the stack, do the same for the left, end of loop
4. if loop ended without triggering Condition B, both nodes are the same
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
