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

  while d <= max_d:
    if not n % d:
      n //= d
      factors.append(d)
      continue
    else:
      d += 1

  return factors if factors else [n]
