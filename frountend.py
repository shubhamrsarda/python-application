from tkinter import*
import backend
#pinstaller --onefile --windowed frountend.py
def get_selected_row(event):
    try:
        global selected_tupple
        index=list1.curselection()[0]
        selected_tupple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tupple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tupple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tupple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tupple[4])
    except IndexError:
        pass
    #return(selected_tupple)
#    print(index)

def delete_command():
    backend.Delete(selected_tupple[0])

def update_command():
    backend.Update(selected_tupple[0],title_text.get(),auther_text.get(),year_text.get(),ISBN_text.get())

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.Search(title_text.get(),auther_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def add_command():
    backend.Insert(title_text.get(),auther_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
    #list1.insert(END,(title_text.get(),auther_text.get(),year_text.get(),ISBN_text.get()))
window=Tk()

window.wm_title("Book Store")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Auther")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=2,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=2,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

auther_text=StringVar()
e2=Entry(window,textvariable=auther_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=2,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=2,column=3)

list1=Listbox(window,height=6,width=30)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text='View All',width=12,command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text='Search',width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="ADD",width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text='Update',width=12,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text='Exit',width=12,command=window.destroy)
b6.grid(row=8,column=3)



window.mainloop()
