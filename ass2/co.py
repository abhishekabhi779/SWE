def sum_of_digits(n, base):
    # Calculate the sum of digits in a given number n in the specified base.
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total

def is_tasty(number, base):
    # Check if a number is tasty in the specified base.
    coefficients = [0] * base
    current = number
    while current >= base:
        current = sum_of_digits(current, base)
        coefficients[current] += 1

    # All coefficients must show up at least once and the same number of times.
    return all(coefficients[i] > 0 for i in range(base)) and len(set(coefficients)) == 1

def find_tasty_numbers():
    for base in range(2, 11):
        print(f"Base {base}:")
        tasty_numbers = []
        number = 1
        while len(tasty_numbers) < 10:
            if is_tasty(number, base):
                tasty_numbers.append(number)
                projection = sum_of_digits(number, base)
                print(f"{number} -> {projection}")
            number += 1

if __name__ == "__main__":
    find_tasty_numbers()
