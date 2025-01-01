def hasCycle(self, head: []):
    fast_pointer = head
    slow_pointer = head

    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        listLen = 0

        if fast_pointer == slow_pointer:
            print(listLen)


hasCycle([3,2,0,-4])

        