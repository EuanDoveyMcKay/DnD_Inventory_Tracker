import customtkinter as tk
from PIL import Image

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)
TextFont = tk.CTkFont(family="Office", size=15)
InfoImage = tk.CTkImage(dark_image=Image.open(R"FrontEnd\ImageGraphics\InfoImage.png"))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

InventoryMaster = tk.CTkFrame(  master=root,
                            border_width=2,
                            border_color="darkgrey",
                            fg_color="grey10")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

InvTitle = tk.CTkLabel( master=InventoryMaster,
                        font=TitleFont,
                        justify="center",
                        text="Inventory",
                        width=500)

ItemList = tk.CTkScrollableFrame(   master=InventoryMaster,
                                    width=450,
                                    fg_color="grey10")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MakeItemRecord(text: str="Unnamed", quantity: int=1): # Note to self: The "ItemRecordFrame" is all the stuff for one instance of an item, and all of these are put into "ItemList" frame (the scroll one)

    ItemRecordFrame = tk.CTkFrame(  master=ItemList,
                                    fg_color="grey10")

    ItemName = tk.CTkLabel( master=ItemRecordFrame,
                            font=TextFont,
                            text=text)
    
    InfoButton = tk.CTkButton(  master=ItemRecordFrame,
                                font=TextFont,
                                fg_color="grey10",
                                hover_color="grey10",
                                text="",
                                image=InfoImage,
                                width=10,
                                height=10)
    
    Amount = tk.CTkLabel(master=ItemRecordFrame,
                         font=TextFont,
                         text=f"x {quantity}")

    ItemName.pack(side="left", padx=(0,5))
    InfoButton.pack(side="left", padx=(0,25))
    Amount.pack(side="left")
    ItemRecordFrame.pack(pady=(0,10))
    return ItemName.cget("text") # All the pack stuff is done, then name of the item is returned (just in case i need to do something with)

def Main():
    InvTitle.grid(row=0, column=0, padx=(15,25), pady=(10,10))
    ItemList.grid(row=1, column=0, padx=15, pady=(0,20))
    InventoryMaster.pack()
    root.mainloop()

if __name__ == "__main__":
#    for i in range(50):
#        MakeItemRecord(f"Item {i}")   --> Here for testing purposes
    Main()
    