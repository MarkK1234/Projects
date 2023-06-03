import tkinter as tk 
from tkinter import ttk 

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x800')

# button
def button_func():
    print('a basic button')
    print(radiovar.get())

button_string = tk.StringVar(value= 'a button with string var')
button = ttk.Button(window, text = ' A simple button', command = button_func, textvariable= button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value= 10)
check1 = ttk.Checkbutton(window,
                         text = 'checkbox 1',
                         command= lambda: print(check_var.get()),
                         variable= check_var,
                         onvalue= 10,
                         offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(window,
                         text='checkbox 2',
                         command= lambda: check_var.set(5))
check2.pack()
 
 # radio buttons
radiovar = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                          text = 'radiobutton1', 
                          value='radio1',
                          variable= radiovar, 
                          command= lambda: print(radiovar.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text = 'radiobutton2', value= 2, variable= radiovar)
radio2.pack()

# exercise radio buttons
def ex_func():
    print(ex_var2.get())
    ex_var2.set(False)

ex_var = tk.StringVar()
ex_var2 = tk.BooleanVar()

radio_ex1 = ttk.Radiobutton(window,
                           text = 'radio ex1',
                           value= 'A',
                           variable=ex_var,
                           command= ex_func)
radio_ex1.pack()
radio_ex2 = ttk.Radiobutton(window,
                            text = 'radio ex2',
                            value= 'B',
                            variable=ex_var,
                            command= ex_func)
radio_ex2.pack()

# exercise check button
check_ex = ttk.Checkbutton(window,
                           text= 'checkbox for exercise',
                           variable= ex_var2,
                           command= lambda: print(ex_var.get()))
check_ex.pack()

# run
window.mainloop()