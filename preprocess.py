import csv
import re


def write_func(name, source, text):
    with open("./to_search_for.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        text = re.sub(
            r"(pcVar\d*)|(undefined\d*)|(param_\d*)|(cVar\d*)|(puVar\d*)||(int)|(char)|(long)|(double)|(float)|(if)|(while)|(do)|(return)|(void)|(static)|(bool)|(for)|(else)|(struct)",
            "",
            text,
        )
        writer.writerow([name, source, text])

import csv
import glob
import re
import os


def remove_comments(string):
    string = re.sub(r"//.*?\n", "", string, flags=re.MULTILINE)
    string = re.sub(r"/\*.*?\*/", "", string, flags=re.DOTALL)
    return string

link_files = glob.glob(f"{directory}/**/link_to_repo.txt", recursive=True)
with open("./to_search_for.csv", "w", newline="") as new_file:
    writer = csv.writer(new_file)
        with open("binary.c", "r") as f:
                try:
                    f = f.read()
                    f = re.sub(
                        r"((.*Var\d*)|(undefined\d* .*\n)|(param_\d*)|#include .+\n)|(int)|(char)|(long)|(double)|(float)|(if)|(while)|(do)|(return)|(void)|(static)|(bool)|(for)|(else)|(struct)",
                        r"",
                        f,
                    )
                    f = remove_comments(f)
                    writer.writerow([f])
                except:
                    continue
