from tkinter import Tk, Frame, Grid, ttk
from helper import Helper_Window
from solver import Solver_Config

class Entry_Window():
    def __init__(self):
        self._root = Tk()
        self._root.title("Nonogram Helper")
        self._root.grid()

        ttk.Label(
            self._root, text='Nonogram Helper', font=('Arial', 32)
        ).grid(column=1, row=0, columnspan=2, sticky='s', pady=15)
        
        self._menu_frame = ttk.Frame(
            self._root, borderwidth=2, relief='solid'
        )
        self._menu_frame.grid(
            column=1, row=1, columnspan=2,
            ipadx=15, sticky='n'
        )
        self._build_menu_frame()

        self._root.columnconfigure(0, weight=0)
        self._root.columnconfigure(1, weight=1)
        self._root.columnconfigure(2, weight=1)
        self._root.columnconfigure(3, weight=0)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)

        self.run()

    def run(self):
        self._root.mainloop()

    def _build_menu_frame(self):
        helper_button = ttk.Button(
            self._menu_frame, text='Helper', command=self._launch_helper
        ).grid(
            column=0, row=0, sticky='we',
            padx=10, pady=10
        )
        solver_button = ttk.Button(
            self._menu_frame, text='Solver', command=self._launch_solver
        ).grid(
            column=1, row=0, sticky='we',
            padx=10, pady=10
        )

        self._menu_frame.columnconfigure(0, weight=1)
        self._menu_frame.columnconfigure(1, weight=1)

    def _launch_helper(self):
        self._root.destroy()
        Helper_Window()

    def _launch_solver(self):
        self._root.destroy()
        Solver_Config()