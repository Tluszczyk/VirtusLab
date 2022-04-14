def split_record(record):
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