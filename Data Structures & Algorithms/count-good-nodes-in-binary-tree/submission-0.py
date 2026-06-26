# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurDFSwithMax(self,root, maxSeen):
        if not root:
            return 0
        
        count = 0
        if root.val >= maxSeen:
            maxSeen = root.val
            count+=1
        
        leftSide = self.recurDFSwithMax(root.left,maxSeen)
        rightSide = self.recurDFSwithMax(root.right,maxSeen)
        # print(count + leftSide + rightSide)
        return count + leftSide + rightSide

    def goodNodes(self, root: TreeNode) -> int:
        #DFS seems like the way to go...
        #Idea: Build a allPaths 2D array. 
        
        #Given an array of numbers, how do you idenitfy how many numbers have no numbers bigger than them when iteating in order
        #start at fron of array, every time we encounter a new max number, inc by 1? Ok thats easy

        #We dont actually need to build an array we can just carry maxSeen and count in our dfs
        return self.recurDFSwithMax(root, -float('inf'))

        
        