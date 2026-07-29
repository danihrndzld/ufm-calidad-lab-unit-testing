"""Input validation rules used across the lab."""

MIN_USERNAME_LENGTH = 5
MAX_USERNAME_LENGTH = 12


def validate_username(name: str) -> bool:
    """Check whether ``name`` is a valid username.

    A username is valid when both rules hold:

    1. It contains letters only. "Letter" follows Python's ``str.isalpha()``
       definition, so accented letters count as letters ("mañana" is valid)
       while digits, spaces, hyphens and underscores do not.
    2. Its length is between 5 and 12 characters, both ends included.

    Args:
        name: The candidate username.

    Returns:
        ``True`` if the username satisfies both rules, ``False`` otherwise.

    Examples:
        >>> validate_username("carlos")
        True
        >>> validate_username("ana")
        False
        >>> validate_username("carlos123")
        False
    """
    if not name.isalpha():
        return False
    return MIN_USERNAME_LENGTH <= len(name) < MAX_USERNAME_LENGTH
