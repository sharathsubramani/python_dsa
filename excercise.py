class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, self.head)

    def print(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        itr = self.head
        llstr = ''
        len = 0
        while itr:
            nextitr = itr.next
            print(nextitr)
                


        #     llstr += str(itr.data) + '--->'
        #     itr  = itr.next
        #     if(self.head.next is None):
        #         print("Last node")
        #     len += 1
        # print(llstr)
        # print(len)

    

if __name__ == '__main__':
    ll = LinkedList()
    for i in range(20):
        ll.insert_at_beginning(i)
    ll.print()
