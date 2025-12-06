import csv
from datetime import date

class BorrowRecord:
    file = "data/borrow_records.csv"

    def __init__(self, recordID, studentID, bookID, borrowDate, returnDate):
        self.recordID = recordID
        self.studentID = studentID
        self.bookID = bookID
        self.borrowDate = borrowDate
        self.returnDate = returnDate

    @staticmethod
    def get_all():
        records = []
        with open(BorrowRecord.file, "r") as f:
            for row in csv.reader(f):
                if row:
                    records.append(BorrowRecord(*row))
        return records

    @staticmethod
    def create(studentID, bookID):
        all_records = BorrowRecord.get_all()
        recordID = len(all_records) + 1
        today = date.today().isoformat()

        with open(BorrowRecord.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([recordID, studentID, bookID, today, ""])

    @staticmethod
    def return_book(recordID):
        rows = []
        today = date.today().isoformat()

        with open(BorrowRecord.file, "r") as f:
            for row in csv.reader(f):
                if row[0] == recordID:
                    row[4] = today  
                rows.append(row)

        with open(BorrowRecord.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

