import csv

class Category:
    file = "data/categories.csv"

    def __init__(self, categoryID, name):
        self.categoryID = categoryID
        self.name = name

    @staticmethod
    def get_all():
        categories = []
        with open(Category.file, "r") as f:
            for row in csv.reader(f):
                if row:
                    categories.append(Category(*row))
        return categories

    @staticmethod
    def get_by_id(categoryID):
        with open(Category.file, "r") as f:
            for row in csv.reader(f):
                if row and row[0] == categoryID:
                    return Category(*row)
        return None
