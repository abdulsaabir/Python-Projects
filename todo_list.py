import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def add_task():
    task = entry.get()
    if task:
        task_label = ctk.CTkLabel(frame, text=task)
        task_label.grid(row=row_counter, column=0, pady=5, sticky="W")

        done_button = ctk.CTkButton(frame, text="Done", command=lambda: mark_done(task_label, done_button, edit_button))
        done_button.grid(row=row_counter, column=1, padx=5)

        edit_button = ctk.CTkButton(frame, text="Edit", command=lambda: edit_task(task_label))
        edit_button.grid(row=row_counter, column=2, padx=5)

        delete_button = ctk.CTkButton(frame, text="Delete", command=lambda: delete_task(task_label, done_button, edit_button, delete_button))
        delete_button.grid(row=row_counter, column=3, padx=5)

        entry.delete(0, ctk.END)
        increment_row_counter()

    else:
        CTkMessagebox(title="Warning Message!", message="Please enter a task.", icon="warning")


def mark_done(label, done_button, edit_button):
    label.configure(text_color="gray")
    done_button.configure(state=ctk.DISABLED)
    edit_button.configure(state=ctk.DISABLED)

def edit_task(label):
    current_text = label.cget("text")

    dialog = ctk.CTkInputDialog(text=f'Enter new task: ({current_text})', title="Edit Task")
    new_task = dialog.get_input()  # waits for input
    print(new_task)
    if new_task:
        label.configure(text=new_task)
    elif new_task == '':
        CTkMessagebox(title="Warning Message!", message="Please enter a valid task.", icon="warning")


def delete_task(label, done_button, edit_button, delete_button):


    msg = CTkMessagebox(title="Warning Message!", message="Are you sure you want to delete this task?",icon="warning", option_1="Yes", option_2="No")
    
    confirm = msg.get()
    print(confirm)

    if confirm == 'Yes':
        label.destroy()
        done_button.destroy()
        edit_button.destroy()
        delete_button.destroy()

def increment_row_counter():
    global row_counter
    row_counter += 1

# Create the main window
root = ctk.CTk()
root.title("To-Do List")

# Create and place GUI elements
frame = ctk.CTkFrame(root)
frame.pack(pady=10)

entry = ctk.CTkEntry(frame, width=300)
entry.grid(row=0, column=0, padx=5)

add_button = ctk.CTkButton(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Initialize row counter
row_counter = 1


# Run the Tkinter event loop
root.mainloop()
