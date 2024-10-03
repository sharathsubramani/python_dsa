# def initialize_twod_array():
#     twod_list = []
#     new = []
#     for i in range(3):
#         new.append(0)
#         for j in range(1):
#             twod_list.append(new)
#     new =[]
#     print(twod_list)
#     print(new)


# initialize_twod_array()

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        newnode = Node(data, self.head)
        self.head = newnode
        # self.head = node

    def print(self):
        if self.head is None:
            print("Linked is Empty.!")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)


x = range(20)


def insert_numbers_linkedlist():
    linked_list = LinkedList()
    for i in x:
        linked_list.insert_at_begining(i)
    linked_list.print()


if __name__ == '__main__':
    insert_numbers_linkedlist()
    ll = LinkedList()
    # print(ll)
    # ll.insert_at_begining(5)


# import re

# # Given an array A[] of n numbers and another number x,
# # the task is to check whether or not there exist two elements in A[] whose sum is exactly x.

# # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# # (green, *tropic, red) = fruits

# # print(green)
# # print(tropic)
# # print(red)

# # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# # (green, *tropic, red) = fruits

# # print(green)
# # print(tropic)
# # print(red)

# # print('\tHello \tWorld')

# # alphabetPattern = re.compile(r'abc')

# num = [1,10,10,10,10]


# # def sum(num):
# #     x = 0
# #     for i in num:
# #       x += i
# #     return x
# # sum(num)
# # print(sum(num))


# def multiply(list):
#     x = 1
#     for i in list:
#         x *= i
#     return x

# print(multiply(num))
