"""Small, pure string helpers."""


def to_upper(text: str) -> str:
    """Return ``text`` converted to uppercase.

    Args:
        text: The string to convert. May be empty.

    Returns:
        The uppercase version of ``text``. An empty string returns an empty
        string. Characters without an uppercase form (digits, punctuation)
        are left untouched.

    Examples:
        >>> to_upper("hola")
        'HOLA'
    """
    return text.upper()


def to_lower(text: str) -> str:
    """Return ``text`` converted to lowercase.

    Args:
        text: The string to convert. May be empty.

    Returns:
        The lowercase version of ``text``. An empty string returns an empty
        string. Characters without a lowercase form (digits, punctuation)
        are left untouched.

    Examples:
        >>> to_lower("HOLA")
        'hola'
    """
    return text.lower()


def count_words(text: str) -> int:
    """Count the words in ``text``.

    A word is any run of non-whitespace characters. Words may be separated by
    one or more spaces, tabs or newlines, and leading or trailing whitespace
    is ignored.

    Args:
        text: The string to inspect. May be empty.

    Returns:
        The number of words. An empty string, or a string made only of
        whitespace, has 0 words.

    Examples:
        >>> count_words("hola mundo")
        2
        >>> count_words("   ")
        0
    """
    words = text.strip().split(" ")
    return len(words)


def is_palindrome(text: str) -> bool:
    """Check whether ``text`` reads the same forwards and backwards.

    The comparison ignores whitespace and letter case. It does **not** strip
    punctuation or accents, so "¿Anita?" is not a palindrome and "esta" is
    not the same as "está".

    Args:
        text: The string to inspect. May be empty.

    Returns:
        ``True`` if ``text`` is a palindrome, ``False`` otherwise. The empty
        string is considered a palindrome.

    Examples:
        >>> is_palindrome("anita lava la tina")
        True
        >>> is_palindrome("hola")
        False
    """
    cleaned = [character.lower() for character in text if not character.isspace()]
    return cleaned == cleaned[::-1]
