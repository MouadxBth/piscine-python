from typing import Any


def NULL_not_found(object: Any) -> int:
    """
    Print the object type of all types of Null.

    Args:
        object: Any object to check

    Returns:
        int: 0 if it's a null type, 1 if not found
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
