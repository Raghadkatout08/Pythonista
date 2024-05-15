class GetItem:
    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")

        current_val = self.head
        for _ in range(index):
            if current_val is None:
                raise IndexError("Index out of range")
            current_val = current_val.next
    
        if current_val is None:
            raise IndexError("Index out of range")

        return current_val.value