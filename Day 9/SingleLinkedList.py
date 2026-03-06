class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_name=Node(data)
        if not self.head:
            self.head=new_name
            return
        last_node=self.head

        while last_node.next :
            last_node=last_node.next

        last_node.next=new_name

    def display(self):
        curr=self.head

        while curr :
            print("curr.data ",curr.data, "  " "curr.next ", curr.next.data)
            print(curr.data, end=" -> ")
            curr=curr.next
        print("None")     # The end of the chain
    
list1=LinkedList()
list1.append(10)
list1.append(20)
list1.append("Apple")

list1.display()