class StringList: 
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def __str__(self):
        """Convert the linked list to a string representation."""
        result = []
        current = self.linked_list.head
        while current:
            result.append(str(current.value))
            current = current.next 
        return ' ->'.join(result) if result else 'Empty Linked List'
        