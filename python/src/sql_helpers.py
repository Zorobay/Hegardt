def sql_string(d):
    if d is None:
        return 'null'
    return f"'{d}'"


def sql_number(n):
    if n is None:
        return 'null'
    return n


def escape(s: str) -> str:
    if not s:
        return ''
    return s.replace("'", "''")

# Ids are 0 based in the JSON file, but that is not handled well in SQL so increment them all by 1
def to_id(i: str) -> int:
    return int(i)+1