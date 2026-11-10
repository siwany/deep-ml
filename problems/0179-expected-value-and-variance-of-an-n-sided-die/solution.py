def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Your code here
    sum = 0
    for i in range(1, n+1):
        sum += i
    mean = sum / n

    sum_var = 0
    for i in range(1, n+1):
        sum_var += (i-mean)**2
    var = sum_var / n
    return (mean, var)