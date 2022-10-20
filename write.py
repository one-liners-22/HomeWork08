import csv

def write_csv(empl_data):
    with open('database.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for empl in empl_data:
            writer.writerow(empl.values())

def write_json():
    pass