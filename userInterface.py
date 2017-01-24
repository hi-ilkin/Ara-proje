from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from AllData import SimilarityMatrix as SMM
import Classification_with_weka as classification

def quit(event=None):
    global root
    root.destroy()


# defining options to open or save file
file_opt = options = {}

# default file extension
options['defaultextension'] = '.txt'

# default file types
options['filetypes'] = [('text files', '.txt')]


def open_train(event=None):
    # display a dialog box for file choosing
    txt_file = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), **file_opt)

    # clear text area
    if txt_file:
        # before adding text, enable it
        txt_train.config(state=NORMAL)

        txt_train.delete(1.0, END)

        # open file and write to our text are
        train_set = SMM.openFile(SMM, txt_file, 'train')

        line_num = 1
        for x in train_set:
            txt_train.insert(END, str(line_num)+ '.'+ x + '\n')
            line_num += 1

        # update text widget
        root.update_idletasks()

        # after editing, disable for safety
        txt_train.config(state=DISABLED)

        if txt_test.compare("end-1c", "!=", "1.0"):
            # enabling train button
            btn_train['state'] = 'normal'
        print('train set is loaded')

    else:
        print("File is not exist")


def open_test(event=None):
    # display a dialog box for file choosing
    txt_file = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), **file_opt)

    # clear text area
    if txt_file:
        # before adding text, enable it
        txt_test.config(state=NORMAL)

        txt_test.delete(1.0, END)

        # open file and write to our text are
        test_set = SMM.openFile(SMM, txt_file, 'test')

        line_num = 1
        for x in test_set:
            txt_test.insert(END, str(line_num) + '.' + x + '\n')
            line_num += 1

            # update text widget
            root.update_idletasks()

        # after editing, disable for safety
        txt_test.config(state=DISABLED)

        if txt_train.compare("end-1c", "!=", "1.0"):
            # enabling train button
            btn_train['state'] = 'normal'

        print('Test set is loaded')
    else:
        print("File is not exist")


def save_file(event=None):
    pass


def start_traning():
    print('Active')
    classification.classify()


def start_summary():
    pass


# ---------------- Graphic Interface ------------------------
root = Tk()
root.geometry('700x550')

notebook = ttk.Notebook(root)

btn_frame = Frame(root)
btn_frame.pack(fill='both', side=BOTTOM)

# summary button
btn_summary = Button(btn_frame, state=DISABLED, text="Özetle", width=5, height=2, command=start_summary,
                     background='cornsilk2', activebackground='light grey')
btn_summary.pack(side=RIGHT, fill=X, padx=5, pady=5)

# train button
btn_train = Button(btn_frame, state=DISABLED, text="Eğit", width=5, height=2, command=start_traning,
                   background='cornsilk2', activebackground='light grey')
btn_train.pack(side=RIGHT, padx=5, pady=5)



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
file_menu.add_command(label="Eğitim kümesini ekle...", accelerator='Ctrl+E', command=open_train)
file_menu.add_command(label="Test kümesini ekle...",accelerator='Ctrl+T', command=open_test)
file_menu.add_separator()
file_menu.add_command(label="Sonuçları kaydet...",accelerator='Ctrl+S', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çık",accelerator='Ctrl+Q', command=quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ----------- text areas for train frame --------------
# creating a scroll bar
scrl_train = Scrollbar(train_frame, background='green')

# create text are and connect scroll bar to it
txt_train = Text(train_frame, state=DISABLED, width=600, height=550, yscrollcommand=scrl_train.set, padx=10, pady=10)

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
txt_test = Text(test_frame, state=DISABLED, width=600, height=550, yscrollcommand=scrl_test.set, padx=10, pady=10)

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
txt_classification = Text(classification_frame, state=DISABLED, width=600, height=550,
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
txt_summary = Text(summary_frame, state=DISABLED, width=600, height=550, yscrollcommand=scrl_summary.set, padx=10,
                   pady=10)

# if scroll bar moved, move text
scrl_summary.config(command=txt_summary.yview)

# put scroll bar on the right
scrl_summary.pack(side='right', fill='y')

# add text area to the left
txt_summary.pack(side="left", fill="both", expand=True)


root.bind('<Control-e>', open_train)
root.bind('<Control-t>', open_test)
root.bind('<Control-s>', save_file)
root.bind('<Control-q>', quit)


root.mainloop()
