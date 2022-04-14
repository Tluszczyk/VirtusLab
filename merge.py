from queue import PriorityQueue

from record_tools import split_record

def merge(basefilepath, header, temp_file_map: dict, column_index):
    heap = PriorityQueue()

    sorted_file = open(f"{basefilepath[:-4]}_sorted.csv", 'a')
    sorted_file.write(header)

    for key, value in temp_file_map.items():
        file = open(value)
        file.readline()
        heap.put((key, file))

    while not heap.empty():
        _, file = heap.get()
        line = file.readline()
        sorted_file.write(line)

        old_pos = file.tell()
        next_line = file.readline()
        file.seek(old_pos)

        if next_line == "":
            file.close()
            if line[-1] != '\n':
                sorted_file.write('\n')
        else:
            new_key = split_record(next_line)[column_index]
            
            heap.put((new_key, file))

    sorted_file.close()