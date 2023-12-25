import customtkinter as ctk
root = ctk.CTk()
import random
root.geometry('300x300')

# # take the data
# lst = [(1,'Raj','Mumbai',19),
#        (2,'Aaryan','Pune',18),
#        (3,'Vaishnavi','Mumbai',20),
#        (4,'Rachna','Mumbai',21),
#        (5,'Shubham','Delhi',21)]

# # find total number of rows and
# # columns in list
# total_rows = len(lst)
# total_columns = len(lst[0])

# for i in range(total_rows):
#     for j in range(total_columns):
#         e= ctk.CTkEntry(root, width=200, fg_color='blue',font=('Arial',16,'bold'))
#         e.grid(row=i, column=j)
#         e.insert("0", str(lst[i][j]))

def hideAlldays():
    if checkbox1.get():
        for label in day_labels:
            label.pack_forget()
    else:  # If the checkbox is unchecked
        for label in day_labels:
            label.pack()

def hideRandomDay():
    if checkbox1.get():
        randomDay= random.randint(0,6)
        day_labels[randomDay].pack_forget()
    else:
        for label in day_labels:
            label.pack()


checkbox1 = ctk.CTkCheckBox(root, text='Hide All Days', command=hideAlldays)
checkbox1.pack()
checkbox1 = ctk.CTkCheckBox(root, text='Hide Random Days', command=hideRandomDay)
checkbox1.pack()
 
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_labels = []
for i in days_of_week:
    label = ctk.CTkLabel(root,text=i)
    label.pack()
    day_labels.append(label)

  
# create root window

root.mainloop()