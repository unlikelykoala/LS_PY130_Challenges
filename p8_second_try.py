class SumOfMultiples:
    def __init__(self, *factors):
        self.factors = factors if factors else (3, 5)

    def to(self, limit):
        return sum(multiple for multiple in range(1, limit) if self._any_factors(multiple))

    @classmethod
    def sum_up_to(cls, limit):
        return cls().to(limit)

    def _any_factors(self, multiple):
        return any(multiple % factor == 0 for factor in self.factors)

if __name__ == '__main__':
    print(SumOfMultiples.sum_up_to(100))
    # print(SumOfMultiples(7, 13, 17).to(20))
