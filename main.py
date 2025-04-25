from stats import count_chars, word_count, sorted_dicts
import sys

def get_book_text(file_path):
  with open(file_path) as file:
    file_contents = file.read()
  return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = word_count(book_text)
    chars = count_chars(book_text)
    sorted_list = sorted_dicts(chars)

    print(f"""
  ============ BOOKBOT ============
  Analyzing book found at {file_path}...
  ----------- Word Count ----------
  Found {num_words} total words
  --------- Character Count -------
  """)

    for dict in sorted_list:
      print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()