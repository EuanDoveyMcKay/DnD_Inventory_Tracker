import customtkinter as tk
from tkinter import font

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)
TextFont = tk.CTkFont(family="Office", size=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

SearchFrame = tk.CTkFrame(  master=root,
                            border_width=2,
                            border_color="darkgrey",
                            fg_color="grey10")

ItemList = tk.CTkScrollableFrame(   master=SearchFrame,
                                    width=350,
                                    fg_color="grey10")

ItemRecordFrame = tk.CTkFrame(  master=ItemList,
                                fg_color="grey10")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

SearchEntry = tk.CTkEntry(  master=SearchFrame,
                            width=400,
                            corner_radius=20,
                            placeholder_text="Search",
                            font=TextFont,
                            justify="center",
                            fg_color="grey10",
                            border_color="grey30",
                            border_width=2)

def MakeItemRecord(text: str="Unnamed"):
    return tk.CTkLabel( master=ItemRecordFrame,
                        font=TextFont,
                        justify="center",
                        text=text)

TestItem = MakeItemRecord("Test")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

SearchEntry.pack(padx=12, pady=(10,15))
ItemList.pack(padx=15, pady=(0,20))
TestItem.pack()

SearchFrame.pack()
ItemRecordFrame.pack()
root.mainloop()