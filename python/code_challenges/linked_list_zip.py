from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    if a.head:
        cur = start = a.head
        a.head = a.head.next
    else:
        return LinkedList(b.head)
    while a.head and b.head:
        cur.next = b.head
        b.head = b.head.next
        cur = cur.next
        cur.next = a.head
        a.head = a.head.next
        cur = cur.next
    cur.next = a.head or b.head

    # use the "start" pointer to initiate
    return LinkedList(start)
