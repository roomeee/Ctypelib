class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peak(self):
        if (self.is_empty()):
            return print('Stack empty')
        else:
            return print(self.top.data)

    def pop(self):
        if (self.is_empty()):
            return print('Stack empty')
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next


s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.peak()
s.traverse()


def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    res = ''
    while (not s.is_empty()):
        res = res + s.pop()
    print(res)


reverse_string('hello')
