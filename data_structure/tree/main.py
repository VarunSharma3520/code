class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


class Tree:
    def __init__(self, data=None):
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None

    def search_element(self, search_data):
        if self.root is None:
            return
        elif self.root.data == search_data:
            print(search_data)
            return self.root
        else:
            for child in self.root.children:
                self.search_element(search_data)

    def add_child(self, data, parent=None):
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        if self.root is not None and parent is None:
            self.root.children.append(node)
            return

        # checking whether parent is data or refernce
        if isinstance(parent, Node):
            if self.root == parent:
                self.root = node
                return
            
            for child in self.root.children:
                if child == parent:
                    child.children.append(node)
                    return
                self.add_child(parent)
        
        if self.root == parent:
            self.root = node
            return
        for child in self.root.children:
            if child.data == parent:
                print(child.data)
                child.children.append(node)
                return
            self.add_child(parent)

    def show_tree(self, node=None):
        if node is None:
            print(self.root.data)
        else:
            print(node.data)
            return
        for child in self.root.children:
            self.show_tree(child)


tree = Tree(10)
tree.add_child(20)
tree.add_child(30)
tree.add_child(80, 20)
# tree.search_element(10)
tree.show_tree()
