class Node:
    def_init_(self, data):
    self.data = data
    self.next : None

    class LinkedList:
        def_init_(self):
        self.head = None
         def append(self, data):
             new_node = Node(data)
             if self.head is None:
                 self.head = new_node
                 return
             last_node = sel.head
             while last_node.next:
                 last_node = last_node.next
             last_node.next = new_node