from main import split_record

TESTS = [
    (("1,\"Luke, I am your father\", 2"), ["1", "\"Luke, I am your father\"", " 2"]),
    ((" 12 3, \"akka, is, a, great, framework\", 2, 3, 4, \"22,22\""), [" 12 3"," \"akka, is, a, great, framework\""," 2"," 3"," 4"," \"22,22\""])
]

def runtests():
    err = 0
    for record, result in TESTS:
        got = split_record(record)
        if got != result:
            err += 1
            print(f"split_record: record: {record}, expected: {result} got: {got}")
    print("OK" if err==0 else f'{err} ERRORS')