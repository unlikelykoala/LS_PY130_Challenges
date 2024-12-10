'''
notes:
    - generate random robot names

rules:
    - do not allow repeated names 
        - class variable of existing robot names
    
    - class Name:
        class variable
        - list of existing robot names

        - constructor:
            - no args
            - automatically generate random name
        
        - name property:
            - returns current robot name
        
        - reset():
            - resets the robot name

DS:
    - list of robot names

Alg:
    - 

'''
import random


class Robot:
    NAME_LETTERS = 2
    NAME_DIGITS = 3
    NAMES = []

    def __init__(self):
        self._name = None
        self.reset()

    @property
    def name(self):
        return self._name
    
    def reset(self):
        if self.name:
            self.__class__._deregister_name(self.name)

        self._name = self._generate_name()
        self.__class__._register_name(self.name)

    def _generate_name(self):
        ALPHABET = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
        DIGITS = '0123456789'

        while True:
            name = ''.join(
                [random.choice(ALPHABET) for _ in range(self.__class__.NAME_LETTERS)] 
                + [random.choice(DIGITS) for _ in range(self.__class__.NAME_DIGITS)]
            )
            if name not in self.__class__.NAMES:
                return name

    @classmethod
    def _register_name(cls, name):
        cls.NAMES.append(name)

    @classmethod
    def _deregister_name(cls, name):
        cls.NAMES.remove(name)


if __name__ == '__main__':
    print(Robot().name)
