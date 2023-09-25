"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def has_factor_in_list(num, list):
    for numbers in list:
        if num % numbers == 0:
            return False
        
    return True



def primes(number_of_primes):
    list = [2]

    if number_of_primes <= 0:
        raise ValueError
    
    num = 3
    while len(list) != number_of_primes:
        if has_factor_in_list(num, list):
            list.append(num)

        num += 1

    return list


print(primes(10))


