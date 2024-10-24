def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        num = float(numerator)
        den = float(denominator)
        return num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

