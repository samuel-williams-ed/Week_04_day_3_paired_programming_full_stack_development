import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

#load and save test Authors
author_1 = Author("Will Tipton", 40, "Know when to Holdem")
author_repository.save(author_1)
author_2 = Author("George R.R Martin", 72, "Never forget what you are, for surely the world will not. Make it your strength then it can never be your weakness")
author_repository.save(author_2)

#load and save test Books
book_1 = Book("Applications of NLHoldem", author_1)
print("")
print(f"console: book_1: {book_1.__dict__}")
book_repository.save(book_1)
print("")
print(f"console: book_1 after saving: {book_1.__dict__}")
book_2 = Book("Hobbit", author_2)
book_repository.save(book_2)





# view all books (contains authors)
print("console: view_all_result:")
view_all_result = book_repository.view_all()
print(book_1.__dict__)

print("")
print("console: printing loop:")
for result in view_all_result:
    print(result.__dict__)

# print(book_1.__dict__)
# print(book_2.__dict__)
# print(author_1.__dict__)
# print(author_2.__dict__)