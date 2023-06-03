import tkinter as tk 
from tkinter import ttk 

# lists of events
# pythontutorial.net/tkinter.tkinter-event-binding/

def get_pos(event):
    print(f'x: {event.x} y:{event.y}')
# window
window = tk.Tk()
window.title("event binding")
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = tk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'A button')
btn.pack()

# events <modifier-event-detail>
#btn.bind('<Alt-KeyPress-a>', lambda event: print(event))
#window.bind('<Motion>', get_pos)

#window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

#exercise
text.bind('<Shift-MouseWheel>' , lambda event: print('Mousewheel'))


# run
window.mainloop()