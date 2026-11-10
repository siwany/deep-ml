from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counter = Counter(samples)
    pmf = [(item, count/len(samples)) for item, count in counter.items()]
    return pmf
    