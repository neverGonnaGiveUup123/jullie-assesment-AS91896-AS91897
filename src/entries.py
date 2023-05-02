import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

class Entries(ttkb.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.customer_name_label = ttkb.Label(self,text="Customer name: ")
        self.customer_name_label.grid(row=0,column=0,padx=10,pady=10)

        self.customer_name_entry = ttkb.Entry(self)
        self.customer_name_entry.grid(row=0,column=1,padx=10,pady=10)


        self.receipt_label = ttkb.Label(self,text='Receipt: ')
        self.receipt_label.grid(row=1,column=0,padx=10,pady=10)

        self.receipt_entry = ttkb.Entry(self)
        self.receipt_entry.grid(row=1,column=1,padx=10,pady=10)


        self.item_label = ttkb.Label(self,text='Item hired: ')
        self.item_label.grid(row=2,column=0,padx=10,pady=10)

        self.item_entry = ttkb.Entry(self)
        self.item_entry.grid(row=2,column=1,padx=10,pady=10)


        self.item_amount_label = ttkb.Label(self,text='Item hired amount: ')
        self.item_amount_label.grid(row=3,column=0,padx=10,pady=10)

        self.item_amount_entry = ttkb.Entry(self)
        self.item_amount_entry.grid(row=3,column=1,padx=10,pady=10)