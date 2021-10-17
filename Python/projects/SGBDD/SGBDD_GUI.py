import tkinter as tk
from tkinter import Frame, Variable, Widget, font as tkfont
from typing import Dict, List
from functools import partial


class SGBDD_GUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        # menubar = MenuBar(self)
        # tk.Tk.config(self, menu=menubar)

        self.sideMenu: SideMenu = SideMenu(self, self)
        self.sideMenu.grid(column=0, row=0)
        self.sideMenu.anchor("n")
        self.sideMenu.addTo_containerButton(tk.Button(
            self.sideMenu, text="add view", command=lambda: self.sideMenu.controller.addView()))
        # command=partial(self.addView, "test", self.show_frame("start"))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.grid(column=1, row=0)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.view_container: Dict = {"main": View(
            controller=self, frame_side=self.sideMenu, frame_center=self.container, view_ID="main")}
        self.promoted_view = View(
            controller=self, frame_side=self.sideMenu, frame_center=self.container, view_ID="main")

        self.promote_view("main")

    def show_frame(self):
        self.promoted_view.grid(column=0, row=0)

        # row = 0
        # for k, v in self.promoted_view.frame.children.items():
        #    print("show_frame", k, v)
        #    v.grid(column=0, row=row)
        #    row += 1
        # print("show_frame", "end")

    def destroy_view(self, view_ID):
        self.view_container[view_ID] = None

    def hide_frame_all(self):
        self.container.forget()

    def promote_view(self, view_ID):
        #self.hide_frame_all()
        self.promoted_view = self.view_container[view_ID]
        self.show_frame()

    def addView(self, view_ID=""):
        if view_ID == "":
            # name = input("type a name")
            view_ID = "prof TEST"

        view: View = View(controller=self, frame_side=self.sideMenu,
                          frame_center=self.container, view_ID=view_ID)
        self.view_container[view.ID] = view

        self.sideMenu.addTo_containerButton(tk.Button(self.sideMenu, text=view.ID, command=lambda: self.sideMenu.controller.promote_view(view.ID)))

        self.promote_view(view_ID)

    def exit(self):
        print("ciao")


# class MenuBar(tk.Menu):
#    def __init__(self, parent: SGBDD_GUI):
#        tk.Menu.__init__(self, parent)
#        menu_file = tk.Menu(self, tearoff=0)
#
#        self.add_cascade(label="File", menu=menu_file)
#        menu_file.add_command(
#            label="Start page", command=lambda: parent.show_frame("StartPage"))
#        menu_file.add_separator()
#        menu_file.add_command(label="Exit Application",
#                              command=lambda: parent.exit())
#
#        menu_help = tk.Menu(self, tearoff=0)
#        self.add_cascade(label="Help", menu=menu_help)
#        menu_help.add_command(label="Restart connection",
#                              command=lambda: parent.exit())


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
        # buff = self.frameButton
        # for ell in self.frameButton.children.values():
        #    ell.destroy()
        self.frameButton.forget()

        row = 0
        for ell in self.containerButton:
            print("refreshAll", ell)
            ell.grid(column=0, row=row)
            row += 1
        print("refreshAll", "end")

    def get_containerButton(self) -> List[tk.Button]:
        return self.containerButton

    def addTo_containerButton(self, Button: tk.Button) -> None:
        if len(self.containerButton) == 0:
            self.containerButton.append(Button)
        else:
            AddNewFiche = self.containerButton[-1]
            self.containerButton[-1] = Button
            print("test", AddNewFiche == self.containerButton[-1])
            self.containerButton.append(AddNewFiche)
        self.refreshAll()

    def set_activeButton(self, index):
        raise NotImplementedError()


class StartPage(tk.Frame):

    def __init__(self, frame_parent, controller):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller
        self.label = tk.Label(self, text="This is the start page",
                              font = controller.title_font)

        self.button1=tk.Button(self, text = "Go to Page One",
                                 command = lambda: controller.show_frame("PageOne"))
        self.button2 = tk.Button(self, text="Go to TableView",
                                 command = lambda: controller.show_frame("TableView"))

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


class View(tk.Frame):
    def __init__(self, controller, frame_side, frame_center, view_ID):
        tk.Frame.__init__(self, frame_center)
        self.ID = view_ID
        self.controller = controller
        self.frame_center = frame_center
        self.sideButton = tk.Button(master=frame_side, text="eleves")


# class View:
#    def __init__(self, controller, frame_side, frame_center, view_ID) -> None:
#        self.name = view_ID
#        self.controller = controller
#        self.frame_center = frame_center
#        self.frame = Frame(frame_center)
#        self.sideButton = tk.Button(master=frame_side, text="eleves")
#        self.tableView = TableView(self.frame_center, controller)
#
#    def get_ID(self):
#        return self.name
#
#    def get_Widget(self):
#        return self.frame.children
#
#    def grid(self, column=0, row=0):
#        self.frame = Frame(self.frame_center)
#        self.tableView = TableView(self.frame_center, self.controller)
#        print("me ! me !")
#
#    def forget(self):
#        self.frame.forget()


class TableView(tk.Frame):

    def __init__(self, frame_parent, controller):
        tk.Frame.__init__(self, frame_parent)
        self.controller = controller

        self.tableContainer = []

        self.grid()

    def get_Widget(self):
        print("fuck off !!")

    def Re_grid(self, column=None, row=None):
        height = 5
        width = 5
        textvariable = Variable()  # change me !

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = tk.Entry(self, textvariable=textvariable)
                b.grid(row=i, column=j)
