class Node(object):
    def __init__ (self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext



class LinkedList(object):
    def __init__ (self):
        self.head = None

    def insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode


    def ListSize(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def printlist (self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next


MyList = LinkedList()
MyList.head = Node(1)
second = Node(2)
third = Node(3)

MyList.head.next = second
second.next = third

MyList.printlist()


A = [1,2,3]
print(A)
A = A[::-1]
print(A)