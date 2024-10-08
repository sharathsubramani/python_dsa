# insert node

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_node_at_begining(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def print(self):
        itr = self.head
        llstr = ''
        counter = 0
        if self.head:
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
                counter = counter+1
            print(counter)
            # print(counter)
            print(llstr)

    def insert_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        curr = self.head
        print(curr)
        while curr.next is not None:
            curr = curr.next
        curr.next = temp
        
    def get_length_ll(self):
        itr = self.head
        counter = 0
        if self.head:
            while itr:
                itr = itr.next
                counter += 1
            print(counter)


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(1, 21):
        linked_list.insert_at_end(i)
        # linked_list.insert_at_end(2)

    linked_list.print()
    linked_list.get_length_ll()


# temp = Node(data)
#             if self.head is None:
#                 self.head = temp
#                 return
#             curr = self.head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = temp
