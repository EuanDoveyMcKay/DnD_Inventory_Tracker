import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.after(0, lambda: root.state('zoomed')) # Setting it to full screen (bordered) automatically
root.title("DnD Inventory Manager")

root.mainloop()