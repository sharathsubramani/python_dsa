class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        pass

    def insert_links(self,data):
        new_node = Node(data,self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print("Linked is Empty.!")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
        
        print(llstr,'linked list string')



# def insert_at_begin(self,data):
#     new_node = Node(data)
#     if self.head is None:
#         self.head = new_node
#         return 
#     else:
#         new_node.next = self.head
#         self.head = new_node
#     print(new_node)


# class LinkedList():
#     def __init__(self):
#         self.head = None


def insert_numbers_linkedlist():
    x = range(20)
    linked_list = LinkedList()
    for i in x:
        linked_list.insert_links(i)
        break
    linked_list.print()

if __name__ == '__main__':

    insert_numbers_linkedlist()

    # node =Node(4)
    # print(node.data)
    # node.next = Node(5)
    # print(node.next.data)
    # node.next.next = Node(6)
    # print(node.next.next.data)

