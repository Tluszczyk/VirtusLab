from file_tools import read_at_most_n_bytes_of_records, remove_temp_sort_files
from record_tools import split_record, remove_trailing_break
from settings import *
from merge import merge

def sort_bulk(bulk, index):
    ''' sorts small (max memory size) chunks of csv records '''
    records = bulk.splitlines()

    s = sorted(records, key=lambda r: split_record(r)[index])
    return '\n'.join(s), split_record(s[0])[index]


def sort_csv(filepath, column_name):
    ''' splits file to multiple smaller files, then sorts them all and merges with heap '''
    file = open(filepath)

    header = remove_trailing_break(file.readline())
    index = header.split(',').index(column_name)

    temp_file_paths = {}

    bulk_count = 0

    done_reading = False
    while not done_reading:
        bulk, done_reading = read_at_most_n_bytes_of_records(file, buffer_size)
        bulk, key = sort_bulk(bulk, index)

        bulk_file_path = f"{filepath[:-4]}_temp_sort_{bulk_count}.csv"
        bulk_file = open(bulk_file_path, 'a')

        bulk_file.write(header+'\n')
        bulk_file.write(bulk)

        bulk_file.close()

        if key in temp_file_paths:
            temp_file_paths[key].append(bulk_file_path);
        else:
            temp_file_paths[key] = [bulk_file_path]
        bulk_count += 1

    file.close()

    merge(filepath, header, temp_file_paths, index)
    remove_temp_sort_files(filepath)