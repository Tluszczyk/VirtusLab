from queue import PriorityQueue

from record_tools import split_record

def merge(basefilepath, header, temp_file_map: dict, column_index):
    class PriorityEntry(object):
        def __init__(self, key, data):
            self.key = key
            self.data = data

        def __lt__(self, other):
            return self.key < other.key

        def __iter__(self):
            for each in self.__dict__.values():
                yield each

    heap = PriorityQueue()

    sorted_file = open(f"{basefilepath[:-4]}_sorted.csv", 'a')
    sorted_file.write(header+"\n")

    for key, temp_files in temp_file_map.items():
        for temp_file in temp_files:
            file = open(temp_file)
            file.readline()
            heap.put(PriorityEntry(key, file))

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
            
            heap.put(PriorityEntry(new_key, file))

    sorted_file.close()