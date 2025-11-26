import sys
import string


def fetch_input() -> str | None:
    """
    Fetch input from command line or user.

    Returns:
        str: Input text
    """
    if len(sys.argv) > 2:
        raise AssertionError("the arguments are bad")

    if len(sys.argv) == 2:
        return sys.argv[1]

    try:
        print("What is the text to count?")
        return sys.stdin.read()
    except (KeyboardInterrupt, EOFError):
        return None


def main():
    """
    Count character types in a string.
    """
    try:
        text = fetch_input()

        if text is None:
            return

        upper_count = sum(1 for c in text if c.isupper())
        lower_count = sum(1 for c in text if c.islower())

        punctuation_count = sum(1 for c in text if c in string.punctuation)

        space_count = sum(1 for c in text if c.isspace())
        digit_count = sum(1 for c in text if c.isdigit())

        print(f"The text contains {len(text)} characters:")

        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")

        print(f"{punctuation_count} punctuation marks")

        print(f"{space_count} spaces")
        print(f"{digit_count} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
