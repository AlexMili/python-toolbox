from typing import Any, List


# Function to print data in pandas'/numpy's apply functions
def print_func(x: Any) -> None:
    print(x)


# Apply regex patterns on a string
def apply_patterns(string: str, patterns: List) -> str:
    for pattern in patterns:
        string = pattern.sub("",string)

    return string


# Keys becomes values and vis versa in a dict
def invert_keys_values(mydict: dict) -> dict:
    return {v: k for k, v in mydict.items()}
