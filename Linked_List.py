# Node class to represent individual nodes in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class to manage the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Creating a linked list and adding elements
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Displaying the linked list
linked_list.display()
