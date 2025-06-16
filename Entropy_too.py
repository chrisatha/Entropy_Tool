import math
import sys
from collections import Counter

# Define the base for entropy calculations Normalized ripped from the chefofcybers
# I am convinced doing 
base = {
    'shannon': 2.,
    'natural': math.exp(1),
    'hartley': 10.,
    'somrand': 256.
}

def eta(data, unit):
    """Calculate the entropy of the given data using the specified file in all sorts of formats"""
    if len(data) <= 1:
        return 0
    counts = Counter()
    for d in data:
        counts[d] += 1
    ent = 0
    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])
    return ent

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        # Attempt to read the file in binary mode this is the way 
        with open(filename, 'rb') as file:
            data = file.read()
            # Decode using UTF-8, fallback to ISO-8859-1 if it fails cause ISO ya know
            try:
                data = data.decode('utf-8')
            except UnicodeDecodeError:
                data = data.decode('ISO-8859-1')  # Fallback encoding
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading '{filename}': {e}")
        sys.exit(1)

    print("=======================================================================================================")
    print("Entropy Calculation for file:", filename)
    print("=======================================================================================================")
    print(f"{'Base':<10}{'Entropy':>15}")
    print("-------------------------------------------------------------------------------------------------------")

    for unit in base:
        entropy_value = eta(data, unit)
        print(f"{unit.capitalize():<10}{entropy_value:>15.6f}")

if __name__ == "__main__":
    main()
