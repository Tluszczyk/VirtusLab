import os
import glob

def read_at_most_n_bytes_of_records(file, n):
    buffer = ''

    # TODO: records that have break in them
    
    while True:
        file_pos = file.tell()
        line = file.readline()
        
        if len(line) == 0:
            return (buffer, True)
        
        if len(buffer) + len(line) > n:
            file.seek(file_pos)
            return (buffer, False)
        else:
            buffer += line


def remove_temp_sort_files(basefilepath):
    temp_sort_file_path = f"{basefilepath[:-4]}_temp_sort_*.csv"

    temp_sort_files = glob.glob(temp_sort_file_path)
    for temp_sort_file in temp_sort_files:
        try:
            permission = input(f"remove file {temp_sort_file}? y/[n]").lower()
            if permission == 'y' or permission == "yes":
                os.remove(temp_sort_file)
            else:
                print("Didn't remove the file")
        except OSError:
            print("Error while deleting file")