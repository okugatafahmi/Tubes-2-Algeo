from tkinter import *
from tkinter.messagebox import *
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

#pins_alexandra daddario/alexandra daddario0.jpg

def show():
    nama=str(namaFile.get())
    path = 'data/referensi'
    img = imread(os.path.join(nama))
    plt.imshow(img)
    plt.show()
    


root = Tk()
root.geometry("500x300")
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ("jpeg files","*.jpg"))

Label(root,text="Masukkan direktori file foto: ").grid(row=0,column=0)
namaFile = Entry(root)
namaFile.grid(row=0,column=1)

Label(root,text="Masukkan banyak foto: ").grid(row=1,column=0)
banyakFoto = Entry(root)
banyakFoto.grid(row=1,column=1)
Button(root,text='Compare',command=show).grid(row=10,column=0)

result=Label(root)
result.grid(row=2,column=1)
root.mainloop()