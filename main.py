from user import *
import csv


def get_contacts(filename):
    contacts_list = []
    with open(filename, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)

        index_dict = {j: i for i, j in enumerate(reader.__next__())}

        for row in reader:
            contacts_list.append(User(row, index_dict))

    return contacts_list
