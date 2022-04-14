from sort_csv import sort_csv
from file_tools import remove_sorted_files
from record_tools import split_record, remove_trailing_break

TESTS = [
    ("./data/d_10/A.csv", "id"),  ("./data/d_10/B.csv", "city"), 
    ("./data/d_100/A.csv", "firstname"), ("./data/d_100/B.csv", "country")
]   

def check_if_sorted(file_path, column):
    lines = open(file_path).readlines()
    header = remove_trailing_break(lines[0])
    col_index = split_record(header).index(column)

    return lines[1:] == sorted(lines[1:], key=lambda line: split_record(line)[col_index])

def runtests():
    err = 0
    print("sort csv tests")
    for i, (path, column) in enumerate(TESTS):
        sort_csv(path, column)
        is_sorted = check_if_sorted(path[:-4]+"_sorted.csv", column)
        remove_sorted_files(path)

        if not is_sorted:
            err += 1
            print(f"\ttest {i+1}: args: {path, column}, expected: sorted, got: unsorted")
        else:
            print(f"\ttest {i+1}: ok")

    print("sort_csv: OK" if err==0 else f'sort_csv: {err} ERRORS')
    return err