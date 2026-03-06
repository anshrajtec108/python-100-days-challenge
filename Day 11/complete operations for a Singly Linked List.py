class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

#Traversal (Display List)
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
#Insert Operations
    #Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    #Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    #Insert at Position
    def insert_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

#Delete Operations
    #Delete First Node
    def delete_begin(self):
        if self.head:
            self.head = self.head.next
    
    #Delete Last Node
    def delete_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete by Value
    def delete_value(self, key):

        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

#Update Node Value
    def update(self, old, new):

        temp = self.head

        while temp:
            if temp.data == old:
                temp.data = new
                return
            temp = temp.next

#Search Operation
    def search(self, key):

        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1
    
# . Fast & Slow Pointer Technique

# Very important for interview problems.

# Used for:

# Find middle node

# Detect cycle

# Find kth node from end

# 8.1 Find Middle Node

# Fast moves 2 steps
# Slow moves 1 step

    def find_middle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
    

ll = LinkedList()

ll.insert_begin(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_position(1,15)

ll.traverse()

print("Middle:", ll.find_middle())

ll.delete_value(20)

ll.traverse()