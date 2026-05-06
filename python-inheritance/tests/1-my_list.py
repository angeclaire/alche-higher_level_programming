===========================
How to use 1-my_list module
===========================

Import MyList:
    >>> MyList = __import__('1-my_list').MyList

Test instantiation:
    >>> my_list = MyList()
    >>> type(my_list)
    <class '1-my_list.MyList'>

Test inherits from list:
    >>> issubclass(MyList, list)
    True
    >>> isinstance(my_list, list)
    True

Test __str__ on empty list:
    >>> my_list = MyList()
    >>> print(my_list)
    []

Test append():
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> print(my_list)
    [1]

Test print_sorted() with sorted append:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.print_sorted()
    [1, 2, 3]

Test print_sorted() with not sorted append:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]

Test print_sorted() with negative numbers:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(-5)
    >>> my_list.append(2)
    >>> my_list.append(-3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, -5, 2, -3, 5]
    >>> my_list.print_sorted()
    [-5, -3, 1, 2, 5]
    >>> print(my_list)
    [1, -5, 2, -3, 5]

Test print_sorted() with empty list:
    >>> my_list = MyList()
    >>> my_list.print_sorted()
    []

Test print_sorted() returns a new list (original unchanged):
    >>> my_list = MyList()
    >>> my_list.append(3)
    >>> my_list.append(1)
    >>> my_list.append(2)
    >>> my_list.print_sorted()
    [1, 2, 3]
    >>> print(my_list)
    [3, 1, 2]
