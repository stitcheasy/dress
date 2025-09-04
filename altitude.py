import math
# b = 3
# h = 9.5

def calculate_altitude(base, hypotenuse):
    """Returns the altitude of a right-angled triangle."""
    if hypotenuse <= base:
        print("Error: Hypotenuse must be greater than the base.")
        return None

    try:
        return math.sqrt(hypotenuse**2 - base**2)
    except ValueError:
        print("Error: Invalid triangle dimensions.")
        return None
    
# alt=calculate_altitude(b, h)
# print(alt)

