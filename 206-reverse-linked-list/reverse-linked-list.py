# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         arr = []

#         current = head

#         # Put all nodes in array
#         while current:
#             arr.append(current)
#             current = current.next

#         # Reverse connections
#         for i in range(len(arr) - 1, 0, -1):
#             arr[i].next = arr[i - 1]

#         # Old head becomes last node
#         if arr:
#             arr[0].next = None
#             return arr[-1]

#         return None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev