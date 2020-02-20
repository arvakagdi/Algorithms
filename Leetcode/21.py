# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mylist = []
        ll2 = ListNode(0)
        while l1:
            mylist.append(l1.val)
            l1 = l1.next

        while l2:
            mylist.append(l2.val)
            l2 = l2.next

        mylist.sort()
        mylist = mylist[:: -1]

        list_to_return = None
        aux_node = None

        for element in mylist:
            if list_to_return == None:
                list_to_return = ListNode(int(element))
            else:
                aux_node = ListNode(int(element))
                aux_node.next = list_to_return
                list_to_return = aux_node
                aux_node = None

        return (list_to_return)
