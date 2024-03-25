import customtkinter as tk
from tkinter import font

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()

TextFont = tk.CTkFont(family="Office", size=15)

InvSelectFrame = tk.CTkFrame(    master=root,
                                fg_color="grey10")

Selector = tk.CTkOptionMenu(  master=InvSelectFrame,
                            corner_radius=20,
                            values=["Nugget", "Inej", "Jimminy", "Wagon"],
                            font=TextFont,
                            dropdown_font=TextFont,
                            fg_color="grey10",
                            button_color="grey10",
                            button_hover_color="grey10",
                            dropdown_fg_color="grey10",
                            anchor="center")

Selector.pack(padx=10, pady=10)
InvSelectFrame.pack()

root.mainloop()