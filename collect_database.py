import csv
import glob

# Проходим по всем файлам в директории


with open('base.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    for file_path in glob.glob('./repos/tmate/*.c'):
        with open(file_path, 'r') as file:
            f = file.read()
            writer.writerow([file_path, f])

