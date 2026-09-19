def take_until(s: str, until: str, ignore_case: bool = False) -> str:
    until = until.lower() if ignore_case else until
    out = ''
    found = False

    for c in s:
        out += c

        if until in out:
            found = True
            break

    return out[:-len(until)] if found else out
