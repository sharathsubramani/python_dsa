class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_node_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def s_print(self):
        if self.head is None:
            print("Linked is Empty.!")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def delete_node_from_begining(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_node_from_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        while temp.next is not None:
            prenode = temp
            temp = temp.next
        prenode.next = None
        del temp
        # print(prenode.data,prenode.next,'prenode')

    # def delete_node_from_pos(self):

    def get_length_linkedlist(self):
        temp = self.head
        if self.head is None:
            print("linked list is empty!")
        count = 0

        while temp:
            count += 1
            temp = temp.next
        print('length of linked list is: ' , count)
        return count


if __name__ == '__main__':
    linkedlist = LinkedList()
    for i in range(1, 21):
        linkedlist.insert_node_at_begining(i)
    # linkedlist.get_length_linkedlist()
    # linkedlist.insert_node_at_begining(4)
    # linkedlist.insert_node_at_begining(5)
    # linkedlist.s_print()
    # linkedlist.delete_node_from_begining()
    # linkedlist.delete_node_from_end()
    linkedlist.s_print()
    linkedlist.get_length_linkedlist()
