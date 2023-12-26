import customtkinter as ctk
root = ctk.CTk()
import random
root.geometry('700x100')

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
    for check in day_labels:
        check.toggle()
        
    if day_labels[0].get():
        checkbox1.configure(text='Uncheck All days')
    else:  
        checkbox1.configure(text='check All days')


def hideRandomDay():
    uncheckeddays = []
    for day in day_labels:
        if not day.get():
            uncheckeddays.append(day)

    if uncheckeddays:
        randomDay= random.randint(0,len(uncheckeddays)-1)
        uncheckeddays[randomDay].select()
        uncheckeddays = []
    
    if all(check.get() == 1 for check in day_labels):
        checkbox1.configure(text='Uncheck All days')
        
        

frame = ctk.CTkFrame(root)
frame.place(relx=0,rely=0,relwidth=1,relheight=0.3)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_labels = []
for i in days_of_week:
    label = ctk.CTkCheckBox(frame,text=i)
    label.pack(side='left')
    day_labels.append(label)

checkbox1 = ctk.CTkButton(root, text='check All Days', command=hideAlldays)
checkbox1.pack(side='bottom')
checkbox2 = ctk.CTkButton(root, text='Select Random Day', command=hideRandomDay)
checkbox2.pack(side='bottom')
 


  
# create root window

root.mainloop()