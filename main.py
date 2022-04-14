import sys
from join_csv import join_csv

from sort_csv import sort_csv

if __name__ == '__main__':
    a_file_path = sys.argv[1]
    b_file_path = sys.argv[2]
    column = sys.argv[3]
    join_type = sys.argv[4]
    
    join_csv(a_file_path, b_file_path, column, join_type)