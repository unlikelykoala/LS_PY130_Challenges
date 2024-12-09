'''
notes:
    - categories:
        - abundant
            - AQ sum > original number
        - perfect
            - AQ sum is == original number
        - deficient
            - AQ sum < original number
    - based on comparing the number and the sum of its positive divisors
    - Aliquot sum: sum of the positive divisors of a number (does not inlcude number itself)

rules:
    - input: number
    - output: classify the number
    
    - make a PerfectNumber class
        - don't create isntances
        
        - classmethod: classify(number)
            - if not positive, raise ValueError

DS:
    - maybe list to hold divisors

Alg:
    - init total to 0
    - iterate from 1 to squareroot of num
        - if divisor, add num to total

    - if total > num: abundant
    - if < num: deficient
    else: perfect

'''
class PerfectNumber:
    @classmethod
    def classify(cls, number):
        if not cls._valid_number(number):
            raise ValueError("Input must be a positive integer")
        
        total = 0

        for divisor in range(1, ((number // 2) + 1)):
            if number % divisor == 0:
                total += divisor

        return cls._match_type(number, total)

    @classmethod
    def _match_type(cls, number, total):
        if total > number:
            return 'abundant'
        
        if total < number:
            return 'deficient'
        
        return 'perfect'
    
    @classmethod
    def _valid_number(cls, number):
        return number > 0


if __name__ == '__main__':
    print(PerfectNumber.classify(-1))
