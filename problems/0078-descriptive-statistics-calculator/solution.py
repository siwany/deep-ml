import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean = np.mean(data)
    median = np.median(data)
    val, counts = np.unique(data, return_counts=True)
    mode = val[np.argmax(counts)]
    variance = np.var(data)
    stdev = np.std(data)
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'standard_deviation': stdev, '25th_percentile': np.percentile(data,25), '50th_percentile': np.percentile(data, 50), '75th_percentile': np.percentile(data,75), 'interquartile_range': np.percentile(data,75) - np.percentile(data,25)}