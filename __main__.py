from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.display()  # Output: 1 -> 2 -> 3 -> None

    ll.delete(2)
    ll.display()  # Output: 1 -> 3 -> None
