from Node import Node 
from GetItem import GetItem
from LengthLS import LengthLS
from StringList import StringList

class Linkedlist(GetItem, LengthLS):
    def __init__(self): 
        """Initialize a new instance of the LinkedList class."""
        self.head = None 
    
    
    """ Append a new node with the given value to the end of the linked list. """
    def append(self, value):
        node = Node(value)

        ''' if LinkedList is Empty '''
        if self.head is None:
            self.head = node 
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        return self.to_list()
             
    
    """ Convert the linked list into a Python list. """
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    """ (__getitem__) Retrieve the value at the specified index using [] operator. """
    def get_item(self, index):
        return self.__getitem__(index)
    

    """ (__len__) Get the length of the linked list. """
    def get_length(self):
        return len(self)
    
    
    """ (__str__) Convert the linked list to a string. """
    def stringls(self):
        return str(StringList(self))