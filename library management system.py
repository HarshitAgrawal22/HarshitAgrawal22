def display():
  myfile = open("display.txt")
  books = eval(myfile.read())
  myfile.close()

  for b_id in books:
    details = books.get(b_id)
    print("Name:", details[0])
    print("Author:", details[1])
    print("Description:", details[2])
    print("=" * 50)


# ============= ADD A BOOK =============

# dict[key] = value


def add_book():
  myfile = open("display.txt")
  books = eval(myfile.read())
  myfile.close()

  book_id = max(books) + 1

  name = input("Enter the name of the book: ")
  author = input("Enter the author's name of the book: ")
  description = input("Enter the description of the book: ")

  books[book_id] = [name, author, description]

  myfile = open("display.txt", 'w')
  myfile.write(str(books))
  myfile.close()

  print("The book has been added successfully!")


display()