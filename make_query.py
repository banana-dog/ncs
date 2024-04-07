import csv

with open("binary.c", 'r') as f:
    with open("./to_search_for.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        text = f.read()
        writer.writerow([text])

