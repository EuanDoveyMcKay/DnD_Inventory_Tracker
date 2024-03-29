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

    ItemRecordFrame = tk.CTkFrame(  master=ItemList,
                                fg_color="grey10")

    ItemName = tk.CTkLabel( master=ItemRecordFrame,
                        font=TextFont,
                        justify="center",
                        text=text)
    
    ItemDownBtn = tk.CTkButton(master=ItemRecordFrame,
                               font=TextFont,
                               width=15,
                               height=10,
                               fg_color="grey10",
                               hover_color="grey10",
                               text="v")

    ItemCounter = tk.CTkLabel(master=ItemRecordFrame,
                            font=TextFont,
                            text=0)
    
    ItemUpBtn = tk.CTkButton(master=ItemRecordFrame,
                               font=tk.CTkFont(family="Office", size=20),
                               width=15,
                               height=10,
                               fg_color="grey10",
                               hover_color="grey10",
                               text="^",)
    
    ItemAddBtn = tk.CTkButton(master=ItemRecordFrame,
                       font=TextFont,
                       width=25,
                       height=10,
                       corner_radius=20,
                       text="+")

    ItemName.grid(row=0, column=0, padx=(0,10))
    ItemDownBtn.grid(row=0, column=1, pady=(0,2))
    ItemCounter.grid(row=0, column=2)
    ItemUpBtn.grid(row=0, column=3, pady=(8,0))
    ItemAddBtn.grid(row=0, column=4, padx=(10,0))

    ItemRecordFrame.pack()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

SearchEntry.pack(padx=12, pady=(10,15))

ItemList.pack(padx=15, pady=(0,20))
SearchFrame.pack()
root.mainloop()