import customtkinter as tk
from tkinter import font

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()

FilterFrame = tk.CTkFrame(  master=root,
                            border_width=2,
                            border_color="darkgrey")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=20)

FilterTitle = tk.CTkLabel(  master=FilterFrame,
                            width= 20,
                            height= 10,
                            corner_radius=10,
                            text="Filter",
                            font=TitleFont,
                            justify="center")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

FilterTitle.pack(padx=50,pady=10)
FilterFrame.pack()
root.mainloop()