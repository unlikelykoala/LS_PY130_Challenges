'''
notes:
    - string of digits and return all possible consecutive numbers series ofa  specified length
    - examples:
        - 01234
            - 3-digit series:   
                - 012
                - 123
                - 234
            - 4-digit series:
                - 01234
                - 1234

            - if ask for 6 digit series from 5 digit string, raise value error

rules:
    - Series class:
        - constructor:
            - takes 1 arg: numeric string
                - always numeric, don't worry about errors
        - slices(int): 
            - returns list of lists of consecutive number series
            - if just  input is 1, then all numbers are considered consecutive
            - raises ValueError if slice length is greater than length of the series

DS:
    - list of numeric string
    - list of lists of numeric strings

Alg:
    - throw error if length > slice length
    - init output list to hold list to []
    - iterate thru slice_string:
        - if there are enough chars remaining from the current index,
            - init current list to []
            - append series the length of input to current list
            - append current list to output list
        - else: break
    
    - return output list


'''
class Series:
    def __init__(self, _slice_string):
        self._slice_string = _slice_string

    def slices(self, length):
        slice_length = len(self._slice_string)
        if length > slice_length:
            raise ValueError('Input must be less than the length of the slice string')
        
        result = []

        for idx in range(slice_length):
            if idx + length <= slice_length:
                current = [int(digit) for digit in self._slice_string[idx:idx+length]]
                result.append(current)
            else:
                break
        
        return result


if __name__ == '__main__':
    print(Series('1234').slices(1))
