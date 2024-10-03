# rows = 3
# cols = 3
# twod_arr = [rows for rows in range(3)]
# print(twod_arr)


# class Node:
#     def __init__(self,data =None, next =None):
#         self.data = data
#         self.next = next


# def get_length_of_linked_list(head):
#     length = 0

#     while head:
#         length += 1
#         head = head.next

#     return length


# def main():
#     # Create a hard-coded linked list:
#     # 10 -> 20 -> 30 -> 40 -> 50 -> 60
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
#     head.next.next.next.next.next = Node(60)
#     print(head)


# if __name__ == '__main__':
#     main()
def search(myList, number):
    def search_recursive(lst, num):
        if lst[0] == num:
            print(lst[0])
            return 0
        return 1 + search_recursive(lst[1:], num)
    try:
        print(1 + search_recursive(myList, number))
        return search_recursive(myList, number)
    except IndexError:
        return -1


search([1, 2, 3, 4, 5], 6)
