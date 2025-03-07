import csv

def list_csv_rows(file_path, num_rows):
    rows = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i >= num_rows:
                break
            rows.append(row)
    return rows

if __name__ == "__main__": #Ez a sor ellenőrzi, hogy a szkriptet közvetlenül futtatjuk-e, vagy importáljuk egy másik programból.
    file_path = "c:\\Pyhton\\Input\\otos.csv"  # Adjuk meg a CSV fájl elérési útját
    num_rows = 10  # Állítsuk be a kívánt sorok számát
    result = list_csv_rows(file_path, num_rows)
    for row in result:
        print(row)
