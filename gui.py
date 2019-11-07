from tkinter import *
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
from main import ReadData, match
from extractor import extract_features
from PIL import ImageTk, Image

arr_img_name=[]
idx_img=1

def change_img():
    global arr_img_name, idx_img, canvas2, img_on_canvas
    n = len(arr_img_name)-1
    idx_img = (idx_img%n)+1
    # idx_img = ((idx_img+n)%n)+1
    img = ImageTk.PhotoImage(Image.open(arr_img_name[idx_img]))
    canvas2.itemconfig(img_on_canvas, image = img)
    canvas2.image = img

def show():
    global arr_img_name, idx_img, canvas2, img_on_canvas
    window = Toplevel(root)
    window.title("Hasil")
    window.geometry("800x600")
    window.configure(background="#282829")
    canvas1 = Canvas(window,width = 300, height = 300)
    canvas1.pack(side = "left")
    img = ImageTk.PhotoImage(Image.open(arr_img_name[0]))
    canvas1.create_image(150,150, image = img)
    canvas1.image = img

    canvas2 = Canvas(window,width = 300, height = 300)
    canvas2.pack(side = "right")
    img = ImageTk.PhotoImage(Image.open(arr_img_name[idx_img]))
    img_on_canvas = canvas2.create_image(150,150, image = img)
    canvas2.image = img

    Button(
    window,
    text="Next",
    command=change_img,
    border=0,
    activebackground="#282829",
    bg="#282829").pack(side = "bottom")
    # Button(
    # window,
    # text="Next",
    # command=change_img(False),
    # border=0,
    # activebackground="#282829",
    # bg="#282829").pack(side = "bottom")



def compare():
# menampilkan foto
    gagal=False
    global arr_img_name
    arr_img_name = []
    if (len(namaFile.get())==0):
        err_namaFile['text'] = 'Nama file harus diisi\n'
        gagal = True
    else:
        img_name=str(namaFile.get())
        try:
            img = imread(os.path.join(img_name))
            err_namaFile['text'] = ''
        except FileNotFoundError:
            err_namaFile['text'] = 'File tidak ditemukan\n'
            gagal=True
    
    if (len(banyakFoto.get())==0):
        err_banyakFoto['text'] = 'Banyak foto harus diisi\n'
        gagal = True
    else:
        try:
            n_img = int(banyakFoto.get())
            err_banyakFoto['text'] = ''
        except ValueError:
            err_banyakFoto['text'] = 'Masukan harus berupa angka\n'
            gagal=True
    
    if (pilihan.get()==-1):
        err_pilihan['text'] = 'Harap pilih metode pencocokan!'
        gagal = True
    else:
        err_pilihan['text'] = ''

    if (gagal):
        return
    
    arr_img_name.append(img_name)
    vector_extract = extract_features(img_name)
    
    result["text"] = "File foto yang akan diuji:\n"+img_name.split('/')[-1]+'\n'

    pil = int(pilihan.get())
    list_result = match(vector_extract,dict_img,pil)
    print(vector_extract)
    
    if (pil): #euclid
        list_result = sorted(list_result, key=lambda tup: tup[1])
    else:
        list_result = sorted(list_result, key=lambda tup: tup[1], reverse=True)

    result["text"] += "\nFoto yang mirip adalah:\n"
    for i in range(n_img):
        print(list_result[i][0])
        print(list_result[i][1])
        result["text"] += list_result[i][0].split('/')[-1]+'\n'+str(list_result[i][1])+'\n'
        arr_img_name.append(list_result[i][0])    
    show()

def browse_file():
    img_name = filedialog.askopenfilename(initialdir = "data/", title = "Select A File", filetypes =(("jpeg files","*.jpg"),) )
    img_name = "data/"+img_name.split("data/")[-1]
    namaFile.delete(0,END)
    namaFile.insert(0,img_name)
    
# Membaca data
dict_img = ReadData()


root = Tk()
root.geometry("650x500")
root.title("Face Recognition")
root.configure(background="#282829")

Label(root,text="Masukkan direktori file foto : ", font="baloo 10", bg="#282829", fg="white").grid(row=0,column=0,sticky=W,padx=3,pady=10)
namaFile = Entry(root)
namaFile.grid(row=0,column=1,sticky=W, ipady=3)
err_namaFile = Label(root, bg="#282829", fg="white")
err_namaFile.grid(row=1,column=1,sticky=W)
browse = PhotoImage(file="foto/browse.png")
Button(root,text='Browse File',command=browse_file, image=browse, border=0, bg="#282829", activebackground="#282829").grid(row=0,column=2,sticky=W,padx=3)

Label(root,text="Masukkan banyak foto : ", font="baloo 10", bg="#282829", fg="white" ).grid(row=2,column=0,sticky=W,padx=3,pady=10)
banyakFoto = Entry(root)
banyakFoto.grid(row=2,column=1,sticky=W,ipady=3)
err_banyakFoto = Label(root, bg="#282829", fg="white")
err_banyakFoto.grid(row=3,column=1,sticky=W)

pilihan = IntVar()
pilihan.set(-1)
err_pilihan = Label(root, bg="#282829", fg="white")
err_pilihan.grid(row=4,column=0,sticky=W)
cosineON = PhotoImage(file="foto/cosineON.png")
cosineOFF = PhotoImage(file="foto/cosineOFF.png")
euclidianON = PhotoImage(file="foto/euclidianON.png")
euclidianOFF = PhotoImage(file="foto/euclidianOFF.png")

Radiobutton(
    root,
    text="Cosine Similarity",
    variable=pilihan,
    value=0,
    indicatoron=False,
    image=cosineOFF,
    selectimage=cosineON,
    border=0,
    selectcolor="#282829",
    activebackground="#282829",
    highlightbackground="#282829",
    bg="#282829").grid(row=5,column=0,sticky=W)

Radiobutton(
    root, 
    text="Euclidean Distance",
    variable=pilihan,
    value=1,
    indicatoron=False,
    image=euclidianOFF,
    selectimage=euclidianON,
    bd=0,
    selectcolor="#282829",
    activebackground="#282829",
    highlightbackground="#282829",
    bg="#282829").grid(row=5,column=1,sticky=W)

compare_img = PhotoImage(file="foto/compare.png")
Button(
    root,
    text="Compare",
    command=compare,
    image=compare_img,
    border=0,
    activebackground="#282829",
    bg="#282829").grid(row=10,column=0,sticky=W,padx=3,pady=5)
result=Label(root, justify=LEFT, bg="#282829", fg="white")
result.grid(row=11,column=0,sticky=W)

root.mainloop()