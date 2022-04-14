import pandas as pd
from join_csv import join_csv, create_joined_name
from file_tools import remove_sorted_files
from record_tools import split_record, remove_trailing_break

TESTS = [
    ("./data/d_10/A.csv", "./data/d_10/B.csv", "id", "left"), 
    ("./data/d_10/A.csv", "./data/d_100/B.csv", "id", "right"),
    ("./data/d_100/A.csv", "./data/d_10/B.csv", "id", "left"),
    ("./data/d_100/A.csv", "./data/d_10/B.csv", "id", "inner"),
    ("./data/d_100/A.csv", "./data/d_100/B.csv", "id", "right"),
    ("./data/d_100/A.csv", "./data/d_100/B.csv", "id", "inner") 
]   

def check_if_joined(a_path, b_path, column, join_type):
    joined_path = create_joined_name(a_path, b_path, join_type)

    a_csv = pd.read_csv(a_path)
    b_csv = pd.read_csv(b_path)
    j_csv = pd.read_csv(joined_path)

    m_csv = a_csv.merge(b_csv, on=column, how=join_type).sort_values(by=column)

    other_name = joined_path[:-4]+"_pandas.csv"
    m_csv.to_csv(other_name)

    is_joined = True
    with open(joined_path).readlines() as j_rl, open(other_name) as m_rl:
        for j,m in zip(j_rl, m_rl):
            if j != m: is_joined = False

    return is_joined


def runtests():
    err = 0
    print("join csv tests")
    for i, (a_path, b_path, column, join_type) in enumerate(TESTS):
        join_csv(a_path, b_path, column, join_type)
        is_joined = check_if_joined(a_path, b_path, column, join_type)

        if not is_joined:
            err += 1
            print(f"\ttest {i+1}: args: {a_path, b_path, column, join_type}, expected: joined, got: unjoined")
        else:
            print(f"\ttest {i+1}: ok")

    print("join_csv: OK" if err==0 else f'join_csv: {err} ERRORS')
    return err