class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Empty Linked List: )
        self.head = None
        # no of nodes or length
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        # connection
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + '->'
            current = current.next
        return result[:-2]

    # head --> Node(3, next=Node(2, next=Node(1)))
    # traverse to the the last node(tail) set the next of tail to new node
    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next
        #             yoy=u are at last node
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            print('ITEM not found')
        # print(curr.data)

    #         case: 1 break (item found) current is not none case: 2(loop fully executed and item not found)

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return print('Empty linked List')
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):  # pop delete tail'
        if self.head == None:
            return print('Empty linked List')
        curr = self.head
        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1

    def remove(self, value):
        if self.head == None:
            return print('Empty linked List')
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        #         case 2 item found 3 wala node or not found 5 pr tail
        if curr.next == None:
            return print('Not found')
        else:
            curr.next = curr.next.next

    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'Not Foynd'

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'index error'
    # def search(self, item):
    #     curr= self.head
    #     pos=0
    #     while curr !=None:
    #         if curr.data== item:
    #             return pos
    #         curr= curr.next
    #         pos= pos+1
    #     return 'Not Found'


L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)

# print(L.search(3))
