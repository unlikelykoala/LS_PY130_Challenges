'''
notes:
    - all elements must be numbers
    - all unique values
    - ME: don't use built-in sets

rules:
    - 
    
    - class Name:
        - constructor:
            - doesn't need args
        
        - is_empty():
            - return bool

        - contains(int)
            - returns bool of whether int in set

        - is_subset(CustomSet)
            - returns bool
            - checks if calling set contained within CustomSet
            - not strict, so identical set is subset

        - is_disjoint(CustomSet)
            - returns bool
            - True if nothing in common
            - True if both emopty?!

        - is_same(CustomSet)
            - returns bool
            - checks if sets are same
            - order doesn't matter

        - add(self, element)

        - intersection(CustomSet)"
            - returns custome set with all shared elements
            - empty if nothing in common

        - difference(custom set):
            - returns new CS with all elements in  the CALLING set and NOT in other set

        - union(CS):
            - returns CS with all elements from each
        
        - __eq__(self, other)



DS:
    - 

Alg:
    - 

'''
class CustomSet:
    def __init__(self, seq=None):
        self._set = []
        if seq:
            self._add_list(seq)

    def contains(self, element):
        return element in self._set
    
    def add(self, element):
        if self._no_duplicates(element):
            self._set.append(element)
        
        return self
    
    def difference(self, other):
        diff = [element for element in self._set
                if element not in other._set]
        
        return CustomSet(diff)
    
    def intersection(self, other):
        shared = [element for element in self._set + other._set
                  if element in self._set
                  and element in other._set]
        
        return CustomSet(shared)
    
    def is_empty(self):
        return not self._set
    
    def is_disjoint(self, other_set):
        return all(element not in other_set._set for element in self._set)
    
    def is_same(self, other):
        return self == other
    
    def is_subset(self, other_set):
        return all(element in other_set._set for element in self._set)
    
    def union(self, other):
        every = [element for element in self._set + other._set]

        return CustomSet(every)
    
    def _add_list(self, seq):
        self._set += ( [self._no_duplicates(element) for element in seq])

    def _no_duplicates(self, element):
        if element not in self._set:
            return element
        
    def __eq__(self, other):
        return (
            self.is_subset(other)
            and other.is_subset(self)
        )
    
    def __str__(self):
        return f'{self._set}'


if __name__ == '__main__':
    print(CustomSet([2, 1]).is_same(CustomSet([1, 2])))
