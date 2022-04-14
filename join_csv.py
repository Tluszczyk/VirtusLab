import os
from settings import *
from record_tools import split_record, remove_trailing_break
from sort_csv import sort_csv
from file_tools import remove_sorted_files

def create_joined_name(a_file_path, b_file_path, join_type):
    a_name = os.path.basename(a_file_path)[:-11]
    b_name = os.path.basename(b_file_path)[:-11]
    base_path = os.path.dirname(a_file_path)
    return f'{base_path}/{a_name}_{join_type}_{b_name}.csv'

def join(a_file_path, b_file_path, column_name, join_type):
    def choose_on_type(alt_left, alt_right):
        return alt_left if join_type != 'right' else alt_right

    joined_file_path = create_joined_name(a_file_path, b_file_path, join_type)

    a_file,b_file = open(a_file_path), open(b_file_path)
    joined_file = open(joined_file_path, 'a')
    
    a_header = a_file.readline()
    b_header = b_file.readline()

    a_join_column_index = a_header.split(',').index(column_name)
    b_join_column_index = b_header.split(',').index(column_name)

    b_header_split = remove_trailing_break(b_header).split(',')

    b_null_record = ','.join(map(lambda _: "NULL", b_header_split))

    joined_header = remove_trailing_break(a_header) + ',' + ','.join(b_header_split[:b_join_column_index] + b_header_split[b_join_column_index+1:]) + '\n'
    joined_file.write(joined_header)
    print(joined_header, end="")

    main_file = choose_on_type(a_file, b_file)
    sub_file  = choose_on_type(b_file, a_file)

    while True:
        main_line = remove_trailing_break(main_file.readline())
        if main_line == '':
            break

        main_split_record = split_record(main_line)

        found_match = False
        while True:
            sub_line = remove_trailing_break(sub_file.readline())
            if sub_line == '':
                sub_file.seek(0)
                break
            
            sub_split_record = split_record(sub_line)

            a_split_record = choose_on_type(main_split_record, sub_split_record)
            b_split_record = choose_on_type(sub_split_record, main_split_record)

            a_line = choose_on_type(main_line, sub_line)
            b_line_no_joined_column = ','.join(b_split_record[:b_join_column_index] + b_split_record[b_join_column_index+1:]) + '\n'

            if b_split_record[b_join_column_index] == a_split_record[a_join_column_index]:
                joined_file.write(a_line + ',' + b_line_no_joined_column)
                print(a_line + ',' + b_line_no_joined_column, end="")
                found_match = True
                
        if not found_match:
            if join_type == 'left':
                joined_file.write(a_line + ',' + b_null_record + '\n')
                print(a_line + ',' + b_null_record)

            elif join_type == 'right':
                a_null_record_split = ["NULL"] * len(a_split_record)
                a_null_record_split[a_join_column_index] = a_split_record[a_join_column_index]

                b_line_no_joined_column = ','.join(main_split_record[:b_join_column_index] + main_split_record[b_join_column_index+1:]) + '\n'

                joined_file.write(','.join(a_null_record_split) + ',' + b_line_no_joined_column + '\n')
                print(','.join(a_null_record_split) + ',' + b_line_no_joined_column)

    joined_file.close()
    a_file.close()
    b_file.close()


def join_csv(a_file_path, b_file_path, column, join_type):
    sort_csv(a_file_path, column)
    sort_csv(b_file_path, column)

    join(a_file_path[:-4]+'_sorted.csv', b_file_path[:-4]+'_sorted.csv', column, join_type)

    remove_sorted_files(a_file_path)
    remove_sorted_files(b_file_path)