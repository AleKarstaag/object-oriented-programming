def gcd(a, b):
    """Return the greatest common divisor of a and b using a recursive
    implementation of Euclid's algorithm."""
    try: #keep calling gcd on smaller and smaller values of b
        return gcd(b, a % b)
    except ZeroDivisionError: #untill we get to the point that b is zero
        #this line will get an exception and we return a
        return a
