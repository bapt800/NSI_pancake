from Common import *

from dataclasses import dataclass
from typing import Union, Iterable
import time


@dataclass
class emit:
    level: int
    origine: Union[str, None] = None
    info: Union[str, None] = None
    file: Union[str, Iterable[str],  None] = None
    time: Union[str, None] = None

    def __post_init__(self) -> None:
        if self.level == None:
            raise NotImplementedError()
        if self.origine == None:
            self.origine = "unknow"
        if self.info == None:
            self.info = "unknow"
        if self.file == None:
            self.file = "unknow"
        if self.time == None:
            self.time = time.strftime("%H:%M:%S", time.localtime())

    def __getitem__(self, key):
        return getattr(self, key)



class Logger:
    """
    trace -> 0
    warning -> 1
    FatalError -> 2
    """

    def __init__(self) -> None:
        self.save: dict[int, list[emit]] = {0: [], 1: [],
                                            2: [], -1: []}
        self.associateTable: dict[int, str] = {0: "trace", 1: "warning",
                                               2: "fatalError", -1: "undertermined"}

        self.lastEmit: Union[emit, None] = None

    def _add_emit(self, _emit: emit) -> None:
        """
        To be used only by the developer of the class, because there are no verification of the inputs.
        """
        self.save[_emit.level].append(_emit)

        if _emit.level == 2:
            raise InterruptedError(_emit)

    def set_lastEmit(self, _emit: emit):
        self.lastEmit = _emit

    def get_lastEmit(self) -> Union[emit, None]:
        return self.lastEmit

    def add_emit(self, _emit: emit) -> None:
        """
        self, _emit: emit
        self, level: int, info: str, file=None
        """
        try:
            self.associateTable[_emit.level]
        except KeyError:
            print("level", _emit.level, " -> not exist")
            self._add_emit(emit(level=-1, origine=_emit.origine,
                           info=_emit.info, time=_emit.time, file=_emit.file))
        else:
            self._add_emit(_emit=_emit)
            self.set_lastEmit(_emit=_emit)

    def addEmitType(self, level: int, associatedName: str) -> bool:
        try:
            self.associateTable[level]
        except KeyError:
            try:
                self.save[level]
            except KeyError:
                self.associateTable[level] = associatedName
                self.save[level] = []
            else:
                print("nom assoc deja pris")
                return False
        else:
            print("level deja pris")
            return False
        return True

    def getSave(self) -> tuple[dict, dict]:
        return (self.save, self.associateTable)

    def printSave(self) -> None:
        print("--> saved emit")
        for type in self.save:
            for emit in self.save[type]:
                print("    ", type, " -->", str(emit))

        print("end emit <--")


# fake decorator
def emit_printThisEmit(funcEmit):
    """
    Please read this doc befor use !
    This is a decorator but not to use over an function !

    Use this syntaxe:
        decorator(functionToDecorate)(_emit: emit) #please use 'emit' struct

    sample use:
        log = Logger()
        emit_printThisEmit(log.emit)(emit(level=0, info="trace emit exemple", path=__file__))
        >>>
    """
    def wrapper(_emit: emit, *args, **kwargs):
        print("--> this emit")
        print(_emit)
        print("end emit <--")

        return funcEmit(_emit, *args, **kwargs)
    return wrapper


# decorator
def emit_whenUsed(logger: Logger, _emit: emit):
    """
    Emet un signal quand la fonction est appeler
    exemple:
        log = Logger()

        @emit_whenUsed(logger=log, level=0, info="--> sayHello is used <--", path="main.py")
        def myFunction(param):
            print(param)
    """
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            logger.add_emit(_emit)
            return f(*args, **kwargs)
        return wrapped_f
    return wrap
