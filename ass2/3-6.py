def to_base(num, b):
    """Convert integer to a specified base as a string."""
    if not (2 <= b <= 10):
        raise ValueError("Base must be between 2 and 10")
    result = ""
    while num > 0:
        result = str(num % b) + result
        num //= b
    return result or "0"

def sum_digits(s, b):
    """Sum the digits in a base-represented string and convert sum back to the base."""
    return to_base(sum(int(d) for d in s), b)

def reduce_digit(num, b):
    """Continuously sum digits until a single digit is obtained, track frequency of digits."""
    freq = {str(x): 0 for x in range(b)}
    num_str = to_base(num, b)
    path = [num_str]

    while len(num_str) > 1:
        for d in num_str:
            freq[d] += 1
        num_str = sum_digits(num_str, b)
        path.append(num_str)

    freq[num_str] += 1
    return num_str, freq, path

def check_tasty(freq):
    """Check if all digit frequencies are equal."""
    f = list(freq.values())
    return len(set(f)) == 1

def display_path(num, b, path):
    """Display the reduction path for a tasty number."""
    print(" -> ".join(path))

def find_tasty(b, count):
    """Find 'count' tasty numbers in base 'b'."""
    found = 0
    n = 1
    while found < count:
        sd, freq, p = reduce_digit(n, b)
        if check_tasty(freq):
            display_path(n, b, p)
            found += 1
        n += 1

# finds first 10 tasty numbers
for base in range(2, 11):
    print(f"Base {base}:")
    find_tasty(base, 10)
