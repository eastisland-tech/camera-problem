import re


def de_abbreviate(s, brand, **kwargs):
    """
    This function will remove abbreviations,
    depending on reg matching associated with
    brand names.
    """
    patterns = {
        'canon': {
            r'(?i)mk': 'Mark'
        }
    }
    for pattern, value in patterns[brand].items():
        s = re.sub(pattern, value, s)
    return s


def to_numerals(match):
    """
    This function accepts an re match and
    does the actual legwork of replacing decimal
    numbers with roman numerals.
    """
    s = match.group()
    numerals = {
        '1': ' I',
        '2': ' II',
        '3': ' III',
        '4': ' IV',
        '5': ' V',
        '6': ' VI',
        '7': ' VII',
        '8': ' VIII',
        '9': ' IX',
    }
    return numerals[s.strip()]


def add_numerals(s, **kwargs):
    """
    This method handles converting decimal numbers
    to roman numerals, if a proper pattern match exists.
    """
    patterns = [
        r'(?i)(?<=mark)\s*[1-9]'
    ]
    for pattern in patterns:
        s = re.sub(pattern, to_numerals, s)
    return s


def format_data(s):
    """
    This function will handle the calling
    of individual formatters for special case
    formatting. ie. Abbreviations, Roman Numerals, etc
    """
    cases = {
        'canon': [de_abbreviate, add_numerals]
    }
    for brand, formatters in cases.items():
        if brand in s.lower():
            for formatter in formatters:
                s = formatter(s, brand=brand)
    return s


def better_name(new, original):
    """
    This function will do a quick check to see
    which name is prefered. More verbose naming
    seems to be me appropriate, so we'll compare
    the lengths.
    """
    return len(new) > len(original)


if __name__ == '__main__':
    i = raw_input("Input File Path: ")
    o = raw_input("Out File Path: ")
    cam_lookup = {}
    with open(i) as f:
        cameras = sorted(set(f.readlines()))
        for c in cameras:
            c = format_data(c).strip()
            key = c.replace(' ', '').lower()
            lookup = cam_lookup.get(key, None)
            if not lookup or better_name(c, lookup):
                cam_lookup[key] = c

    with open(o, 'w') as f:
        values = sorted(cam_lookup.values())
        for c in values:
            f.write(c + '\n')
