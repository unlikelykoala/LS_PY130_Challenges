'''
notes:
    - anagrams: contain same number of each letter

input: list of strings
output: sublist of strings that are anagrams for current word

rules:
    - create Anagram class
        - constructor: 
            - 1 string: target word
        
        - methods:
            - match:
                - input: list of strings
                - output: sublist of matching anagrams
                - emopty list if no matches
                - must be exact anagram, not simply contained within
                - case insensitive

DS:
    - outputs list of anagrams

Alg:
    - match:
        - make target word lowercase
        - sort loewr target word
        - iterate thru input list
            - make new word loercase
            - compare sorted new word and sorted target word
            - if same, add to output list
        - identical words are not anagrams (reagardless of case)
        - return output list
'''
class Anagram:
    def __init__(self, target):
        self._target = target

    def match(self, words):
        return [word for word in words if self._validate_word(word)]
    
    def _validate_word(self, word):
        low_target = self._target.casefold()
        sorted_low_target = sorted(low_target)

        return low_target != word.casefold() and sorted_low_target == sorted(word.casefold())



if __name__ == '__main__':
    a = Anagram('goodbye')
    print(a.match(['hey', 'hello', 'byegood']))
