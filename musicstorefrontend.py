from tkinter import *
from musicstorebackend import database
import webbrowser

dtb=database("musicstore.db")

def get_selected_row(event):
    try:
        global selected_row
        index=t_list_of_songs.curselection()[0]
        selected_row=t_list_of_songs.get(index)
        e_title.delete(0,END)
        e_title.insert(END,selected_row[1])
        e_author.delete(0, END)
        e_author.insert(END, selected_row[2])
        e_date.delete(0, END)
        e_date.insert(END, selected_row[3])
        e_link.delete(0, END)
        e_link.insert(END, selected_row[4])
    except IndexError:
        pass

def view_command():
    t_list_of_songs.delete(0,END)
    for row in dtb.view_all():
        t_list_of_songs.insert(END,row)

def search_command():
    t_list_of_songs.delete(0,END)
    for row in dtb.search_entry((title_txt.get()),(author_txt.get()),(date_txt.get()),(link_txt.get())):
        t_list_of_songs.insert(END,row)

def add_command():
    dtb.add_entry(title_txt.get()+',',author_txt.get()+',',date_txt.get()+',',link_txt.get())
    t_list_of_songs.delete(0,END)
    t_list_of_songs.insert(END,(title_txt.get()+',',author_txt.get()+',',date_txt.get()+',',link_txt.get()))
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_date.delete(0, END)
    e_link.delete(0, END)
    view_command()

def delete_command():
    dtb.delete(selected_row[0])
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_date.delete(0, END)
    e_link.delete(0, END)
    view_command()

def update_command():
    dtb.update(selected_row[0],title_txt.get(),author_txt.get(),date_txt.get(),link_txt.get())
    view_command()

def web_command():
    webbrowser.open(selected_row[4])

def close_command():
    quit()

window=Tk()

window.title("MusicDataBase")
window.iconbitmap("ico.ico")

label_title=Label(window,text="Title")
label_title.grid(row=0,column=0)
title_txt=StringVar()
e_title=Entry(window,textvariable=title_txt)
e_title.grid(row=0,column=1)

label_author=Label(window,text="Author")
label_author.grid(row=0,column=2)
author_txt=StringVar()
e_author=Entry(window,textvariable=author_txt)
e_author.grid(row=0,column=3)

label_date=Label(window,text="Date")
label_date.grid(row=1,column=0)
date_txt=StringVar()
e_date=Entry(window,textvariable=date_txt)
e_date.grid(row=1,column=1)

label_link=Label(window,text="YT Link")
label_link.grid(row=1,column=2)
link_txt=StringVar()
e_link=Entry(window,textvariable=link_txt)
e_link.grid(row=1,column=3)

t_list_of_songs=Listbox(window,height=10,width=45)
t_list_of_songs.grid(row=3,rowspan=8,columnspan=2)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=2,column=2,rowspan=8,sticky='NS')

scrl_bar=Scrollbar(window, orient="horizontal")
scrl_bar.grid(row=9,columnspan=2,sticky='EW')

t_list_of_songs.bind('<<ListboxSelect>>',get_selected_row)

t_list_of_songs.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=t_list_of_songs.yview)

t_list_of_songs.configure(xscrollcommand=scrl_bar.set)
scrl_bar.configure(command=t_list_of_songs.xview)

b_view_all=Button(window,text="View All",width=15,command=view_command)
b_view_all.grid(row=3,column=3)
b_search_entry=Button(window,text="Search Entry",width=15,command=search_command)
b_search_entry.grid(row=4,column=3)
b_add_entry=Button(window,text="Add Entry",width=15,command=add_command)
b_add_entry.grid(row=5,column=3)
b_update=Button(window,text="Update",width=15,command=update_command)
b_update.grid(row=6,column=3)
b_delete=Button(window,text="Delete",width=15,command=delete_command)
b_delete.grid(row=7,column=3)
b_close=Button(window,text="Close",width=15,command=close_command)
b_close.grid(row=9,column=3)
b_web=Button(window,text="Go To Video",width=15,command=web_command)
b_web.grid(row=8,column=3)

window.resizable(False,False)

window.mainloop()