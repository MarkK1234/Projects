import tkinter as tk 
from tkinter import ttk 

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
    #label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    #print(label.config())
def ex_but():
    label['text'] = "some text"
    entry['state'] = 'normal'

# window
window = tk.Tk()
window.title('getting and setting widgets')

# widgets
label = ttk.Label(master = window, text= 'some text')
label.pack()

entry = tk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='a button', command= button_func)
button.pack()

ex_button = ttk.Button(master=window , text="change", command=ex_but)
ex_button.pack()

# run
window.mainloop()