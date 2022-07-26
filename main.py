from user import *
import csv


def get_contacts(filename):
    lst = []
    with open(filename, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)

        dict_n = {j: i for i, j in enumerate(reader.__next__())}

        for row in reader:
            lst.append(User(row, dict_n))

    return lst

