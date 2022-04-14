from record_tools import split_record, remove_trailing_break

TESTED = [
    split_record,
    remove_trailing_break
]

NAMES = [
    'split_record',
    'remove_trailing_break'
]

TESTS = [
    [
        (("1,\"Luke, I am your father\", 2"), ["1", "\"Luke, I am your father\"", " 2"]),
        ((" 12 3, \"akka, is, a, great, framework\", 2, 3, 4, \"22,22\""), [" 12 3"," \"akka, is, a, great, framework\""," 2"," 3"," 4"," \"22,22\""])
    ],
    [
        ("record record\n", "record record")
    ]
]

def runtests():
    err = 0
    for TEST, function, name in zip(TESTS, TESTED, NAMES):
        print(f'TESTS for function {name}:')
        err_test = 0
        for args, result in TEST:
            got = function(args)
            if got != result:
                err_test += 1
                print(f"\t{name}: args: {args}, expected: {result} got: {got}")
        err += err_test

        print(f'\t{name}: OK' if err_test==0 else f'{name}: {err} ERRORS')    
    print("OK" if err==0 else f'{err} ERRORS')