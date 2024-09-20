def is_tasty(num, base):
    digits = set()
    projection = []
    orig_num = num

    while num > 0:
        digits.add(num % base)
        projection.append(num % base)
        num //= base

    while len(projection) > 1:
        num = sum(projection)
        projection = [int(d) for d in str(num)]
        for d in projection:
            digits.add(d)

    if len(digits) == base and all(projection.count(d) == projection.count(projection[0]) for d in digits):
        return orig_num, projection

    return None

def find_tasty_numbers(base):
    tasty_nums = []
    num = 1
    while len(tasty_nums) < 10:
        result = is_tasty(num, base)
        if result:
            tasty_nums.append(result)
        num += 1
    return tasty_nums

for base in range(2, 11):
    print(f"Base {base}:")
    tasty_nums = find_tasty_numbers(base)
    for num, projection in tasty_nums:
        print(f"{num} -> {' -> '.join(map(str, projection))}")
    print()