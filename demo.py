import customtkinter as ctk
root = ctk.CTk()
import random
root.geometry('700x100')

def update_random_day_button_state():
    if all(check.get() == 1 for check in day_labels):
        checkbox2.configure(state='disabled')
    else:
        checkbox2.configure(state='normal')

def hideAlldays():
    for check in day_labels:
        check.toggle()

    # checkbox1.configure(text='Uncheck All days' if day_labels[0].get() else 'Check All days')

    if day_labels[0].get():
        checkbox1.configure(text='Uncheck All days')
    else:  
        checkbox1.configure(text='check All days')

    update_random_day_button_state()


def hideRandomDay():
    uncheckeddays = []
    for day in day_labels:
        if not day.get():
            uncheckeddays.append(day)
    # unchecked_days = [day for day in day_labels if not day.get()]

    if uncheckeddays:
        randomDay= random.randint(0,len(uncheckeddays)-1)
        uncheckeddays[randomDay].select()
    
    if all(check.get() == 1 for check in day_labels):
        checkbox1.configure(text='Uncheck All days')

    update_random_day_button_state()
        
        

frame = ctk.CTkFrame(root)
frame.pack(pady=10)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_labels = []
for i in days_of_week:
    label = ctk.CTkCheckBox(frame,text=i)
    label.pack(side='left')
    day_labels.append(label)

checkbox1 = ctk.CTkButton(root, text='check All Days', command=hideAlldays)
checkbox1.pack(side='left')
checkbox2 = ctk.CTkButton(root, text='Select Random Day', command=hideRandomDay)
checkbox2.pack(side='left',padx=10)
 


  
# create root window

root.mainloop()