'''
A, E, I, O, U, L, N, R, S, T	1
D, G	2
B, C, M, P	3
F, H, V, W, Y	4
K	5
J, X	8
Q, Z	10

notes:
    - given a word, compute its scrabble score

rules:
    - create a Scrabble class:
        - constructor:
            - 1 argument: string (can be empty) or None
        
        - score(self):
            - returns the score of self._word
            - can be '' or None
            - have to account for whitespace chars: \t anmd \n
            - not testing if it's an actual word
            - case insensitive

        - calculate_score(self, word):
            - returns the score of the argument word, not self._word
            - same as score

DS:
    - dict of tile scores

Alg:
    - total = 0
    - remove whitespace chars
    - if not word, return total
    - make all chars upper (bc dict is upper)
    - iterate thru remaining chars
        - access their score from dict and sum scores
    - return total
'''
import re


class Scrabble:
    SCORES = (
        {letter: 1 for letter in 'AEIOULNRST'}
        | {letter: 2 for letter in 'DG'}
        | {letter: 3 for letter in 'BCMP'}
        | {letter: 4 for letter in 'FHVWY'}
        | {'K': 5}
        | {letter: 8 for letter in 'JX'}
        | {letter: 10 for letter in 'QZ'}
    )
    
    def __init__(self, word):
        self._word = word

    def score(self):
        total = 0

        if not self._word:
            return total

        no_ws = re.sub(r'[\s]', '', self._word)
        
        no_ws_upper = no_ws.upper()

        for char in no_ws_upper:
            total += Scrabble.SCORES[char]

        return total

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()



if __name__ == '__main__':
    a = Scrabble('hey')
    print(a.calculate_score('he\nllo'))
