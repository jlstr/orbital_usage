import re

def calculate_credits(text: str) -> float:
  base_cost = 1.0
  char_cost = 0.05 * len(text)
  # Using Python's Regex Expression Module to build the List
  # of words from a Message's Text
  words = re.findall(r"[a-zA-Z'-]+", text)
  word_cost = 0

  # Rules for Word Length Multipliers:
  for word in words:
    word_length = len(word)
    if word_length <= 3:
      word_cost += 0.1
    elif word_length <= 7:
      word_cost += 0.2
    else:
      word_cost += 0.3

  third_vowel_count = 0
  # Third bowel rules, start = 1 is used to keep the formula consistent with
  # the Math behind it
  for index, char in enumerate(text, start = 1):
    if index % 3 == 0 and char.lower() in "aeiou":
      third_vowel_count += 1

  third_vowel_bonus = third_vowel_count * 0.3
  length_penalty = 5.0 if len(text) > 100 else 0.0
  unique_bonus = -2.0 if len(set(words)) == len(words) else 0.0

  # Calculation of total credits 
  total = base_cost + char_cost + word_cost + third_vowel_bonus + length_penalty + unique_bonus
  total = max(total, 1.0)

  # Palindrome Exceptional case
  if is_palindrome(text):
    total *= 2

  return total

# Palindrome function also relies on Regular expression evaluation
def is_palindrome(text: str) -> bool:
  cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
  return cleaned == cleaned[::-1]