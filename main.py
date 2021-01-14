from tkinter import *


def start():
    root.bind('<Button-1>', b1)

def b1(event):
    root.title("Левая кнопка мыши")
    canvass.create_oval(event.x-20,event.y-20,event.x+30,event.y+30, fill='lightgrey', outline='white')

def b3(event):
    root.title("Правая кнопка мыши")


def move(event):
    root.title("Движение мышью")


# создаем главное окно программы
root = Tk()
root.title("Заголовок окна программы")
root.geometry('1000x700')

menu = Menu(root)
new_item = Menu(menu)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
menu.add_command(label='Вершины', command=start)
root.config(menu=menu)

canvass = Canvas(root, width=1000, height=700, bg='grey')

root.bind('<Button-3>', b3)
root.bind('<Motion>', move)

canvass.pack()
root.mainloop()