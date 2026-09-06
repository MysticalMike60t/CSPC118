import re


def check_has_special_chars(string: str) -> bool:
    return bool(re.search(r"[^a-zA-Z0-9]", string))
