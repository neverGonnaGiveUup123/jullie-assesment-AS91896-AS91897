import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from src.entries import Entries
from src.select_data import SelectData
import json

# import all the frames and create the main window
class JulieGui(ttkb.Window):
    def __init__(
        self,
        title="ttkbootstrap",
        themename="litera",
        iconphoto="",
        size=None,
        position=None,
        minsize=None,
        maxsize=None,
        resizable=None,
        hdpi=True,
        scaling=None,
        transient=None,
        overrideredirect=False,
        alpha=1,
    ):
        super().__init__(
            title,
            themename,
            iconphoto,
            size,
            position,
            minsize,
            maxsize,
            resizable,
            hdpi,
            scaling,
            transient,
            overrideredirect,
            alpha,
        )

        # Add the frames to main
        self.title("AS91896 & AS91897")

        self.entries = Entries(self)
        self.entries.grid(row=0, column=0, padx=20, pady=10)

        self.select_data = SelectData(self)
        self.select_data.grid(row=0, column=1, padx=10, pady=10)

        try:
            with open('src/stored_data.json', 'x') as file:
                json.dump({"Customer name" : [], "Receipt" : [], "Item hired" : [], "Hired item amount" : []},file)
        except FileExistsError:
            pass

# Only execute the code if the file is being run directly and not as an import
if __name__ == "__main__":
    app = JulieGui()
    app.mainloop()
