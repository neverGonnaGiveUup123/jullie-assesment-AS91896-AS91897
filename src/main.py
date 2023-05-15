import ttkbootstrap as ttkb
import json
from ttkbootstrap.constants import *
from entries import Entries
from select_data import SelectData

class julieGui(ttkb.Window):
    def __init__(self, title="ttkbootstrap", themename="litera", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize, resizable, hdpi, scaling, transient, overrideredirect, alpha)

        self.title('AS91896 & AS91897')

        self.entries = Entries(self)
        self.entries.grid(row=0,column=0,padx=20,pady=10)

        self.select_data = SelectData(self)
        self.select_data.grid(row=0,column=1,padx=10,pady=10)

if __name__ == '__main__':
    app = julieGui()
    app.mainloop()