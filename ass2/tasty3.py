def digit_sum(n, base):
    """Calculate the sum of digits of n in the given base."""
    sum_digits = 0
    while n > 0:
        sum_digits += n % base
        n //= base
    return sum_digits

def projection(n, base):
    """Compute the projection of n in the given base."""
    while n >= base:
        n = digit_sum(n, base)
    return n

def is_tasty(n, base):
    """Check if n is a tasty number in the given base."""
    coefficients = [0] * base
    while n >= base:
        n = digit_sum(n, base)
        if n < base:
            coefficients[n] += 1
    coefficients[n] += 1
    
    # Check if all coefficients appear at least once and the same number of times
    min_count = min(coefficients)
    max_count = max(coefficients)
    return min_count > 0 and min_count == max_count

def find_tasty_numbers(base, count=10):
    """Find the first count tasty numbers in the given base."""
    tasty_numbers = []
    n = 1
    while len(tasty_numbers) < count:
        if is_tasty(n, base):
            tasty_numbers.append(n)
        n += 1
    return tasty_numbers

def main():
    for base in range(2, 11):
        print(f"Base {base}:")
        tasty_numbers = find_tasty_numbers(base)
        for number in tasty_numbers:
            proj = projection(number, base)
            print(f"{number} -> {proj}")
        print()

if __name__ == "__main__":
    main()