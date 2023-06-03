import tkinter as tk 
from tkinter import ttk 

def button_func():
    print('a button was pressed')
def button_hello():
    print('hello')

#create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk lable
label = ttk.Label(master = window, text= 'This is a test')
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk label
label1 = ttk.Label(master = window, text = 'my label')
label1.pack()

# ttk button
#button1 = ttk.Button(master = window, text = 'hello', command = button_hello)
button1 = ttk.Button(master = window, text = 'hello', command = lambda: print('hello'))
button1.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

# run
window.mainloop() #updates the gui checks for events