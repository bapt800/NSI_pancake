import tkinter as tk
from tkinter import Frame, Variable, Widget, font as tkfont
from typing import List
from functools import partial


class SGBDD_GUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        #menubar = MenuBar(self)
        #tk.Tk.config(self, menu=menubar)

        self.sideMenu: SideMenu = SideMenu(self, self)
        self.sideMenu.grid(column=0, row=0)
        self.sideMenu.anchor("n")
        self.sideMenu.set_containerButton([tk.Button(self.sideMenu, text="Go to Page One", command=lambda: self.sideMenu.controller.show_frame("PageOne")),
                                           tk.Button(self.sideMenu, text="add view", command=lambda: self.sideMenu.controller.addView())])
        #command=partial(self.addView, "test", self.show_frame("start"))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.grid(column=1, row=0)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.liveFrames = {"start": StartPage(
            self.container, self), "PageOne": PageOne(self.container, self)}
        self.hide_frame_all()
        self.show_frame("start")

    def hide_frame_all(self):
        for frame in self.liveFrames.values():
            frame.grid_forget()

    def show_frame(self, frame_id):
        self.hide_frame_all()
        self.liveFrames[frame_id].grid(column=1, row=1)

    def addView(self, name=""):
        if name == "":
            #name = input("type a name")
            name = "prof TEST"

        view: View = View(frame_parent=self.container,
                          controller=self, name=name)
        self.liveFrames[view.get_name()] = view.tableView
        self.sideMenu.set_containerButton([tk.Button(
            self.sideMenu, text=view.get_name(), command=lambda: self.sideMenu.controller.show_frame(view.get_name()))])

    def exit(self):
        print("ciao")


class MenuBar(tk.Menu):
    def __init__(self, parent: SGBDD_GUI):
        tk.Menu.__init__(self, parent)
        menu_file = tk.Menu(self, tearoff=0)

        self.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(
            label="Start page", command=lambda: parent.show_frame(frame_id="StartPage"))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.exit())

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=menu_help)
        menu_help.add_command(label="Restart connection",
                              command=lambda: parent.exit())


class SideMenu(tk.Frame):
    def __init__(self, frame_parent: SGBDD_GUI, controller: SGBDD_GUI):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller

        self.frameButton = tk.Frame(self)
        self.frameButton.grid(column=0, row=0)
        self.frameButton.anchor("n")
        
        self.containerButton: List[tk.Button] = []

        self.refreshAll()

    def refreshAll(self):
        for ell in self.frameButton.children.values():
            ell.forget()

        row = 0
        for ell in self.containerButton:
            print(ell)
            ell.grid(column=0, row=row)
            row += 1

    def get_containerButton(self) -> List[tk.Button]:
        return self.containerButton

    def set_containerButton(self, containerButton: List[tk.Button]) -> None:
        self.containerButton = containerButton
        self.refreshAll()
        print("xoork")

    def set_activeButton(self, index):
        raise NotImplementedError()


class StartPage(tk.Frame):

    def __init__(self, frame_parent, controller):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller
        self.label = tk.Label(self, text="This is the start page",
                              font=controller.title_font)

        self.button1 = tk.Button(self, text="Go to Page One",
                                 command=lambda: controller.show_frame("PageOne"))
        self.button2 = tk.Button(self, text="Go to TableView",
                                 command=lambda: controller.show_frame("TableView"))

        self.show()

    def show(self):
        self.label.pack(side="top", fill="x", pady=10)
        self.button1.pack()
        self.button2.pack()


class PageOne(tk.Frame):

    def __init__(self, frame_parent, controller):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class View:
    def __init__(self, frame_parent, controller, name) -> None:
        self.name = name
        self.tableView = TableView(frame_parent, controller)

    def get_name(self):
        return self.name


class TableView(tk.Frame):

    def __init__(self, frame_parent, controller):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller

        self.tableContainer = []

        height = 5
        width = 5
        textvariable = Variable()  # change me !
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = tk.Entry(self, textvariable=textvariable)
                b.grid(row=i, column=j)