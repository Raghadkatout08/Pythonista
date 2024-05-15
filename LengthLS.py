class LengthLS:
    def __len__(self):
        current = self.head 
        count = 0 
        while current:
            count+=1
            current = current.next 
        return count