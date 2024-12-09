'''
notes:
    - 

rules:
    - create SumOfMultiples class
        - methods:
            - constructor: takes list of ints
                -

            static method
            - sum_up_to(int): 
            
            isntance method
            - to(int): calculates SoM for each number in its list for multiples up to but not including the number

            important: for the numbers in the list, only allow them to multiply by each other once (other duplicates are allowed)

DS:
    - 

Alg:
    - problem:
        - numbers in the set are multiplying by each other twice; once in their respective iterations
        - i only want to add one of the products to the total
            - removing all dulicates doesn't work bc other numbers can be multipled to get some products
        - 

'''
class SumOfMultiples:
    def __init__(self, *args):
        self._set = args if args else (3, 5)

    def to(self, limit):
        multiples = set()

        for num in self._set:
            for multiplier in range(1, limit):
                product = multiplier * num
                if product < limit:
                    multiples.add(product)
                else:
                    break

        return sum(multiples)
    
    @classmethod
    def sum_up_to(cls, limit):
        return cls().to(limit)


if __name__ == '__main__':
    print(SumOfMultiples.sum_up_to(100))
    # print(SumOfMultiples(7, 13, 17).to(20))
