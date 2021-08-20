import sys

# Typical fizzbuzz interview question response
def fizzbuzz(input: int):
  """
  Typical fizzbuzz interview question response.
  Given an input integer:
  - If the number is a multiple of 3, return 'fizz'
  - If the number is a multiple of 5, return 'buzz'
  - If the number is a multiple of both 3 and 5, return 'fizzbuzz'
  - Otherwise return the input number
  """
  if type(input) != int:
    raise TypeError('Invalid argument type')
  if input < 0 or input > 9999:
    raise ValueError('Invalid argument range')
  if input % 15 == 0:
    return 'fizzbuzz'
  if input % 3 == 0:
    return 'fizz'
  if input % 5 == 0:
    return 'buzz'
  return str(input)

# Trivial CLI wrapper for fizzbuzz function
if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise TypeError('missing argument')
  first_arg = sys.argv[1]
  input_int = int(first_arg)
  print(fizzbuzz(input_int))
