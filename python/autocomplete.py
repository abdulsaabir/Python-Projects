import customtkinter as ctk
root = ctk.CTk()

height = 10
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
        b = ctk.CTkButton(root,text='', border_spacing=0, corner_radius=0, border_width=1, fg_color='black' )
        b.grid(row=i, column=j)

root.mainloop()