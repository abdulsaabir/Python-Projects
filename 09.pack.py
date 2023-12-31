import customtkinter as ctk
app = ctk.CTk()
app.geometry('300x300')



# ====================================== 1 ======================================
# place  => x,y
# place  => x,y width,height
# place => relx, rely
# place => relx, rely, relwidth, relheight
# place => relx, rely, relwidth, relheight , sticky => s,n,e,w, center



# ====================================== 2 ======================================
# window.title
# window.resizable
# lambda function


# ====================================== 3 ======================================
# def printtext():
#     val = txt.get()
#     print(val)
#     txt.set('')

# txt = ctk.StringVar(value='')
# label= ctk.CTkLabel(app,textvariable=txt)
# label.pack()
# text_entry = ctk.CTkEntry(app,textvariable=txt).pack()
# button = ctk.CTkButton(app,text='click', command=printtext).pack()





# ====================================== 3 ======================================
# def checkbox_event():
#     print("checkbox toggled, current value:", check_var.get())

# check_var = ctk.StringVar()
# checkbox = ctk.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
#                                      variable=check_var)
# checkbox.pack()

# onvalue="on", offvalue="off"
# checkbox.configure(state="disabled") # you will see error because .pack() doesn't return anything so make the .pack in seprate line 
# checkbox.select()
# checkbox.deselect()
# checkbox.toggle()




# ====================================== 3 ======================================

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = ctk.StringVar()
radiobutton_1 = ctk.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value='male')
radiobutton_2 = ctk.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value='female')
radiobutton_3 = ctk.CTkRadioButton(app, text="CTkRadioButton 3",
                                             command=radiobutton_event, variable= radio_var, value='none')

radiobutton_1.pack()
radiobutton_2.pack()
radiobutton_3.pack()

 
# select ( selects the value no command action wil be triggered)
# deselect  
# invoke selected the value but also trigers the command






# ====================================== 3 ======================================
# def combobox_callback(choice):
#     print("combobox dropdown clicked:", choice)


# # without variable
# combobox = ctk.CTkComboBox(app, values=["option 1", "option 2"],
#                                      command=combobox_callback)

# # with variable 
# combobox_var = ctk.StringVar(value="option 2")
# combobox = ctk.CTkComboBox(app, values=["option 1", "option 2"],
#                                      command=combobox_callback, variable=combobox_var)
# combobox.pack()
# combobox.set("option 2")




app.mainloop()