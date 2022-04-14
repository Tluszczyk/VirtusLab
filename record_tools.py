def split_record(record):
    ''' splits csv record by a comma, but leaves the quoted fields unsplit '''
    ''' e.g. 102,Antofagasta,"Tanzania, United Republic of" will be split to '''
    ''' ["102" , "Antofagasta", "Tanzania, United Republic of"] '''

    res = []

    opened_quote = False
    curr = ""
    for c in record:
        if c == '\"':
            opened_quote = not opened_quote
            curr += c
        
        elif not opened_quote:
            if c == ',':
                res.append(curr)
                curr = ""
            else:
                curr += c
        else:
            curr += c
    return res + [curr]

def remove_trailing_break(record):
    ''' removes \n character if it is the last character of a line '''
    if record == "": return ""
    return record[:-1] if record[-1] == '\n' else record