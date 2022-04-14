import sys, os

from join_csv import join_csv
from record_tools import remove_trailing_break

def validate_file(f):
    ''' check if the file exists '''
    if not os.path.exists(f):
        raise Exception("File does not exist")

def validate_column(a, b, column):
    ''' check if the specified column exists in both files '''
    with open(a) as fa, open(b) as fb:
        aheaders = remove_trailing_break(fa.readline()).split(',')
        bheaders = remove_trailing_break(fb.readline()).split(',')

        if column not in aheaders:
            raise Exception("Column name doesn't appear in the first file's header")
        if column not in bheaders:
            raise Exception("Column name doesn't appear in the second file's header")

        fa.close()
        fb.close()

def validate_join_type(j):
    ''' check if the specified join type is one of these three '''
    if j not in ["left", "right", "inner"]:
        raise Exception("join type must be one of those (left, right, inner)")

def validate_input(a,b,c,j):
    validate_file(a)
    validate_file(b)
    validate_column(a,b,c)
    validate_join_type(j)


if __name__ == '__main__':
    argc = len(sys.argv)-1
    if argc < 3: raise Exception("You have to specify at least two input files, and a column name")
    if argc > 4: raise Exception("Too many inputs")

    a_file_path = sys.argv[1]
    b_file_path = sys.argv[2]
    column = sys.argv[3]
    join_type = 'inner' if argc==3 else sys.argv[4]

    validate_input(a_file_path, b_file_path, column, join_type)
    
    join_csv(a_file_path, b_file_path, column, join_type)