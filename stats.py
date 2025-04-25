def word_count(book_text):
  count = 0
  split_text = book_text.split()
  for word in split_text:
    count += 1
  return count

def count_chars(book_text):
  dict_of_chars = {}
  for i in book_text.lower():
    if i not in dict_of_chars:
      dict_of_chars[i] = 1
    else:
      dict_of_chars[i] += 1  
  return dict_of_chars
