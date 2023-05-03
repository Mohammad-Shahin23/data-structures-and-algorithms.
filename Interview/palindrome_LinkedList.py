class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    if head is None:
        return True

    # Find the middle of the linked list
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    curr = slow.next
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # Compare the first half and the reversed second half
    p1 = head
    p2 = prev
    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next

    return True

