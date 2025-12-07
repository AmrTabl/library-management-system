import csv

class Book:
    file = "data/books.csv"

    def __init__(self, bookID, title, author, categoryID, status):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.categoryID = categoryID
        self.status = status
    @staticmethod
    def get_all():
        books = []
        with open(Book.file, "r") as f:
            for row in csv.reader(f):
                if row:
                    books.append(Book(*row))
        return books

    @staticmethod
    def search(query):
        results = []
        with open(Book.file, "r") as f:
            for row in csv.reader(f):
                if row and query.lower() in row[1].lower():
                    results.append(Book(*row))
        return results

    @staticmethod
    def update_status(bookID, new_status):
        rows = []
        with open(Book.file, "r") as f:
            for row in csv.reader(f):
                if row[0] == bookID:
                    row[4] = new_status
                rows.append(row)

        with open(Book.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

