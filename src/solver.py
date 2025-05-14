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
        self.row_display = ttk.Labelframe(
            self._display_frame, text='Rows'
        )
        self.row_display.grid(column=0, row=0, sticky='we')

        self.col_display = ttk.Labelframe(
            self._display_frame, text='Columns'
        )
        self.col_display.grid(column=0, row=1, sticky='we')
    
    def _fill_display_frame(self):
        _row = 0
        for e in self._col_row_lst:
            for j in range(len(self._col_row_lst[0])):
                ttk.Label(
                    self.col_display, text=self._col_row_lst[0][j]
                ).grid(column=0, row=_row)
                _row += 1
            for j in range(len(self._col_row_lst[1])):
                ttk.Label(
                    self.row_display, text=self._col_row_lst[1][j]
                ).grid(column=0, row=_row)
                _row += 1

    def _build_entry_frame(self):
        row = ttk.Radiobutton(
            self._entry_frame, text='Column', variable=self._col_row, value=1
        ).grid(column=0, row=0)
        col = ttk.Radiobutton(
            self._entry_frame, text='Row', variable=self._col_row, value=2
        ).grid(column=1, row=0, sticky='e')

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


    def _set_list(self):
        _lst = self.lst.get()
        print(f'Sent list: {_lst}')
        int_list = [int(num.strip()) for num in _lst.split(',')]
        print(f'Converted list: {int_list}')
        print(f'Button value: {self._col_row.get()}')
        button_val = self._col_row.get()
        if button_val == '1':
            self._col_row_lst[0].append(int_list)
        if button_val == '2':
            self._col_row_lst[1].append(int_list)
        else:
            print('Check fail')
        self._fill_display_frame()
        print(f'Col/Row list: {self._col_row_lst}')

    def print_entry_text(self, *kwargs):
        text = self.lst.get()
        print(text)

class Solver_Window():
    pass