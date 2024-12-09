'''
notes:
    - octal to decimal conversion
    - input: octal string
    - output: decimal int
    
rules:
    - crate Octal class
        - constructor: 1 arg: the octal string

        - to_decimal(self): converts the octal string to a decimal int

DS:
    - reversed string

Alg:
    - init total to 0
    - init power to 0
    - reverse the octal string
    - itertate thru reversed string (think about it like moving left to right)
        - change digit to int
        - multiply digit by 8**power
        - add product to total

    - return total

'''
class Octal:
    def __init__(self, octal):
        self._octal = octal

    def to_decimal(self):
        total = 0

        if not Octal._valid_octal(self._octal):
            return total
        
        power = 0
        reverse_octal = self._octal[::-1]

        for digit in reverse_octal:
            digit = int(digit)
            product = digit * 8**power
            total += product
            power += 1

        return total
    
    @staticmethod
    def _valid_octal(octal):
        return all(char.isdigit() and "0" <= char <= "7" for char in octal)

if __name__ == '__main__':
    print(Octal('77').to_decimal())
