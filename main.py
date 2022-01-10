import math
from math import sqrt

def tavolsag_n_d(*nums):
    return math.sqrt( sum( [ num ** 2 for num in nums] ))
    
print(tavolsag_n_d(1,2,3,5,6,14))
