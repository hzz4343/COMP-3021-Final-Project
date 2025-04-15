""""
Description: An enumeration containing valid Borrower Statuses.
Author: Ace Faculty
Date: 2024
"""
from enum import Enum

class BorrowerStatus(Enum):
    """
    An enumeration listing each of the available borrower statuses.
    To use:  BorrowerStatus.GENRE_NAME.  
    Example: BorrowerStatus.MINOR
    Descriptions:
    ACTIVE: A borrower in good standing that has borrowed materials in the last year.
    INACTIVE: A borrower in good standing that has not borrowed materials in the last year.
    DELINQUENT: A borrower with overdue items.
    MINOR: A borrower below the age of 18.
    """
    ACTIVE = 0
    INACTIVE = 1
    DELINQUENT = 2
    MINOR = 3
