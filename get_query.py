import csv
# не запускать
# просто загружает содержимое файла. В текущем data/to_search_for.csv уменьшила объем кода вручную
with open("data/binary.c", 'r') as f:
    with open("data/to_search_for.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        text = f.read()
        writer.writerow([text])

