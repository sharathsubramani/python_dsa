class Node():
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begining(self,head,data):
        new_node = Node(data)
        new_node.next = head
        if self.head:
            new_node.prev = new_node
        return new_node

        # new_node = Node()
