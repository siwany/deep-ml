def slope(x):
  return 4*x**3 - 9*x**2
def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    # f_prime = 4x^3 - 9x^2
    lr = 0.002
    x = start_x
    if x <= 0:
      x = 0.1
    for _ in range(10000):
      if abs(slope(x)) < 0.00001:
        break
      x = x - lr * slope(x)

    return x
