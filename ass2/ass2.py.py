def convert_to_base(n, base):
    """Convert a decimal number n to a given base."""
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

def sum_digits_in_base(n_str, base):
    """Sum the digits of a number represented as a string in a given base."""
    return sum(int(digit, base) for digit in n_str)

def projection_sequence(n_str, base):
    """Generate the projection sequence for a number in a given base."""
    sequence = [n_str]
    while len(n_str) > 1:
        digit_sum = sum_digits_in_base(n_str, base)
        n_str = convert_to_base(digit_sum, base)
        sequence.append(n_str)
    return sequence

def is_tasty(number_str, base):
    """Check if a number is tasty in a given base."""
    sequence = projection_sequence(number_str, base)
    all_digits = ''.join(sequence)
    digit_count = {str(i): all_digits.count(str(i)) for i in range(base)}
    
    values = list(digit_count.values())
    return values.count(values[0]) == len(values) and values[0] > 0

def find_tasty_numbers(base, count):
    """Find the first `count` tasty numbers in a given base."""
    tasty_numbers = []
    number = 1
    while len(tasty_numbers) < count:
        number_str = convert_to_base(number, base)
        if is_tasty(number_str, base):
            tasty_numbers.append((number_str, projection_sequence(number_str, base)))
        number += 1
    return tasty_numbers

# Find the first 10 tasty numbers for bases 2 through 10 and print them
for base in range(2, 11):
    print(f"Base {base}:")
    tasty_numbers = find_tasty_numbers(base, 10)
    for number, projection in tasty_numbers:
        print(f"{number} -> {' -> '.join(projection[1:])}")
    print()

