"""
specification LIFO
"""


class Pile:
    def __init__(self) -> None:
        # create a list
        pass

    def is_void(self) -> bool:
        if True:
            return True
        else:
            return False

    def append(self, obj) -> None:
        # just append "obj" to this pile
        pass

    def get(self):
        # return the last obj of this list and delete it
        pass


maPile = Pile()
print(maPile.is_void())  # -> True

maPile.append(5)
print(maPile.is_void())  # -> False

print(maPile.get())  # -> 5
print(maPile.is_void())  # -> True
