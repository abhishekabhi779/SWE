def digit_sum(n, base):
    """Calculates the sum of the digits of n in the specified base."""
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total

def projection(n, base):
    """Generates the projection of n in the specified base until it becomes a single digit."""
    result = [n]
    while n >= base:
        n = digit_sum(n, base)
        result.append(n)
    return result

def is_tasty(projection, base):
    """Determines if a projection in the specified base is tasty."""
    counts = [0] * base
    for num in projection:
        for digit in format(num, f'0{base}'):
            counts[int(digit)] += 1
    return all(count == counts[0] for count in counts)

def find_tasty_numbers(base, limit=10):
    """Finds the first `limit` tasty numbers for the given base."""
    tasty_numbers = []
    n = base  # Start checking from the first number having at least 2 digits in the given base
    while len(tasty_numbers) < limit:
        proj = projection(n, base)
        if is_tasty(proj, base):
            tasty_numbers.append((n, proj))
        n += 1
    return tasty_numbers

def print_tasty_numbers():
    """Prints the first ten tasty numbers and their projections for each base from 2 through 10."""
    for base in range(2, 11):
        print(f"Base {base}:")
        tasty_numbers = find_tasty_numbers(base)
        for num, proj in tasty_numbers:
            proj_str = " -> ".join(format(p, f'0{base}') for p in proj)
            print(f"{format(num, f'0{base}')} -> {proj_str}")
        print()

# Run the function to print the tasty numbers for bases 2 to 10
print_tasty_numbers()
