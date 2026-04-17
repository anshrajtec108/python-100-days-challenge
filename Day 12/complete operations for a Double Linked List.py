class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    #Display Forward 
    def display_forward(self):
        temp=self.head
        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.next
        print("None")
    
    #Display Backward
    def display_backward(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp=temp.prev
        
        print("None")

    #Insert at Beginning
    def insert_beginning(self,data):
        new_node=Node(data)

        if self.head:
            self.head.prev=new_node
            new_node.next=self.head
    
        self.head=new_node

    
    #Insert at End
    def insert_end(self,data):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return

        temp=self.head
        while temp.next: 
            temp=temp.next
        
        temp.next=new_node
        new_node.prev=temp
    
    #Insert at index
    def insert_index(self,data,index):
        new_node=Node(data)

        temp=self.head
        count=0

        while temp and count<index:
            temp=temp.next
            count +=1

        if temp is None:
            print("index out of range")
            return
        
        prev_node=temp.prev
        new_node.next=temp
        new_node.prev=prev_node

        if prev_node:
            prev_node.next=new_node
        
        temp.prev=new_node

        if index==0:
            self.head=new_node

    
  