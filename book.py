#Create ejecutable: pyinstaller book.py --onefile --windowed
import tkinter
import sqlite3
import pandas as pd
from os import remove
import string
from tkinter import messagebox

basededatos = 'books.db'

def stop():
    cursor.close()
    raiz.destroy()

def visualize():
    cursor.execute("SELECT * FROM BOOKS")
    books = cursor.fetchall()
    lista.delete(0,tkinter.END)
    for book in books:
        lista.insert(tkinter.END, book)

def add():
    cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
    if (cursor.fetchall()==[]):
        argumentos = [pantalla1.get(), int(pantalla2.get()), pantalla3.get(), int(pantalla4.get())]
        cursor.execute("INSERT INTO BOOKS VALUES (?,?,?,?,NULL)", argumentos)
        conexion.commit()
    else:
        tkinter.messagebox.showinfo("Error", "Element already exists")

def search():
    argumentos = [pantalla1.get(), pantalla2.get(), pantalla3.get(), pantalla4.get()]
    vacios = 0
    for i in argumentos:
        if (i == ""):
            vacios += 1

    if(vacios == 4):
        tkinter.messagebox.showinfo("Error", "Fill in a selection field")
    
    #It could be better to simplify with OR operator instead of AND, but since I did it that way and it works, I decided to don't modify it.
    #I use something similar in the function delete.
    if (vacios == 3):
        if (pantalla1.get() == "") and (pantalla2.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE ISBN = {int(pantalla4.get())}")
        elif (pantalla1.get() == "") and (pantalla2.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE Author = '{pantalla3.get()}'")
        elif (pantalla1.get() == "") and (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE Year = {int(pantalla2.get())}")
        elif (pantalla2.get() == "") and (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE Title = '{pantalla1.get()}'")

    if (vacios == 2):
        if (pantalla1.get() == "") and (pantalla2.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
        elif (pantalla1.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Year = {pantalla2.get()} AND ISBN = {pantalla4.get()})")
        elif (pantalla1.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Year = {pantalla2.get()} AND Author = '{pantalla3.get()}')")
        elif (pantalla2.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND ISBN = {pantalla4.get()})")
        elif (pantalla2.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Author = '{pantalla3.get()}')")
        elif (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()})")

    if (vacios == 1):
        if (pantalla1.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Year = {pantalla2.get()} AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
        elif (pantalla2.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
        elif (pantalla3.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND ISBN = {pantalla4.get()})")
        elif (pantalla4.get() == ""):
            cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND Author = '{pantalla3.get()}')")

    if (vacios == 0):
        cursor.execute(f"SELECT * FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")

    seleccionados = cursor.fetchall()
    lista.delete(0,tkinter.END)
    for book in seleccionados:
        lista.insert(tkinter.END, book)
    

def delete():
    argumentos = [pantalla1.get(), pantalla2.get(), pantalla3.get(), pantalla4.get()]
    vacios = 0
    for i in argumentos:
        if (i == ""):
            vacios += 1

    if(vacios == 4):
        tkinter.messagebox.showinfo("Error", "Fill in a selection field")
            
    if (vacios == 3):
        if (pantalla1.get() == "") and (pantalla2.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE ISBN = {int(pantalla4.get())}")
            conexion.commit()
        elif (pantalla1.get() == "") and (pantalla2.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE Author = '{pantalla3.get()}'")
            conexion.commit()
        elif (pantalla1.get() == "") and (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE Year = {int(pantalla2.get())}")
            conexion.commit()
        elif (pantalla2.get() == "") and (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE Title = '{pantalla1.get()}'")
            conexion.commit()

    if (vacios == 2):
        if (pantalla1.get() == "") and (pantalla2.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla1.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Year = {pantalla2.get()} AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla1.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Year = {pantalla2.get()} AND Author = '{pantalla3.get()}')")
            conexion.commit()
        elif (pantalla2.get() == "") and (pantalla3.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla2.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Author = '{pantalla3.get()}')")
            conexion.commit()
        elif (pantalla3.get() == "") and (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()})")
            conexion.commit()

    if (vacios == 1):
        if (pantalla1.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Year = {pantalla2.get()} AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla2.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla3.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND ISBN = {pantalla4.get()})")
            conexion.commit()
        elif (pantalla4.get() == ""):
            cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND Author = '{pantalla3.get()}')")
            conexion.commit()

    if (vacios == 0):
        cursor.execute(f"DELETE FROM BOOKS WHERE(Title = '{pantalla1.get()}' AND Year = {pantalla2.get()} AND Author = '{pantalla3.get()}' AND ISBN = {pantalla4.get()})")
        conexion.commit()

def catch(event):
    try:
        global seleccionado
        indice = lista.curselection()[0]
        seleccionado = lista.get(indice)
        pantalla1.delete(0,tkinter.END)
        pantalla1.insert(tkinter.END, seleccionado[0])
        pantalla2.delete(0,tkinter.END)
        pantalla2.insert(tkinter.END, seleccionado[1])
        pantalla3.delete(0,tkinter.END)
        pantalla3.insert(tkinter.END, seleccionado[2])
        pantalla4.delete(0,tkinter.END)
        pantalla4.insert(tkinter.END, seleccionado[3])
    except IndexError:
        pass

def update():
    print(seleccionado[4])
    cursor.execute("UPDATE BOOKS SET Title=?, Year=?, Author=?, ISBN=? WHERE id=?",(pantalla1.get(), pantalla2.get(), pantalla3.get(), pantalla4.get(), seleccionado[4]))
    conexion.commit()

conexion = sqlite3.connect("books.db")
#Crear tabla:
cursor = conexion.cursor()
try:
    cursor.execute("CREATE TABLE BOOKS(Title TEXT, Year INTEGER, Author TEXT, ISBN INTEGER, id INTEGER PRIMARY KEY)")
    conexion.commit()
except:
    pass

#Componente raíz
raiz = tkinter.Tk()
raiz.title("Books")
raiz.geometry('560x350')
raiz.resizable(False,False)

#Etiquetas
etiqueta1 = tkinter.Label(raiz, text="Title")
etiqueta1.config(font="Cortana,20")
etiqueta1.grid(row=0, column=0, columnspan=1, pady=10, padx = 5)

etiqueta2 = tkinter.Label(raiz, text="Year")
etiqueta2.config(font="Cortana,20")
etiqueta2.grid(row=1, column=0, columnspan=1, pady=10, padx = 5)

etiqueta3 = tkinter.Label(raiz, text="Author")
etiqueta3.config(font="Cortana,20")
etiqueta3.grid(row=0, column=2, columnspan=1, pady=10, padx = 5)

etiqueta4 = tkinter.Label(raiz, text="ISBN")
etiqueta4.config(font="Cortana,20")
etiqueta4.grid(row=1, column=2, columnspan=1, pady=10, padx = 5)

#Busquedas
pantalla1 = tkinter.Entry(raiz, font=('arial', 13), borderwidth=2)
pantalla1.grid(row=0, column=1, columnspan=1, pady=10, padx = 5)

pantalla2 = tkinter.Entry(raiz, font=('arial', 13), borderwidth=2)
pantalla2.grid(row=1, column=1, columnspan=1, pady=10, padx = 5)

pantalla3 = tkinter.Entry(raiz, font=('arial', 13), borderwidth=2)
pantalla3.grid(row=0, column=3, columnspan=1, pady=10, padx = 5)

pantalla4 = tkinter.Entry(raiz, font=('arial', 13), borderwidth=2)
pantalla4.grid(row=1, column=3, columnspan=1, pady=10, padx = 5)

#Lista y scrollbar
lista = tkinter.Listbox(raiz, height=12, width=30)
lista.grid(row=2, column=0, rowspan=6, columnspan=2, pady=10, padx = 5)

scrollbar = tkinter.Scrollbar(raiz)
scrollbar.grid(row=2, column=2, rowspan=6)

lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

lista.bind('<<ListboxSelect>>', catch)

#Botones
boton1 = tkinter.Button(raiz, text="Visualize", width=20, height=1, command=visualize)
boton1.grid(row=2, column=3, columnspan=1, padx=10, pady=1)
boton2 = tkinter.Button(raiz, text="Search", width=20, height=1, command=search)
boton2.grid(row=3, column=3, columnspan=1, padx=10, pady=1)
boton3 = tkinter.Button(raiz, text="Add", width=20, height=1, command=add)
boton3.grid(row=4, column=3, columnspan=1, padx=10, pady=1)
boton4 = tkinter.Button(raiz, text="Update", width=20, height=1, command=update)
boton4.grid(row=5, column=3, columnspan=1, padx=10, pady=1)
boton5 = tkinter.Button(raiz, text="Delete", width=20, height=1, command=delete)
boton5.grid(row=6, column=3, columnspan=1, padx=10, pady=1)
boton6= tkinter.Button(raiz, text="Close", width=20, height=1, command=stop)
boton6.grid(row=7, column=3, columnspan=1, padx=10, pady=1)

raiz.mainloop()
cursor.close()