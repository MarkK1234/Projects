import tkinter as tk 
from tkinter import ttk 

def but_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('tkinter Variables')

# tkinter variables
string_var = tk.StringVar()
string_ex = tk.StringVar(value= 'start')

# widgets
label = ttk.Label(master = window, text = 'label' , textvariable = string_var)
label.pack()

entry = ttk.Entry(master= window , textvariable = string_var)
entry.pack()

button = ttk.Button(master= window, text= 'button', command= but_func)
button.pack()

entry_ex = ttk.Entry(master= window, textvariable= string_ex)
entry_ex.pack()
entry_ex2 = ttk.Entry(master= window, textvariable= string_ex)
entry_ex2.pack()
label2 = ttk.Label(master = window, text = 'label' , textvariable = string_ex)
label2.pack()


# run
window.mainloop()