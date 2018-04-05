import math

def central_binomial_coefficient(square_grid_side):

     return math.factorial((2 * square_grid_side)) / math.pow( math.factorial(square_grid_side), 2)

print(central_binomial_coefficient(20))