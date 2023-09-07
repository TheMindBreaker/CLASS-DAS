import csv
import os

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


filename = ROOT_DIR + "/sample_grocery.csv"


def load_data():
    with open(filename, mode='r') as file:
        return list(csv.DictReader(file))