# Pythonista

## Introduction
A linked list is a linear data structure consisting of nodes, where each node contains a data value and a reference to the next node in the sequence. Linked lists are dynamic and commonly used for memory efficiency.

## Usage
To use a linked list in Python, import the `LinkedList` class from `LinkedList.py` and the `Node` class from `Node.py`.

## Functionality

### LinkedList Class

#### Methods
- `append(value)`: Add a new node with the given value to the end of the linked list.
- `to_list()`: Convert the linked list into a Python list.
- `get_item(index)`: Get the value of the node at the specified index.
- `get_length()`: Get the length of the linked list.
- `stringls()`: Convert the linked list into a string representation.

### Testing
Unit tests are provided in the `test_linkedlist.py` file to ensure the functionality of the linked list implementation.

## File Structure

- `LinkedList.py`: Contains the implementation of the LinkedList class.
- `Node.py`: Defines the Node class used in the linked list.
- `test_linkedlist.py`: Unit tests for the linked list implementation.

## How to Run Tests

To run the tests, install pytest using the following command:
```pip install pytest```

Then, execute the tests by running:
```pytest```

