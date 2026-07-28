# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []

#         def dfs(node):
#             if not node:
#                 return

#             dfs(node.left)
#             ans.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return ans


# iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans