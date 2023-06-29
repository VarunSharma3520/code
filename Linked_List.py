class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.pre = None
    def create_from_end(self,data):
        new_data = Node(data)
        if self.pre is None:
            self.pre = new_data
        else: 
            temp = self.pre
            while temp.next:
                temp = temp.next
            temp.next = new_data
    def create_from_start(self,data):
        new_data = Node(data)
        temp = self.pre
        self.pre = new_data
        new_data.next = temp
        
    def read(self):
        temp = self.pre
        while temp is not None:
            print(temp.data)
            temp = temp.next
    def delete_from_starting(self):
        if self.pre is None:
            print("Empty")
        else:
            self.pre = self.pre.next
            self.read()
varun = Linked_List()
varun.create_from_end(10)
varun.create_from_end(20)
varun.create_from_end(30)
varun.create_from_end(40)
varun.create_from_end(50)
varun.create_from_end(60)
varun.create_from_end(70)
varun.create_from_end(80)
varun.create_from_end(90)
varun.create_from_end(100)
varun.create_from_start(0)
varun.read()
varun.delete_from_starting()
