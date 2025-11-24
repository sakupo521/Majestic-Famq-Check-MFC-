from tkinter import *
from tkinter import ttk
import urls

def run():
    urls.open_explorer()
    urls.open_url()
    


root = Tk()
root.geometry('400x200')
root.title('MFC - Majestic Famq Check. DS-sakupa666') # можете менять название как угодно
# root.iconbitmap(r'icon.ico') если хотите добавить иконку то в папку src закидываете картинку с разрешением .ico
root.resizable(False, False)


btn_run = ttk.Button(root, text='Запустить программу', command=run)
btn_run.pack(side=BOTTOM, pady=10)

creator_lbl = ttk.Label(root, text='DS-sakupa666', font=30) # DS создателя не удалейте пожалуйста. Пишите если есть вопросы
creator_lbl.pack(side=TOP)

root.mainloop()