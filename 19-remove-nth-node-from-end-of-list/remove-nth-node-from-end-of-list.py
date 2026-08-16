class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next