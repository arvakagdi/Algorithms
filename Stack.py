class stack (object):
    def __init__(self):
        self.stack = list()

    def push (self,data):
        self.stack.append(data)

    def pop (self):
        if len(self.stack) > 0:
            return (self.stack.pop())
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return (self.stack[len(self.stack)-1])
        else:
            return None

    def __str__(self):
        return str(self.stack)


Mystack = stack()
print(Mystack)
Mystack.push(1)
Mystack.push(10)
Mystack.push(100)
print(Mystack)
print(Mystack.peek())
print(Mystack.pop())
print(Mystack)
print(Mystack.pop())
print(Mystack.pop())
print(Mystack)
print(Mystack.pop())
print(Mystack)
