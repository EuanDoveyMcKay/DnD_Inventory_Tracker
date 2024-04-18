import customtkinter as tk
from PIL import Image

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)
TextFont = tk.CTkFont(family="Office", size=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

MasterFrame = tk.CTkFrame(  master=root,
                            border_width=2,
                            border_color="darkgrey",
                            fg_color="grey10")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

InvTitle = tk.CTkLabel( master=MasterFrame,
                        font=TitleFont,
                        justify="center",
                        text="Inventory")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    InvTitle.pack()
    MasterFrame.pack()
    root.mainloop()