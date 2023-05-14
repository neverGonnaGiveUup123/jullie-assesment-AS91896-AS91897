import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from title import Heading
from entries import Entries
from select_data import SelectData

class julieGui(ttkb.Window):
    def __init__(self, title="ttkbootstrap", themename="litera", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize, resizable, hdpi, scaling, transient, overrideredirect, alpha)

        self.title('AS91896 & AS91897')

        self.heading = Heading(self)
        self.heading.grid(row=0,column=0,columnspan=2,padx=20,pady=10)

        self.entries = Entries(self)
        self.entries.grid(row=1,column=0,columnspan=2,padx=20,pady=10)

        self.select_data = SelectData(self)
        self.select_data.grid(row=2,column=0,padx=10,pady=10,columnspan=2)

if __name__ == '__main__':
    app = julieGui()
    app.mainloop()