import os
import csv
import subprocess

def open_explorer(dir_path):
    os.startfile(dir_path)

def read_dir(file_path):
    dirs = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        next(csv_reader)
        for row in csv_reader:
            dirs.append(row)
    return dirs


# if __name__ == '__main__':

#     file_path = "dirs.csv"
#     dirs = read_dir(file_path=file_path)
#     print(dirs)
#     dir_path = dirs[1][1]
#     open_explorer(dir_path=dir_path)

def open_csv():
    filename = 'dirs.csv'
    notepad_path = r"C:\windows\system32\notepad.exe"
    subprocess.call([notepad_path, filename])


if __name__ == '__main__':
    open_csv()