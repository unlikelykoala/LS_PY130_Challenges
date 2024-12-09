class RomanNumeral:   
    NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    
    def __init__(self, decimal):
        self._decimal = decimal

    def to_roman(self):
        roman = ''
        current_decimal_value = self._decimal

        for key, value in RomanNumeral.NUMERALS.items():
            multiplier, remainder = divmod(current_decimal_value, value)
            # if multiplier > 0:
            #     roman += key * multiplier
            roman += key * multiplier
            current_decimal_value = remainder

        return roman
        


