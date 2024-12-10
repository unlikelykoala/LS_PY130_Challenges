'''
notes:
    - input: one letter
    - output: diamond shape with A at top, each level down moves to next letter
    - all capitals

rules:
    - top and bottom have one letter, A
    - middle row uses input letter then goes back to A as it goes to bottom
    - all capitals
    - horizontally symmetric
    - square: width == height
    - A input outputs A\n
    - \n after EVERY line, including last
    - must include spaces on the RIGHT side of each char as well as left
    
    - class Diamond:
        - class constant ABCs string
        - constructor:
            - none
        
        - make_diamond(cls, letter): returns the diamond string
            - 

DS:
    - string of alphabet
    - string for each line
    - list of strings for each line
        - to be joined by '' empty string
    - join result list to result string

Alg:
    - init spaces to index of middle letter
    - init result list to []
    - iterate thru alphabet until current letter == input letter:
        - concat space * spaces + letter + space * spaces + \n
        - append line to result list
        - decrement spaces by 1
        - if current letter == middle letter: break from loop
    - append the top half, minus the middle, to the bottom half of the diamon
        - create a slice of current list except for last element, and then reverse it.
        - append that to the result list
    - join result list with ''
    - return the diamond string

'''
class Diamond:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def make_diamond(cls, middle_letter):
        result = cls._build_top_half(middle_letter)
        result += cls._build_bottom_half(result)

        return ''.join(result)

    @classmethod
    def _build_top_half(cls, middle_letter):
        outer_spaces = cls.ALPHABET.index(middle_letter)
        inner_spaces = 1
        top_half = []

        for letter in cls.ALPHABET:
            if letter == 'A':
                line = ' ' * outer_spaces + letter + ' ' * outer_spaces + '\n'
            else:
                line = ' ' * outer_spaces + letter + ' ' * inner_spaces + letter + ' ' * outer_spaces + '\n'
                inner_spaces += 2

            top_half.append(line)
            outer_spaces -= 1

            if letter == middle_letter:
                return top_half
            
    @classmethod
    def _build_bottom_half(cls, top_half):
        return top_half[:-1][::-1]


if __name__ == '__main__':
    print(Diamond.make_diamond('C'))
