import customtkinter as tk

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

# The "Search frame" is essentially the master of this component, it is the top most frame (in that it has no parents / isn't packed into any other frames besides root).
# This is for organisation purposes so that each component does not clash with each other...
# ...every component has their own frame, which is then put into this master frame. So it appears as though they are all in one box, but really they all have their own individual space.

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

def MakeItemRecord(text: str="Unnamed"): # Note to self: The "ItemRecordFrame" is all the stuff for one instance of an item, and all of these are put into the List frame (the scrollable one)
    return tk.CTkLabel( master=ItemRecordFrame,
                        font=TextFont,
                        justify="center",
                        text=text)

TestItem = MakeItemRecord("Test")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

SearchEntry.pack(padx=12, pady=(10,15))
TestItem.pack()

ItemRecordFrame.pack()
ItemList.pack(padx=15, pady=(0,20))
SearchFrame.pack()
root.mainloop()