"""Lab package for the unit-testing session.

Every public function lives in a small module, but they are re-exported here
so both import styles work::

    from lab_unit_testing.text import to_upper
    from lab_unit_testing import to_upper
"""

from lab_unit_testing.numeric import clamp, is_leap_year
from lab_unit_testing.text import count_words, is_palindrome, to_lower, to_upper
from lab_unit_testing.validators import validate_username

__all__ = [
    "clamp",
    "count_words",
    "is_leap_year",
    "is_palindrome",
    "to_lower",
    "to_upper",
    "validate_username",
]
