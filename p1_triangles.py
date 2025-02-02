'''
input: 3 ints 
output: string (type of triangle)

rules:
    - all triangles: 
        - all sides must be > 0
        - sum of lengths of any 2 sides must be greater than the 3rd side 
    - equilateral: all 3 sides have same length
    - isosceles: exactly 2 sides have same length 
    - scalene: all sides have different lengths

    - build a Triangle class with:
        - 3 sides input via the constructor
            - floats are ok
        - exception is raised if side <= 0, or sum of 2 sides is <= 3rd side

    - kind method that returns a string representing the type of the triangle

DS:
    - 

Alg:
    - 

'''
class Triangle:
    def __init__(self, s1, s2, s3):
        self._sides = (s1, s2, s3)
        self._validate_triangle()
    
    @property
    def kind(self):
        def is_equilateral():
            return len(set(self._sides)) == 1
        
        def is_scalene():
            return len(set(self._sides)) == 3
        
        if is_equilateral():
            return 'equilateral'
        
        if is_scalene():
            return 'scalene'
        
        return 'isosceles'
    
    def _validate_triangle(self):
        def validate_sides():
            for side in self._sides:
                if type(side) not in [int, float]:
                    raise TypeError("Sides must be numbers")
                if side <= 0:
                    raise ValueError('Sides must be greater than 0')
                
        def validate_side_combo():
            for side in self._sides:
                without_side = list(self._sides)
                without_side.remove(side)
                if side >= sum(without_side):
                    raise ValueError('Sum of any 2 sides should be greater than 3rd side')
        
        validate_sides()
        validate_side_combo()
