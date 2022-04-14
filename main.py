from sort_csv import sort_csv

if __name__ == '__main__':
    a_file_path = "./data/d_10/A.csv"
    b_file_path = "./data/d_10/B.csv"
    column = "id"

    sort_csv(a_file_path, column)
    sort_csv(b_file_path, column)
