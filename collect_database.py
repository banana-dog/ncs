import csv
import glob
import os

directory = "data/repos"
# check origin source
link_files = glob.glob(f"{directory}/**/link_to_repo.txt", recursive=True)
with open(
    "data/base.csv", "w", newline=""
) as new_file:
    writer = csv.writer(new_file)
    for link_file in link_files:
        with open(link_file, "r") as file:
            link_content = file.read()

        curr_dir = os.path.dirname(link_file)

        other_files = glob.glob(f"{curr_dir}/**/*.c", recursive=True)

        for other_file in other_files:
            with open(other_file, "r") as f:
                try:
                    f = f.read()
                    writer.writerow([other_file, link_content, f])
                except Exception as e:
                    print(e)