DIGITS = {}


def parse_digits(file: str) -> None:
    """parses an entry with 0 through 9 and returns a mapping of digits to digit strings"""

    with open(file, 'r') as f:
        entry = f.read()

    for i in range(10):
        j = i * 3
        k = j + 3
        digit = '\n'.join([o[j:k] for o in entry.split('\n')])
        DIGITS[digit] = str(i)


def parse_test_cases(file: str) -> list[dict]:
    """parses plaintext test cases from file"""
    with open(file, 'r') as f:
        lines = f.read().split('\n')

    cases, entry = [], []
    for line in lines:
        if line.startswith('='):
            cases.append({"input": '\n'.join(entry), "result": line[3:]})
            entry = []
        else:
            entry.append(line)

    return cases


def parse_entry(entry: str) -> str:
    """parse a 9-digit entry"""
    output = ''
    for i in range(9):
        i = i * 3
        j = i + 3
        digit = '\n'.join([o[i:j] for o in entry.split('\n')])
        output += DIGITS[digit]
    return output


def main():
    parse_digits('digits.txt')
    cases = parse_test_cases('testcases1.txt')

    entry, expected, result = None, None, None
    try:
        for case in cases:
            entry = case['input']
            expected = case['result']
            result = parse_entry(entry)

            assert expected == result

    except AssertionError:
        # if any match fails, print the expected and actual results
        print('case incorrect')
        print('entry:', entry)
        print('expected:', expected)
        print('result:', result)
        return

    print('success')


if __name__ == "__main__":
    main()
