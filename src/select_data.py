import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import json

class SelectData(ttkb.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.customer_names_list = []

        def refresh_func():
            with open('src/stored_data.json', 'r') as file:
                self.customer_names_list = json.load(file)['Customer name']
            self.display_checkbox.config(values=self.customer_names_list)
        
        def select_data_func():
            self.display_checkbox.config(values=self.customer_names_list)

        def delete_button_func():
            with open('src/stored_data.json', 'r') as file:
                data = json.load(file)
                selected_data = self.display_checkbox.get()
                index = data["Customer name"].index(selected_data)
                for keys in data.keys():
                    data[keys].pop(index)
            with open('src/stored_data.json', 'w') as file:
                json.dump(data,file)


        def display_button_func():
            pass

        self.display_checkbox = ttkb.Combobox(self,postcommand=select_data_func)
        self.display_checkbox.config(values=tuple(self.customer_names_list))
        self.display_checkbox.grid(row=0,column=0,columnspan=2)
        
        self.update_button = ttkb.Button(self,text="Refresh data", command=refresh_func, bootstyle=INFO)
        self.update_button.grid(row=1,column=0,columnspan=2,pady=10)

        self.delete_button = ttkb.Button(self,command=delete_button_func,bootstyle=DANGER, text="Delete selected data")
        self.delete_button.grid(row=3,column=0,padx=10,pady=10)

        self.display_button = ttkb.Button(self,command=display_button_func,bootstyle=SUCCESS, text="Display selected data")
        self.display_button.grid(row=3,column=1,padx=10,pady=10)