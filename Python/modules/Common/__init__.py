"""
# common fonction and class for me
## credit
- Entat Baptiste
#python min 3.9 ?
"""

import builtins
import os
from typing import Tuple, Union, List, Iterable, Any, overload
from dataclasses import dataclass
import time


def input(msg: str = "") -> str:
    """# debug fonction for pyteste"""
    return builtins.input(msg)


# clear screen
def cls():
    """
    # clear console
    - Window and Linux supported
    """
    os.system('cls' if os.name == 'nt' else 'clear')


@dataclass
class char:
    """
    # Provide char type
    """
    _char: str = ""

    def __post_init__(self) -> None:
        if self._char.__len__() == 0 and self._char.__len__() == 1:
            raise MemoryError("len is:", self._char.__len__())

    def __setattr__(self, attr: str, value: Any) -> None:
        self.__dict__[attr] = value
        self.__post_init__()
        super().__setattr__(attr, value)

    def __repr__(self):
        return self._char

    def __str__(self):
        return self._char
