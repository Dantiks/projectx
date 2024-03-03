from tkinter import *
from tkinter import ttk
import customtkinter
import tkintermapview





def find_location():
    location = entry.get()
    map_widget.set_address(location, marker=True)
    hints.append(location)
    hint_widget.configure(values=hints)



def enter_hint(event):
    location = hint_widget.get()
    map_widget.set_address(location, marker=True)
    entry.delete(0,END)
    entry.insert(0, location)

hints = ['']

window = Tk()
window.title('google maps')
window.geometry('480x800')
# window.resizable(False, False)



map_widget = tkintermapview.TkinterMapView(window, width=800, height=600, corner_radius=0)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.place(x=0, y=0)
hint_widget = ttk.Combobox(window, values=hints, font=('', 15))
hint_widget.place(x=300, y=65, width=525)
  


entry = customtkinter.CTkEntry(window, width=800)
entry.place(x=80, y=20)



button = customtkinter.CTkButton(window, text='find', text_color='white', width=20,
                                 corner_radius=10, command=find_location)
button.place(x=520, y=20)
hint_widget.bind('<<ComboboxSelected>>', enter_hint)



window.mainloop()