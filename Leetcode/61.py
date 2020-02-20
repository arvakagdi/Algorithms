# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        elif head == None:
            return None
        else:
            newlist = head

            length = 0
            while head:
                length += 1
                head = head.next
            oldlength = length
            head = newlist

            if length == 1:
                return head
            else:

                x = k % length
                for i in range(x):
                    while length != 2:
                        head = head.next
                        length -= 1
                    new = ListNode(head.next.val)
                    print(new)

                    head.next = None
                    new.next = newlist
                    print(new)

                    head = new
                    newlist = head
                    length = oldlength
                return (newlist)