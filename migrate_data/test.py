import csv

def load_models():
    with open("models.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            print(row)


load_models()
