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


def checksum(entry: str):
    """perform checksum on an entry
    checksum calculation: (d1+2*d2+3*d3+...+9*d9) mod 11 = 0
    """
    total = 0
    for i, digit in enumerate(entry):
        total += int(digit) * (i + 1)
    return total % 11 == 0


def parse_entry(entry: str) -> str:
    """parse a 9-digit entry"""
    output = ''
    for i in range(9):
        i = i * 3
        j = i + 3
        digit = '\n'.join([o[i:j] for o in entry.split('\n')])
        output += DIGITS[digit]

    if not checksum(output):
        output += ' ERR'

    return output


def main():
    parse_digits('digits.txt')
    cases = parse_test_cases('testcases2.txt')

    entry, expected, result = None, None, None
    try:
        for case in cases:
            entry = case['input']
            expected = case['result']
            result = parse_entry(entry)

            assert expected == result

    except AssertionError:
        print('case incorrect')
        print('entry:', entry)
        print('expected:', expected)
        print('result:', result)
        return

    print('success')


if __name__ == "__main__":
    main()
