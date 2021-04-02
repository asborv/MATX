from matx import tallteori

# link https://www.calculatorsoup.com/calculators/math/prime-factors.php
def test_factors():
  assert tallteori.factors(654) == [2, 3, 109]
  assert tallteori.factors(654434) == [2, 11, 151, 197]
  assert tallteori.factors(13) == [13]
  assert tallteori.factors(65481) == [3, 13, 23, 73]
  assert tallteori.factors(654815) == [5, 7, 53, 353]
  assert tallteori.factors(111111) == [3, 7, 11, 13, 37]
