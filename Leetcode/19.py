# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        newlist = ListNode(0)
        newlist = head

        i = 0
        while head:
            i += 1
            head = head.next
        numtodel = i - n

        head = newlist

        if head.next is None:
            return None

        elif numtodel == 0:
            newlist = newlist.next
            return newlist
        else:
            for i in range(numtodel - 1):
                newlist = newlist.next
            newlist.next = newlist.next.next
            return (head)