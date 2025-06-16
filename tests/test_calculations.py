import pytest
from src.orbital_usage_api.calculations import calculate_credits, is_palindrome

# pytest.approx will allow the expected value to have some error margin specified
# in the second parameter
@pytest.mark.parametrize("text, expected", [
  ("Short Message", pytest.approx(1.0, 0.01)),  # 1.0 because of unique bonus!
  ("Are there any restrictions on alterations or improvements?", pytest.approx(5.2, 0.01)),
  ("What are the indemnity provisions?", pytest.approx(2.9, 0.01)),
  ("What are the restrictions on operating hours and any related provisions for commercial tenants?", pytest.approx(10.55, 0.01)),
  ("A man, a plan, a canal, Panama", pytest.approx(8.8, 0.1)),   # palindrome * 2
  ("What happens if the property is sold during the lease term?", pytest.approx(7.05, 0.01)),
  ("What are the detailed conditions under which the landlord can increase the rent during the lease period?", pytest.approx(20.01, 0.01)),
])
def test_calculate_credits_various_cases(text, expected):
  assert calculate_credits(text) == expected

@pytest.mark.parametrize("text, expected", [
  ("madam", True),
  ("racecar", True),
  ("Was it a car or a cat I saw?", True),
  ("hello", False),
  ("", True),  # empty is a palindrome
  ("Ma'am", True),  # with apostrophe
])
def test_is_palindrome(text, expected):
  assert is_palindrome(text) == expected