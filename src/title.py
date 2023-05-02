import ttkbootstrap as ttkb

class Heading(ttkb.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title = ttkb.Label(self,text="Julie's customer info recorder")
        self.title.config(font=('Helvetica', 18))
        self.title.pack()