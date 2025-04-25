from stats import count_chars

def get_book_text(file_path):
  with open(file_path) as file:
    file_contents = file.read()
  return file_contents

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  chars = count_chars(book_text)
  print(chars)

main()