def format_big_number(num):
    """
    Formats a number into a readable string with suffixes (K, M, B).
    """
    if num is None:
        return "-"
    
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
        
    # Choose suffix based on magnitude
    suffix = ['', 'K', 'M', 'B', 'T'][magnitude]
    
    # Format to 1 or 2 decimal places depending on size
    return f"{num:.1f}{suffix}"
