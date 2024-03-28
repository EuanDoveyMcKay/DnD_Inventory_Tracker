import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
TitleFont = tk.CTkFont(family="Office", weight="bold", underline=True, size=30)
TextFont = tk.CTkFont(family="Office", size=15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

FilterFrame = tk.CTkFrame(  master=root,
                            border_width=2,
                            border_color="darkgrey",
                            fg_color="gray10")

CheckboxFrame = tk.CTkFrame(    master=FilterFrame,
                                fg_color="gray10")

# The "filter frame" is essentially the master of this component, it is the top most frame (in that it has no parents / isn't packed into any other frames besides root).

# The checkbox frame is the one that contains the ticky boxes seen on screen. Instead of griding them into the master frame, they are gridded into this, and then this is packed into the
# master frame. This is better as it allows them to be rearranged seperately without considering tons of other things like the master title, as they have their own frame.
# Set the checkbox frame fg colour to a contrasting colour like red to see what I mean. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

FilterTitle = tk.CTkLabel(  master=FilterFrame,
                            text="Filter",
                            font=TitleFont,
                            justify="center")

ItemFilter = tk.CTkCheckBox(    master=CheckboxFrame,
                                text="Items",
                                font=TextFont)

WeaponFilter = tk.CTkCheckBox(  master=CheckboxFrame,
                                text="Weapons",
                                font=TextFont)

ArmourFilter = tk.CTkCheckBox(  master=CheckboxFrame,
                                text="Armour",
                                font=TextFont)

ContainerFilter = tk.CTkCheckBox(   master=CheckboxFrame,
                                    text="Containers",
                                    font=TextFont)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

FilterTitle.pack(padx=25,pady=(5,20))

### Everything in the following chunk is the checkbox frame organisation
ItemFilter.grid(row=0, column=0, padx=(10,0), pady=(0,20))
WeaponFilter.grid(row=0, column=1, padx=(0,10), pady=(0,20))
ArmourFilter.grid(row=1, column=0, padx=(10,0), pady=(0,20))
ContainerFilter.grid(row=1,column=1, padx=(0,10), pady=(0,20))
CheckboxFrame.pack(padx=20,pady=(0,10))
###

FilterFrame.pack()
root.mainloop()