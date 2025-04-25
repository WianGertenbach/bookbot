def get_book_text(file_path):
  with open(file_path) as file:
    file_contents = file.read()
  return file_contents

def count_words(file_str):
  split_text = file_str.split()
  count = 0
  for word in split_text:
    count += 1
  return count

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  num_words = count_words(book_text)
  print(f"{num_words} words found in the document")

main()