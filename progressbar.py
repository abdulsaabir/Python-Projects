import customtkinter as ctk

def update_progress():
    currentvalue = progressbar.get()
    print(currentvalue)
    if currentvalue < 1:
        progressbar.set(currentvalue + 0.01)
        progress_var.set(int(progressbar.get()*100))
        root.after(100,update_progress)
def step_update():
    progressbar.start()


# Create the main window
root = ctk.CTk()
root.title("Progress Bar Demo")

# Create and place GUI elements
progress_var = ctk.IntVar(value=0)
# progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, mode='determinate')

progressbar = ctk.CTkProgressBar(root, orientation="horizontal",mode='determinate')
progressbar.set(0)
progressbar.pack(pady=20)


label = ctk.CTkLabel(root,textvariable=progress_var)
label.pack(pady=10)
start_button = ctk.CTkButton(root, text="Start Progress", command=update_progress)
step_button = ctk.CTkButton(root, text="Start Progress", command=step_update)
step_button.pack(pady=10)
start_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
