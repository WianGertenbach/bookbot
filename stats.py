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

def sorted_dicts(dict_of_all_chars):
  list_of_dicts = []
  for char in dict_of_all_chars:
    if char.isalpha():
      chars_dict = {"char":char, "num":dict_of_all_chars[char]}
      list_of_dicts.append(chars_dict)

  def sort_on(dict):
    return dict["num"]

  list_of_dicts.sort(reverse=True, key=sort_on)
  return list_of_dicts
