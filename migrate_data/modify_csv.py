import csv

model_map = {
    "1": "Honda",
    "2": "Suzuki",
    "3": "Yamaha",
    "4": "Triumph",
    "5": "Harley Davidson",
    "6": "Ducati",
    "7": "Victory",
    "8": "Kawasaki"
}

with open("model.csv", "r") as f:
    rows = csv.reader(f)
    lines = [l for l in rows]
    for line in lines:
        if line[0][0] in model_map:
            new_line = [model_map[line[0][0]], line[0][1], line[0][2]]
        print(new_line)
