# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newlist = head

        while newlist and newlist.next:
            if newlist.val == newlist.next.val:
                newlist.next = newlist.next.next
            else:
                newlist = newlist.next

        return head