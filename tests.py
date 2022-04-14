import split_record_tests

tests = [
    split_record_tests
]

if __name__ == '__main__':
    for test in tests:
        test.runtests()