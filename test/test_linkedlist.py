from LinkedList import Linkedlist, Node 


""" Test the append method of the LinkedList class. """
def test_append():
    ls = Linkedlist()
    actual = ls.append(1)
    expected = [1]
    assert actual == expected

    actual = ls.append(2)
    expected = [1, 2]
    assert actual == expected

    actual = ls.append(3)
    expected = [1, 2, 3]
    assert actual == expected



""" Test the __getitem__ method of the LinkedList class. """
def test_getitem():
    ls = Linkedlist()

    ls.head = Node(1)
    ls.head.next = Node(2)
    ls.head.next.next = Node(3)

    actual_value_1 = ls.__getitem__(0)
    expected_value_1 = 1
    assert actual_value_1 == expected_value_1

    actual_value_2 = ls.__getitem__(1)
    expected_value_2 = 2
    assert actual_value_2 == expected_value_2

    actual_value_3 = ls.__getitem__(2)
    expected_value_3 = 3
    assert actual_value_3 == expected_value_3

    try:
        ls.__getitem__(3)
    except IndexError as e:
        actual_exception = str(e)
        expected_exception = "Index out of range"
        assert actual_exception == expected_exception



""" Test the __len__ method of the LinkedList class. """
def test_length():
    ls = Linkedlist()
    ls.append(1)
    ls.append(2)
    ls.append(3)

    actual = len(ls)
    expected = 3 
    assert actual == expected  



""" Test the __len__ method of an empty LinkedList. """
def test_empty_list_length():
    ls = Linkedlist()

    actual = len(ls)
    expected = 0 
    assert actual == expected  


""" Test the __str__ method of the LinkedList class. """
def test_str():
    ls = Linkedlist()
    ls.append(1)
    ls.append(2)
    ls.append(3)

    actual = ' -> '.join(map(str, ls.to_list()))
    expected = "1 -> 2 -> 3"
    assert actual == expected

    ls_empty = Linkedlist()
    actual = ls_empty.stringls()
    expected = "Empty Linked List"
    assert actual == expected


