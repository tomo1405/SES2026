import math
from sympy import isprime
def task_func(input_list):
    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    return sorted_primes