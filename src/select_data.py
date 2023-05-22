import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import json

# create a frame for the part that displays the data
class SelectData(ttkb.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.customer_names_list = []

        # Open the json file and add all the data to customer_names_list. Then show the items in the dropdown box.
        def dropdown_get_data():
            with open("src/stored_data.json", "r") as file:
                self.customer_names_list = json.load(file)["Customer name"]
            self.display_checkbox.config(values=self.customer_names_list)

        # If there is a selected item, then find the item in the json file and delete only that one. Then refresh the display.
        def delete_button_func():
            if self.display_checkbox.get() == "":
                return 0
            with open("src/stored_data.json", "r") as file:
                data = json.load(file)
                selected_data = self.display_checkbox.get()
                index = data["Customer name"].index(selected_data)
                for keys in data.keys():
                    data[keys].pop(index)
            with open("src/stored_data.json", "w") as file:
                json.dump(data, file)
            self.display_checkbox.set("")
            self.customer_name.config(text="Customer name:")
            self.receipt.config(text="Receipt:")
            self.item_hired.config(text="Hired item:")
            self.hired_item_amount.config(text="Hired item amount:")

        # If there is a selected name, then open the json file, find that name, and display the data under that name.
        # If some entries are too long, then show ... at the end.
        def display_button_func():
            if self.display_checkbox.get() == "":
                return 0
            
            with open("src/stored_data.json", "r") as file:
                json_file = json.load(file)

            for i in json_file["Customer name"]:
                if i == self.display_checkbox.get():
                    target_index = json_file["Customer name"].index(i)

            for keys in json_file.keys():
                for items in json_file[keys]:
                    if len(items) > 18:
                        json_file[keys][json_file[keys].index(items)] = (
                            items[0:16] + "..."
                        )

            self.customer_name.config(
                text="Customer name: " + json_file["Customer name"][target_index]
            )
            self.receipt.config(text="Receipt: " + json_file["Receipt"][target_index])
            self.item_hired.config(
                text="Item hired: " + json_file["Item hired"][target_index]
            )
            self.hired_item_amount.config(
                text="Hired item amount: "
                + json_file["Hired item amount"][target_index]
            )

        # Open the json file and reset everything, then refresh the display
        def delete_all_func():
            with open("src/stored_data.json", "w") as file:
                json.dump(
                    {
                        "Customer name": [],
                        "Receipt": [],
                        "Item hired": [],
                        "Hired item amount": [],
                    },
                    file,
                )
            self.display_checkbox.set("")
            self.customer_name.config(text="Customer name:")
            self.receipt.config(text="Receipt:")
            self.item_hired.config(text="Hired item:")
            self.hired_item_amount.config(text="Hired item amount:")

        # Add all the buttons, labels and dropdown boxes.
        self.display_checkbox = ttkb.Combobox(self, postcommand=dropdown_get_data)
        self.display_checkbox.config(
            values=tuple(self.customer_names_list), state="readonly"
        )
        self.display_checkbox.grid(row=0, column=0, columnspan=2,padx=75,pady=10)

        self.delete_button = ttkb.Button(
            self,
            command=delete_button_func,
            bootstyle=WARNING,
            text="Delete selected data",
            width=20,
        )
        self.delete_button.grid(row=1, column=0, padx=10, pady=10,columnspan=2)

        self.display_button = ttkb.Button(
            self,
            command=display_button_func,
            bootstyle=SUCCESS,
            text="Display selected data",
            width=20,
        )
        self.display_button.grid(row=2, column=0, padx=10, pady=10,columnspan=2)

        self.customer_name = ttkb.Label(self, text="Customer name:")
        self.customer_name.config(font=("Helvetica", 11))
        self.customer_name.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.receipt = ttkb.Label(self, text="Receipt:")
        self.receipt.config(font=("Helvetica", 11))
        self.receipt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.item_hired = ttkb.Label(self, text="Hired item:")
        self.item_hired.config(font=("Helvetica", 11))
        self.item_hired.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.hired_item_amount = ttkb.Label(self, text="Hired item amount:")
        self.hired_item_amount.config(font=("Helvetica", 11))
        self.hired_item_amount.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.del_all_button = ttkb.Button(
            self, text="Delete all", bootstyle=DANGER, width=20, command=delete_all_func
        )
        self.del_all_button.grid(row=7, column=0, padx=10, pady=10,columnspan=2)
