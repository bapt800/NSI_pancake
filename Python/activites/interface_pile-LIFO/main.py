import tkinter as tk

def inserer(L, x, i):
    if L[0] == len(L)+1 or i-1 > L[0]:
        return False
    else:
        for k in range(L[0]+1, i, -1):
            L[k] = L[k-1]
        L[i] = x
        L[0] = L[0]+1
        return True


class Pile:
    def __init__(self) -> None:
        self.stack = []

    def void(self) -> bool:
        return len(self.stack) <= 0

    def get_top(self):
        if not self.void():
            return self.stack.pop()

    def empilated(self, value):
        self.stack.append(value)

    def __str__(self) -> str:
        return str(self.stack)


# D:/softwares/Python/python-3.10.0b4.amd64/python.exe -m pip install -U autopep8 --user


class File:
    def __init__(self) -> None:
        self.first_stack: Pile = Pile()
        self.second_stack: Pile = Pile()

    def get_first(self):
        if not self.second_stack.void():
            return self.second_stack.get_top()
        elif self.first_stack.void() == True and self.second_stack.void():
            raise IndexError()
        else:
            while not self.first_stack.void():
                self.second_stack.empilated(self.first_stack.get_top())

    def empilated(self, value):
        self.first_stack.empilated(value)

    def __str__(self) -> str:
        return str(self.first_stack) + str(self.second_stack)


class File_borned:
    def __init__(self, len) -> None:
        self.len_max = len
        self.len = 0
        self.stack = File()

    def empilated(self, value):
        if self.len < self.len_max:
            self.len += 1
            self.stack.empilated(value)
        else:
            raise OverflowError()

    def get_first(self):
        self.len -= 1
        return self.stack.get_first()

    def __str__(self) -> str:
        return str(self.stack)


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("number")

        tk.Entry(self, textvariable=self.var).pack()

        tk.Button(self, text="add", command=self.empilated).pack()
    
    def empilated(self):
        tk.Label(self, text=str(self.var.get())).pack()

app = App()


app.mainloop()

