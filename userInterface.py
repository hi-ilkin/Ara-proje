from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import platform


def quit():
    global root
    root.destroy()


# defining options to open or save file
file_opt = options = {}

# default file extension
options['defaultextension'] = '.txt'

# default file types
options['filetypes'] = [('text files', '.txt')]


def open_train():
    # display a dialog box for file choosing
    txt_file = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), **file_opt)

    # clear text area
    if txt_file:
        txt_train.delete(1.0, END)

        # open file and write to our text are
        with open(txt_file, encoding='utf_8') as _file:
            txt_train.insert(0.0, _file.read())

            # update text widget
            root.update_idletasks()
    else:
        print("File is not exist")


def open_test():
    # display a dialog box for file choosing
    txt_file = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), **file_opt)

    # clear text area
    if txt_file:
        txt_test.delete(1.0, END)

        # open file and write to our text are
        with open(txt_file, encoding='utf_8') as _file:
            txt_test.insert(0.0, _file.read())

            # update text widget
            root.update_idletasks()
    else:
        print("File is not exist")


def save_file():
    pass


root = Tk()
root.geometry('800x600')

notebook = ttk.Notebook(root)

input_set_frame = Frame(notebook)
classification_frame = Frame(notebook)
summary_frame = Frame(notebook)

inner_notebook = ttk.Notebook(input_set_frame)

train_frame = Frame(inner_notebook)
test_frame = Frame(inner_notebook)

inner_notebook.add(train_frame, text='Eğitim Kümesi')
inner_notebook.add(test_frame, text='Test Kümesi')
inner_notebook.pack(fill='both', pady=10, padx=2)

notebook.add(input_set_frame, text='Veri seti')
notebook.add(classification_frame, text='Kümeleme')
notebook.add(summary_frame, text='Sınıflandırma')
notebook.pack(fill='both', padx=2)

# ----------- adding menu bar ------------

menu_bar = Menu(root)

# menu item 1
file_menu = Menu(menu_bar, tearoff=0)

# add sub menus to menu item 1
file_menu.add_command(label="Eğitim kümesini ekle...", command=open_train)
file_menu.add_command(label="Test kümesini ekle...", command=open_test)
file_menu.add_separator()
file_menu.add_command(label="Sonuçları kaydet...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çık", command=quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ----------- text areas for train frame --------------
# creating a scroll bar
scrl_train = Scrollbar(train_frame, background='green')

# create text are and connect scroll bar to it
txt_train = Text(train_frame, width=600, height=550, yscrollcommand=scrl_train.set, padx=10, pady=10)

# if scroll bar moved, move text
scrl_train.config(command=txt_train.yview)

# put scroll bar on the right
scrl_train.pack(side='right', fill='y')

# add text area to the left
txt_train.pack(side="left", fill="both", expand=True)

# ----------- text areas for test frame --------------
# creating a scroll bar
scrl_test = Scrollbar(test_frame, background='green')

# create text are and connect scroll bar to it
txt_test = Text(test_frame, width=600, height=550, yscrollcommand=scrl_test.set, padx=10, pady=10)

# if scroll bar moved, move text
scrl_test.config(command=txt_test.yview)

# put scroll bar on the right
scrl_test.pack(side='right', fill='y')

# add text area to the left
txt_test.pack(side="left", fill="both", expand=True)

# ---------- text area for classification frame ---------------
# creating a scroll bar
scrl_classification = Scrollbar(classification_frame)

# create text are and connect scroll bar to it
txt_classification = Text(classification_frame, width=600, height=550,
                          yscrollcommand=scrl_classification.set, padx=10,
                          pady=10)

# if scroll bar moved, move text
scrl_classification.config(command=txt_classification.yview)

# put scroll bar on the right
scrl_classification.pack(side='right', fill='y')

# add text area to the left
txt_classification.pack(side="left", fill="both", expand=True)

# ---------- text area for summary frame ---------------
# creating a scroll bar
scrl_summary = Scrollbar(summary_frame)

# create text are and connect scroll bar to it
txt_summary = Text(summary_frame, width=600, height=550, yscrollcommand=scrl_summary.set, padx=10,
                   pady=10)

# if scroll bar moved, move text
scrl_summary.config(command=txt_summary.yview)

# put scroll bar on the right
scrl_summary.pack(side='right', fill='y')

# add text area to the left
txt_summary.pack(side="left", fill="both", expand=True)

root.mainloop()
