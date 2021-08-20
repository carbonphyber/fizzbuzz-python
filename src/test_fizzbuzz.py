from fizzbuzz_app import fizzbuzz
import pytest

class TestFizzbuzzClass:
  """
  Test harness class for fizzbuzz function
  """
  def test_none(self):
    """
    fizzbuzz should raise a TypeError when passed None
    """
    raised = False
    try:
      fizzbuzz(None)
    except:
      raised = True
    assert raised == True

  def test_str(self):
    """
    fizzbuzz should raise a TypeError when passed str
    """
    raised = False
    try:
      fizzbuzz('some string')
    except:
      raised = True
    assert raised == True

  def test_bool(self):
    """
    fizzbuzz should raise a TypeError when passed bool
    """
    raised = False
    try:
      fizzbuzz(False)
    except:
      raised = True
    assert raised == True

  def test_int_negative(self):
    """
    fizzbuzz should raise a ValueError when passed a negative integer
    """
    raised = False
    try:
      fizzbuzz(-1)
    except:
      raised = True
    assert raised == True

  def test_int_too_large(self):
    """
    fizzbuzz should raise a TypeError when passed an integer larger than the supported range
    """
    raised = False
    try:
      fizzbuzz(10000)
    except:
      raised = True
    assert raised == True

  def test_int_one(self):
    """
    fizzbuzz should return '1' when passed 1
    """
    output = fizzbuzz(1)
    assert output == '1'

  def test_int_two(self):
    """
    fizzbuzz should return '2' when passed 2
    """
    output = fizzbuzz(2)
    assert output == '2'

  def test_int_three(self):
    """
    fizzbuzz should return 'fizz' when passed 3
    """
    output = fizzbuzz(3)
    assert output == 'fizz'

  def test_int_four(self):
    """
    fizzbuzz should return '4' when passed 4
    """
    output = fizzbuzz(4)
    assert output == '4'

  def test_int_five(self):
    """
    fizzbuzz should return 'buzz' when passed 5
    """
    output = fizzbuzz(5)
    assert output == 'buzz'

  def test_int_six(self):
    """
    fizzbuzz should return 'fizz' when passed 6
    """
    output = fizzbuzz(6)
    assert output == 'fizz'

  def test_int_seven(self):
    """
    fizzbuzz should return '7' when passed 3
    """
    output = fizzbuzz(7)
    assert output == '7'

  def test_int_nine(self):
    """
    fizzbuzz should return 'fizz' when passed 3
    """
    output = fizzbuzz(9)
    assert output == 'fizz'

  def test_int_ten(self):
    """
    fizzbuzz should return 'buzz' when passed 5
    """
    output = fizzbuzz(10)
    assert output == 'buzz'

  def test_int_fifteen(self):
    """
    fizzbuzz should return 'buzz' when passed 5
    """
    output = fizzbuzz(15)
    assert output == 'fizzbuzz'

  def test_int_sixteen(self):
    """
    fizzbuzz should return '16' when passed 5
    """
    output = fizzbuzz(16)
    assert output == '16'

  def test_int_thirty(self):
    """
    fizzbuzz should return 'fizzbuzz' when passed 5
    """
    output = fizzbuzz(30)
    assert output == 'fizzbuzz'

  def test_int_ninenineninenine(self):
    """
    fizzbuzz should return 'fizz' when passed 9999
    """
    output = fizzbuzz(9999)
    assert output == 'fizz'
