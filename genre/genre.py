""""
Description: An enumeration containing valid Genres.
Author: Ace Faculty
Date: 2024
"""
from enum import Enum

class Genre(Enum):
    """
    An enumeration listing each of the available genres.
    To use:  Genre.GENRE_NAME.  
    Example: Genre.NON_FICTION
    """
    FICTION = 0
    NON_FICTION = 1
    FANTASY = 2
    TRUE_CRIME = 3
