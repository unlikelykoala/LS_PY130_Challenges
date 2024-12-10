'''
notes:
    - singly linked list: each element contains data and a next filed pointing to the next element
        - LIFO: push-down stacks (last in firs out)
    - elements can contain a range of data

rules:
    - class Element:
        - constructor(datum):
            - self._datum

        property
        - datum

        -is_tail():
            - returns bool

        property
        - next
            - returns None if nothing next (is_tail) or pointer to next element
    
    - class SimplyLinkedList:
        - constructor:
            - self._size = 0

        property
        - size
            - returns length of list

        property
        - head
            - returns the first element in the list or None if no element

        - is_empty():
            - returns bool

        - pop()
            - removes last item

        -push(element):
            - add element to list
            - the element is the data, and we have to convert the data into an element

        - peek():
            - returns value of first element??? or None if nothing
            - seems to return the datum value, not full element object

        - reverse():
            - 

        - to_list()
            - returns empty list if no elements

        classmethod
        - from_list(list):
            - 

DS:
    - 

Alg:
    - POP
        - remove item from the _list var
        - set the new last item's next var to None

'''
import copy 


class Element:
    def __init__(self, datum, next=None):
        self._datum = datum
        self._next = next

    @property
    def datum(self):
        return self._datum
    
    @property
    def next(self):
        return self._next
    
    def is_tail(self):
        return not self.next
    
    def __str__(self):
        return f'{self.datum}'

class SimpleLinkedList:
    def __init__(self):
        self._list = []

    @property
    def head(self):
        return self._list[-1] if self._list else None
    
    @property
    def size(self):
        return len(self._list)
    
    def is_empty(self):
        return not self._list
    
    def peek(self):
        return self.head.datum if self.head else None
    
    def pop(self):
        return self._list.pop().datum

    def push(self, datum):
        if self.is_empty():
            element = Element(datum)
        else:
            element = Element(datum, self._list[-1])

        self._list.append(element)

    def reverse(self):
        new = SimpleLinkedList()

        for element in self._list[::-1]:
            new.push(element.datum)

        return new
    
    def to_list(self):
        return [element.datum for element in self._list[::-1]]
    
    @classmethod
    def from_list(cls, lst):
        new_list = SimpleLinkedList()

        if lst:
            for item in lst[::-1]:
                new_list.push(item)

        return new_list
    
    def __str__(self):
        data = [str(element) for element in self._list]

        return '\n'.join(data)



if __name__ == '__main__':
    a = SimpleLinkedList.from_list([1, 2])
    print(a)
