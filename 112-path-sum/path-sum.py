# class Solution:
#     def hasPathSum(self, root, targetSum):
#         if not root:
#             return False

#         if not root.left and not root.right:
#             return targetSum == root.val

#         return (
#             self.hasPathSum(root.left, targetSum - root.val) or
#             self.hasPathSum(root.right, targetSum - root.val)
#         )

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True

            if node.right:
                stack.append((node.right, curr_sum + node.right.val))

            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False