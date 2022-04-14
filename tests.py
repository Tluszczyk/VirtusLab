import record_tools_tests
import sort_csv_tests

tests = [
    record_tools_tests,
    sort_csv_tests
]

if __name__ == '__main__':
    err = 0
    for test in tests:
        err += test.runtests()
    print("OK" if err == 0 else f'{err} ERRORS')