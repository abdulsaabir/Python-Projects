import customtkinter as ctk
root = ctk.CTk()
   

# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

for i in range(total_rows):
    for j in range(total_columns):
        e= ctk.CTkEntry(root, width=200, fg_color='blue',font=('Arial',16,'bold'))
        e.grid(row=i, column=j)
        e.insert("0", str(lst[i][j]))
 


  
# create root window

root.mainloop()