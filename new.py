class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_links(self, data):
        new_node = Node(data, self.head)
        # print(new_node.next)
        self.head = new_node
        # print(new_node.data)

    
    def print(self):
        itr = self.head
        llstr = ''
        
        if self.head:
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            return print(llstr)
        else:
            print("linked list is empty")


if __name__ == '__main__':
    linkedList = LinkedList()
    # linkedList.insert_links(4)

    # linkedList.insert_links(5)
    for i in range(10):
        linkedList.insert_links(i)
    
    linkedList.print()