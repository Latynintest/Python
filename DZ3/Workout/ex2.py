from book import Book


book1 = Book('War and Peace', 'Leo Tolstoy')
book2 = Book('Hamlet', 'William Shakespeare')
book3 = Book('Moby Dick', 'Herman Melville')

library = [book1, book2, book3]
for book in library:
    print(book)
