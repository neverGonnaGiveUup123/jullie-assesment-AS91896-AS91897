import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from title import Heading

class julieGui(ttkb.Window):
    def __init__(self, title="ttkbootstrap", themename="litera", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize, resizable, hdpi, scaling, transient, overrideredirect, alpha)

        self.title('AS91896 & AS91897')

        self.heading = Heading(self)
        self.heading.pack(padx=10,pady=20)

        

if __name__ == '__main__':
    app = julieGui()
    app.mainloop()