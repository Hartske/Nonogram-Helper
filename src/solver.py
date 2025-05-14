from tkinter import Tk, Frame, Entry, Grid, ttk, StringVar, Canvas
from tkinter.ttk import Style

class Solver_Config():
    def __init__(self):
        self._root = Tk()
        self._root.title('Nonogram Solver')
        self._col_row = StringVar()
        self.lst = StringVar()
        self._col_row_lst = [[], []]
        
        self._display_frame = ttk.Frame(self._root)
        self._display_frame.grid(column=0, row=0)
        self._build_display_frame()
        
        self._entry_frame = ttk.Frame(self._root)
        self._entry_frame.grid(column=0, row=1)
        self._build_entry_frame()
        
        self.run()

    def run(self):
        self._root.mainloop()
        

    def _build_display_frame(self):
        self.col_display = ttk.Labelframe(
            self._display_frame, text='Columns'
        )
        self.col_display.grid(column=0, row=0, sticky='we')

        ttk.Label(
            self.col_display, text='', width=20
        ).grid(column=0, row=0, padx=5, pady=5)

        self.row_display = ttk.Labelframe(
            self._display_frame, text='Rows'
        )
        self.row_display.grid(column=0, row=1, sticky='we')

        ttk.Label(
            self.row_display, text='', width=20
        ).grid(column=0, row=0, padx=5, pady=5)
    
    def _fill_display_frame(self):
        for widget in self.col_display.winfo_children():
            widget.destroy()
        for widget in self.row_display.winfo_children():
            widget.destroy()

        for e, col_list in enumerate(self._col_row_lst[0]):
            ttk.Label(
                self.col_display, text=col_list, width=20, font=('Arial', 14)
            ).grid(column=0, row=e, padx=5, pady=5)

        for e, col_list in enumerate(self._col_row_lst[1]):
            ttk.Label(
                self.row_display, text=col_list, width=20, font=('Arial', 14)
            ).grid(column=0,row=e, padx=5, pady=5)
            

    def _build_entry_frame(self):
        row = ttk.Radiobutton(
            self._entry_frame, text='Column', variable=self._col_row, value='1'
        ).grid(column=0, row=0)
        col = ttk.Radiobutton(
            self._entry_frame, text='Row', variable=self._col_row, value='2'
        ).grid(column=1, row=0, sticky='e')

        self._col_row.set('1')

        ttk.Label(
            self._entry_frame,
            text='List numbers in column or row. ex: 2,10,1,2', font=('Arial', 20)
        ).grid(
            column=0, row=1, columnspan=3, padx=20
        )

        lst_entry = ttk.Entry(
            self._entry_frame, width=24, textvariable=self.lst, font=('Arial', 20)
        )
        lst_entry.grid(column=0, row=2, columnspan=3, sticky='we', padx=20)

        lst_entry.bind("<KeyRelease>", self.print_entry_text)

        ttk.Button(
            self._entry_frame, text='Confirm Row/Column', command=self._set_list
        ).grid(column=1, row=3)

        ttk.Button(
            self._entry_frame, text='Solve!', command=self._solve
        )


    def _set_list(self):
        _lst = self.lst.get()
        print(f'Sent list: {_lst}')
        try:
            int_list = [int(num.strip()) for num in _lst.split(',')]
            print(f'Converted list: {int_list}')
            print(f'Button value: {self._col_row.get()}')
            button_val = self._col_row.get()
            if button_val == '1':
                self._col_row_lst[0].append(int_list)
            elif button_val == '2':
                self._col_row_lst[1].append(int_list)
            else:
                print('Check fail')
            self._fill_display_frame()
            self.lst.set('')
            print(f'Col/Row list: {self._col_row_lst}')
        except ValueError:
            print("Invalid input format.")

    def print_entry_text(self, *kwargs):
        text = self.lst.get()
        print(text)

    def _solve(self):
        pass

class Solver_Window():
    pass