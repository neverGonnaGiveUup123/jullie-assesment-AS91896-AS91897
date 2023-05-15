import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import json


class Entries(ttkb.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = ttkb.Label(self,text="Julie's customer info recorder")
        self.title.config(font=('Helvetica', 18))
        self.title.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

        self.customer_name_label = ttkb.Label(self, text="Customer name: ")
        self.customer_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.customer_name_entry = ttkb.Entry(self)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.receipt_label = ttkb.Label(self, text="Receipt: ")
        self.receipt_label.grid(row=2, column=0, padx=10, pady=10)

        self.receipt_entry = ttkb.Entry(self)
        self.receipt_entry.grid(row=2, column=1, padx=10, pady=10)

        self.item_label = ttkb.Label(self, text="Item hired: ")
        self.item_label.grid(row=3, column=0, padx=10, pady=10)

        self.item_entry = ttkb.Entry(self)
        self.item_entry.grid(row=3, column=1, padx=10, pady=10)

        self.item_amount_label = ttkb.Label(self, text="Item hired amount: ")
        self.item_amount_label.grid(row=4, column=0, padx=10, pady=10)

        self.item_amount_entry = ttkb.Entry(self)
        self.item_amount_entry.grid(row=4, column=1, padx=10, pady=10)

        def send_info():
            customer_name = self.customer_name_entry.get()
            receipt = self.receipt_entry.get()
            item = self.item_entry.get()
            item_amount = self.item_amount_entry.get()

            if len(customer_name.strip()) == 0:
                self.error_message.config(text="Customer name is required!")
                return 0
            if receipt.isdigit() == False:
                self.error_message.config(text="The receipt must be a number!")
                return 0
            if len(item.strip()) == 0:
                self.error_message.config(text="Hired item is required!")
                return 0
            if item_amount.isdigit() == False:
                self.error_message.config(text="Hired item amount must be a number!")
                return 0
            if int(item_amount) < 1:
                self.error_message.config(text="Item amount must be greater than 0!")
                return 0
            if int(item_amount) > 500:
                self.error_message.config(text="Item mount cannot be greater than 500!")
                return 0
            
            self.error_message.config(text='No current errors.')
            
            with open('src/stored_data.json', 'r') as file:
                customer_data = json.load(file)
                customer_data['Customer name'].append(customer_name)
                customer_data['Receipt'].append(receipt)
                customer_data['Item hired'].append(item)
                customer_data['Hired item amount'].append(item_amount)
            
            with open('src/stored_data.json', 'w') as file:
                json.dump(customer_data, file)
            

        self.enter_button = ttkb.Button(
            self, text="Enter", bootstyle=INFO, width=20, command=send_info
        )
        self.enter_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.error_message = ttkb.Label(self, text="No current errors.")
        self.error_message.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
