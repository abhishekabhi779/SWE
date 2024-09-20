def is_tasty(number, base):
    projection = []
    original_number = number
    while number >= base:
        digits = []
        while number:
            digits.append(number % base)
            number //= base
        projection.append(sum(digits))
        number = sum(digits)
    projection.append(number)

    digits_count = [0] * base
    for num in projection:
        for digit in str(num):
            digits_count[int(digit, base)] += 1

    return all(count > 0 for count in digits_count) and all(count == digits_count[0] for count in digits_count[1:])

def find_tasty_numbers(base, count):
    tasty_numbers = []
    number = 0
    while len(tasty_numbers) < count:
        if is_tasty(number, base):
            projection = [number]
            while number >= base:
                digits = []
                while number:
                    digits.append(number % base)
                    number //= base
                projection.append(sum(digits))
                number = sum(digits)
            projection.append(number)
            projection = [str(num) for num in projection]
            tasty_numbers.append(' -> '.join(projection))
        number += 1
    return tasty_numbers

for base in range(2, 11):
    print(f"Base {base}:")
    tasty_numbers = find_tasty_numbers(base, 10)
    for number in tasty_numbers:
        print(number)
    print()