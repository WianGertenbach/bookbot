def count_words(file_str):
  split_text = file_str.split()
  count = 0
  for word in split_text:
    count += 1
  return count