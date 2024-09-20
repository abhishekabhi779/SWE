def get_digits(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits

def is_tasty(n, base):
    digits = get_digits(n, base)
    projection = [n]
    while len(digits) > 1:
        digits = get_digits(sum(digits), base)
        projection.append(sum(digits))
    freq = {}
    for d in projection:
        for digit in get_digits(d, base):
            freq[digit] = freq.get(digit, 0) + 1
    return len(freq) == base and all(freq[d] == freq[0] for d in freq)

for base in range(2, 11):
    tasty_numbers = []
    n = 1
    while len(tasty_numbers) < 10:
        if is_tasty(n, base):
            tasty_numbers.append(n)
        n += 1
    print(f"Base {base}:")
    for n in tasty_numbers:
        projection = [n]
        while len(get_digits(n, base)) > 1:
            n = sum(get_digits(n, base))
            projection.append(n)
        print(" -> ".join(map(str, projection)))
    print()