def classify(n):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if n <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    total = 0
    
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    if total == n:
        return str('perfect')
    elif total > n:
        return str('abundant')
    elif total < n:
        return str('deficient')
