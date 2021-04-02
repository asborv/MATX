def factors(n: int) -> list[int]:
  """Finds all prime factors of n.

  Args:
      n (int): The number to be factored

  Returns:
      list[int]: All prime factors of n, with duplicates
  """
  # Type check for n
  if not isinstance(n, (int, float)) or int(n) != n:
    raise TypeError(f"""
    n should be of type int, but is {type(n)}.
    If n is passed as a float, it MUST have a whole number value.
    """)
  
  factors = []
  d = 2
  max_d = n/2

  # Sieve of Eratosthenes
  # link https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  while d <= max_d:
    # print(f"{'Checking if {}|{}':-^40}".format(n, d))
    if not n % d:
      factors.append(d)
      # print(f"""
      # {n} divides {d}.
      # New n is: {n//d}.
      # Factors are now: {factors}.
      # """)
      n //= d
      continue
    else:
      d += 1
  # print(f"Done checking because the divisor is {d}.")
  return factors if factors else [n]
