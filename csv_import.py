import csv
from question import Question
from category import Category


def import_csv(filename: str) -> [Category]:
    categories_dict = {}
    with open(file=filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader:
            question = Question(title=row[0], answer=row[1])
            if categories_dict.get(row[2]) is None:
                categories_dict[row[2]] = [question]
            else:
                categories_dict.get(row[2]).append(question)
    return [Category(title=category_name, questions=questions) for category_name , questions in categories_dict.items()]
