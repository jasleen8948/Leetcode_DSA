class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        # Avoid unnecessary rotations
        k = k % n
        if k == 0:
            return head

        # Make circular list
        curr.next = head

        # Find new tail
        steps = n - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head