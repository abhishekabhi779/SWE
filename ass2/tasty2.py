def is_tasty(number, base):
  """Checks if a number is tasty in a given base.

  Args:
      number: The number to check.
      base: The base of the number system.

  Returns:
      True if the number is tasty, False otherwise.
  """
  seen = set()  # Track seen coefficients
  while number > 0:
    sum_of_digits = 0
    while number > 0:
      sum_of_digits += number % base
      number //= base
    if sum_of_digits in seen:
      return False
    seen.add(sum_of_digits)
    number = sum_of_digits
  return len(seen) == base

def main():
  """Finds and prints the first ten tasty numbers for each base 2 through 10."""
  max_iterations = 1000  # Set a maximum number of iterations to prevent infinite loops
  for base in range(2, 11):
    count = 0
    number = 0
    while count < 10 and number < max_iterations:  # Limit both count and number
      number += 1
      if is_tasty(number, base):
        projection = []
        temp = number
        while temp > 0:
          sum_of_digits = 0
          while temp > 0:
            sum_of_digits += temp % base
            temp //= base
          projection.append(sum_of_digits)
          temp = sum_of_digits
        print(f"Base {base}: {number} -> {projection}")
        count += 1

if __name__ == "__main__":
  main()
