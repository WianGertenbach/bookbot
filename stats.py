def split_book(file_str):
  split_text = file_str.split()
  return split_text

def count_chars(split_text):
  dict_of_chars = {}
  list_of_chars = ['a','b','c','4']
  for word in split_text:
    lower_case_word = word.lower()
    for char in list_of_chars:
      if char in word:
        print(f"{char} in {word}")