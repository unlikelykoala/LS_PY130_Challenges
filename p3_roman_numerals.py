'''
notes:
    - convert modern decmimal nums to roman equibvalents
    - I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    - subtraction rule: 4s and 9s, place a 1 (or 10 or etc.) in front of the V or X or C etc.



rules:
    - create a RomanNumeral class
        - iv's:
            - decimal int (no floats)

        - methods:
            - to_roman():
                - converts to roman numeral

    - limits: from 1 to 3000

DS:
    - maybe string to iterate thru

Alg;
    - constructor:
        - iv: decimal
    - method:
        - convert decimal to string 
        - set get length of string
        - iterate thru each num_char:
            - convert
'''
class RomanNumeral:   
    NUMERALS = (
        {num: 'I' * num for num in [1, 2, 3]} | {5: 'V'} | {4: 'IV'}
        | {num: 'V' + 'I' * (num-5) for num in [6, 7, 8]} | {9: 'IX'}
        | {num*10: 'X' * num for num in [1, 2, 3]} | {50:'L'} | {40: 'XL'}
        | {num*10: 'L' + 'X' * (num-5) for num in [6, 7, 8]} | {90: 'XC'}
        | {num*100: 'C' * num for num in [1, 2, 3]} | {500:'D'} | {400: 'CD'}
        | {num*100: 'D' + 'C' * (num-5) for num in [6, 7, 8]} | {900: 'CM'}
        | {num*1000: 'M' * num for num in [1, 2, 3]}
        | {0: ''}
    )
    
    def __init__(self, decimal):
        self._decimal = decimal

    def to_roman(self):
        roman = ''
        num_str = str(self._decimal)
        zeros = len(num_str) - 1

        for digit in num_str:
            place_value = digit + '0' * zeros
            roman += RomanNumeral.NUMERALS[int(place_value)]
            zeros -= 1

        return roman





