"""
# common fonction and class for me
## credit
- Entat Baptiste
#python min 3.9 ?
"""
from Common import *

import builtins
from io import TextIOWrapper
import os
from typing import Tuple, Union, List, Iterable, Any, overload
from dataclasses import dataclass
import time


class File_manager():

    def __init__(self, file_path: str = ""):
        self._file = file_path
        self._resource: TextIOWrapper = open(self._file, "r")

    def open(self, file_path: str):
        self._file = file_path
        self._resource: TextIOWrapper = open(self._file, "r")

    def read(self):
        if self._resource.readable():
            return self._resource.read()
        else:
            self._resource.close()
            self._resource = open(self._file, 'r')
            return self._resource.read()

    def write(self, data):
        if self._resource.writable():
            self._resource.write(data)
        else:
            self._resource.close()
            self._resource = open(self._file, 'w')
            self._resource.write(data)






class test_overload():
    def __init__(self) -> None:
        pass

    @overload
    def process(self, input: str): ...
    @overload
    def process(self, input: Tuple): ...

    def process(self, input):
        if type(input) == str:
            print("str")
        elif type(input) == tuple:
            print("tuple")
        else:
            raise NotImplementedError()

        # match type(input): #In python 3.10
        #    case str:
        #        print("str")
        #    case tuple:
        #        print("tuple")
        #    case int | float:
        #        print("int or float")
        #    case _:
        #        raise NotImplementedError()





