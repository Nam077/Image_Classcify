import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import cv2 as cv
#load the trained model to classify the images
from tensorflow.python.keras.saving.save import load_model
# model= load_model("models/model.h5")
model= load_model("models/model.h5")
model2= load_model("models/modelcifar.h5")
#dictionary to label all the CIFAR-10 dataset classes.
classes = ['Máy bay','Oto','Mèo','Chó','Hoa','Trái cây','Xe máy','Người']
classescifar = {
    0:'Máy bay',
    1:'Xe',
    2:'Chim',
    3:'Mèo',
    4:'Hươu',
    5:'Chó',
    6:'Cóc',
    7:'Ngựa',
    8:'Tàu',
    9:'Xe tải' 
}
 #Creating a dictionary of class names according to the label
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Phân loại hình ảnh ')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
def classifycifar(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model2.predict_classes([image])[0]
    sign = classescifar[pred]
    print(sign)
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_model=Button(top,text="Phân Loại ảnh",command=lambda: classify(file_path),padx=10,pady=5)
    classify_model.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_model.place(relx=0.79,rely=0.46)
    classify_cifar=Button(top,text="Phân Loại ảnh cifar",command=lambda: classifycifar(file_path),padx=10,pady=5)
    classify_cifar.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_cifar.place(relx=0.79,rely=0.35)
    
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
    (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Tải ảnh lên",command=upload_image,
  padx=10,pady=5)
upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Phân Loại hình ảnh",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()