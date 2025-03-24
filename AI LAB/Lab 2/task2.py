class Library:
    def __init__(self):
        self.fiction = set()
        self.non_fiction = set()
        self.science = set()
        self.history = set()

    def add_book(self, genre, book):
        getattr(self, genre).add(book)

    def remove_book(self, genre, book):
        getattr(self, genre).discard(book)

    def check_book(self, genre, book):
        return book in getattr(self, genre)

    def union_books(self, genre1, genre2):
        return getattr(self, genre1).union(getattr(self, genre2))

    def intersection_books(self, genre1, genre2):
        return getattr(self, genre1).intersection(getattr(self, genre2))

    def difference_books(self, genre1, genre2):
        return getattr(self, genre1).difference(getattr(self, genre2))


library = Library()
library.add_book('fiction', 'Atomic Habits')
library.add_book('fiction', 'To Kill a Mockingbird')
library.add_book('science', 'A Brief History of Time')
library.add_book('science', 'Atomic Habits')
print("Fiction & Science Union:", library.union_books('fiction', 'science'))
print("Fiction & Science Intersection:", library.intersection_books('fiction', 'science'))
print("Fiction - Science Difference:", library.difference_books('fiction', 'science'))
