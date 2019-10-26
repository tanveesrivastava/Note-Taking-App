from tkinter import *
import app_1

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

def view_command():
    list1.delete(0,END)
    for row in app_1.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in app_1.search(title_text.get()):
        list1.insert(END,row)

def add_command():
    app_1.insert(title_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get()))

def delete_command():
    app_1.delete(selected_tuple[0])

def update_command():
    app_1.update(selected_tuple[0],title_text.get())

window=Tk()

window.wm_title("Quick Note")

l1=Label(window,text="Enter Note")
l1.grid(row=0,column=0)



title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)



list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
