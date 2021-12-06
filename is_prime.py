from modulo.divisible import div

def is_prime(x: int) -> bool:
    """
    Returns true if x is prime, false otherwise.
    """
    if x > 1:
        for i in range(2, int(x/2)+1):
            if div(x, i):
                return False
        return True
    
    return False


# def is_prime(x: int) -> bool:
#     """
#     Returns true if x is prime, false otherwise.
#     """
#     if x > 1:
#         for i in range(2, int(x/2)):
#             if (x % i) == 0:
#                 return False
#         return True
    
#     return False