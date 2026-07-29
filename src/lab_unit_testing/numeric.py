"""Small, pure numeric helpers."""


def is_leap_year(year: int) -> bool:
    """Check whether ``year`` is a leap year in the Gregorian calendar.

    The Gregorian rule has three parts: a year divisible by 4 is a leap year,
    except when it is divisible by 100, unless it is also divisible by 400.
    So 2024 is a leap year, 1900 is not, and 2000 is.

    Args:
        year: A calendar year, for example 1900, 2000 or 2024.

    Returns:
        ``True`` if ``year`` is a leap year, ``False`` otherwise.

    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(1900)
        False
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def clamp(value: int, minimum: int, maximum: int) -> int:
    """Constrain ``value`` to the closed range [``minimum``, ``maximum``].

    Both ends are included: a value equal to ``minimum`` or to ``maximum`` is
    already inside the range and is returned unchanged.

    Args:
        value: The number to constrain.
        minimum: Lower end of the range, included.
        maximum: Upper end of the range, included.

    Returns:
        ``minimum`` if ``value`` falls below it, ``maximum`` if ``value``
        rises above it, otherwise ``value`` itself.

    Raises:
        ValueError: If ``minimum`` is greater than ``maximum``.

    Examples:
        >>> clamp(7, 0, 10)
        7
        >>> clamp(-3, 0, 10)
        0
        >>> clamp(42, 0, 10)
        10
    """
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum")
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
