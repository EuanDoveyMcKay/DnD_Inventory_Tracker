import customtkinter as tk
from PIL import Image

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)
TextFont = tk.CTkFont(family="Office", size=15)
SearchImage = tk.CTkImage(dark_image=Image.open(R"FrontEnd\ImageGraphics\SearchImage.png"), size=(15,15))
UpArrowImage = tk.CTkImage(dark_image=Image.open(R"FrontEnd\ImageGraphics\UpArrow.png"), size=(10,10))
DownArrowImage = tk.CTkImage(dark_image=Image.open(R"FrontEnd\ImageGraphics\DownArrow.png"), size=(10,10))

OriginalItems = [] # This stays constant once filled with the item compendium, so that we can always refer to the o.g. list of stuff that can be added

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

def Search():

    for Item in ItemList.winfo_children(): # Unpacks everything in the scrolling frame
            Item.pack_forget()

    if SearchEntry.get() != "":
        for Item in OriginalItems:
            if str(Item).find(SearchEntry.get()) != -1: # If there is something to search for, it will only Re-pack the stuff the has the search box substring in
                MakeItemRecord(Item)

    else:
        for Item in OriginalItems:
            MakeItemRecord(Item)

def MakeItemRecord(text: str="Unnamed"): # Note to self: The "ItemRecordFrame" is all the stuff for one instance of an item, and all of these are put into "ItemList" frame (the scroll one)

    def ResetCounter():
        ItemCounter.configure(text = 0)

    def UpButtonClicked():
        ItemCounter.configure(text = ItemCounter.cget("text")+1)

    def DownButtonClicked():
        if ItemCounter.cget("text") != 0:
            ItemCounter.configure(text = ItemCounter.cget("text")-1)

    ItemRecordFrame = tk.CTkFrame(  master=ItemList,
                                    fg_color="grey10")

    ItemName = tk.CTkLabel( master=ItemRecordFrame,
                            font=TextFont,
                            text=text)

    ItemCounter = tk.CTkButton( master=ItemRecordFrame,
                                font=TextFont,
                                text=0,
                                fg_color="grey10",
                                hover_color="grey10",
                                width=20,
                                height=10,
                                command=ResetCounter) # This is a button so that I can have the user click on it to reset the number to 0, instead of spamming the down arrow
    
    ItemUpBtn = tk.CTkButton(  master=ItemRecordFrame,
                               font=tk.CTkFont(family="Office", size=20),
                               width=15,
                               height=10,
                               fg_color="grey10",
                               hover_color="grey10",
                               text="",
                               image=UpArrowImage,
                               command=UpButtonClicked)
    
    ItemDownBtn = tk.CTkButton( master=ItemRecordFrame,
                                font=TextFont,
                                width=15,
                                height=10,
                                fg_color="grey10",
                                hover_color="grey10",
                                text="",
                                image=DownArrowImage,
                                command= DownButtonClicked)
    
    ItemAddBtn = tk.CTkButton(  master=ItemRecordFrame,
                                font=TextFont,
                                width=25,
                                height=10,
                                corner_radius=20,
                                text="+")

    ItemName.grid(row=0, column=0, padx=(0,10))
    ItemDownBtn.grid(row=0, column=1, pady=(0,2))
    ItemCounter.grid(row=0, column=2)
    ItemUpBtn.grid(row=0, column=3, pady=(0,2))
    ItemAddBtn.grid(row=0, column=4, padx=(10,0))

    ItemRecordFrame.pack()

    return ItemName.cget("text") # All the pack stuff is done, then it returns the name of what has been created so that I can append it to a list if necissary (see "Main" and "Search")

SearchButton = tk.CTkButton(    master=SearchFrame,
                                width=0,
                                corner_radius=10,
                                text="",
                                image=SearchImage,
                                command=Search)

SearchEntry = tk.CTkEntry(  master=SearchFrame,
                            width=300,
                            corner_radius=20,
                            placeholder_text="Search",
                            font=TextFont,
                            justify="center",
                            fg_color="grey10",
                            border_color="grey30",
                            border_width=2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Main():
    SearchEntry.grid(row=0, column=0, padx=(12,0), pady=(10,15))
    SearchButton.grid(row=0, column=1, padx=(0,12), pady=(10,15), sticky="w")

    ItemList.grid(row=1, column=0, columnspan=2, padx=15, pady=(0,20))
    SearchFrame.pack()
    root.mainloop()

if __name__ == "__main__":
#    for i in range(50):
#        OriginalItems.append(MakeItemRecord(f"Item {i}"))  --> Here for testing purposes BUT do note how it's done, you need to ensure the new item is added to the o.g. list when it is
#                                                               added to the compendium
    Main()