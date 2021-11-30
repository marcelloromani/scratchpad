def decode_line(line: str) -> dict:
    result = {}
    for field in line.split():
        key, value = field.split(":")
        if value.isnumeric():
            value = int(value)
        result[key] = value
    return result


def read_passports_from_file(filename) -> list:
    passports = []
    with open(filename, "r") as f:
        passport = {}
        for line in f:
            line = line.strip()
            if len(line) == 0:
                # passports are separated by one or more newlines
                # current passport finished now, so we store it
                if passport != {}:
                    passports.append(passport)
                    passport = {}
            else:
                passport = passport | decode_line(line)  # NOTE: 3.9+ ONLY
    if passport != {}:
        passports.append(passport)
    return passports
