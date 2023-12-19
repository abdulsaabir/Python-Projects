import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

# widgets
label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Last of the labels', background='green')
button = ttk.Button(window, text='Button')

# layout
# label1.pack()
# label2.pack()
# label3.pack()
# button.pack()

# label1.pack(side='top')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top')



# label1.pack(side='left')
# label2.pack(side='left')
# label3.pack(side='left')
# button.pack(side='left')

# --------------------------
# add side right + button 
# --------------------


# EXPAND (TRUE OR FALSE) HOW MUCH SPACE (CAN ) OCCUPY
# SIDE TOP => CAN OCCUPY HEIGHT (AND TAKES THE WIDTH OF THAT HEIGHT)

# label1.pack(side='top', expand=True)
# label2.pack(side='top', )
# label3.pack(side='top', )
# button.pack(side='top', )


# label1.pack(side='top', expand=True)
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top', expand=True)


# change the side ?????????????????  FROM TOP TO LEFT
# SIDE TOP => CAN OCCUPY WEIGHT (AND TAKES THE HEIGHT OF THAT WIDTH)

# label1.pack(side='left', expand=True)
# label2.pack(side='left')
# label3.pack(side='left')
# button.pack(side='left', expand=True)




# FILL (X,Y,BOTH, NONE) HOW MUCH SPACE WILL OCCUPY THAT IS AVAILABLE    

# Ex1 
# label1.pack(side='top', expand=True,fill='x')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top',expand=True)
# # Ex2
# label1.pack(side='top', expand=True,fill='y')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top',expand=True)
# # Ex3
# label1.pack(side='top', expand=True,fill='both')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top',expand=True)



# # ex2
# label1.pack(side='top', expand=True,fill='both')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top',expand=True, fill='y')


# label1.pack(side='top', expand=True,fill='both')
# label2.pack(side='top', fill='x')
# label3.pack(side='top', fill='y')
# button.pack(side='top',expand=True, fill='y')


# exercise
# label1.pack(side='top', fill='x')
# label2.pack(side='top', expand=True)
# label3.pack(side='top', expand=True , fill='both')
# button.pack(side='top',fill='x')


# PADY AND PADX
# label1.pack(side='top', fill='x',pady=50)  # latter Add padx =100
# label2.pack(side='top', expand=True, fill='both')
# label3.pack(side='top', expand=True , fill='both')
# button.pack(side='top',fill='x')



# label1.pack(side='top', fill='x',pady=50)  # latter Add padx =100
# label2.pack(side='top', expand=True, fill='both')
# label3.pack(side='top', expand=True , fill='both')
# button.pack(side='top',fill='x',ipady=40) #
# -------------------------------
# show vs pady applied to the same button
# show pady + padx both applied 
# -------------------------------

# exercise
# order matters
label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')
# run
window.mainloop()