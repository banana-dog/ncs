import csv
import glob
import re
import os

def remove_comments(string):
    string = re.sub(r"//.*?\n", "", string, flags=re.MULTILINE)
    string = re.sub(r"/\*.*?\*/", "", string, flags=re.DOTALL)
    return string


directory = "./repos"

link_files = glob.glob(f"{directory}/**/link_to_repo.txt", recursive=True)
with open(
    "./base.csv", "w", newline=""
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
                    f = re.sub(r"(#include .+\n)|(int)|(char)|(long)|(double)|(float)|(if)|(while)|(do)|(return)|(void)|(static)|(bool)|(for)|(else)|(struct)", r"", f)
                    f = remove_comments(f)
                    writer.writerow([other_file, link_content, f])
                except:
                    continue