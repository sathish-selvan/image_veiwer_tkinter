from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image veiwer")
my_image1 = ImageTk.PhotoImage(Image.open("images/picture1.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("images/picture2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("images/picture3.jpg"))

image_list=[my_image1,my_image2,my_image3]


count=0
def forward():
    global count
    global my_lable
    if count<len(image_list)-1:
        count += 1
        print(count)
        my_lable.grid_forget()
        my_lable = Label(image=image_list[count])
        my_lable.grid(row=0,column=0,columnspan=3)
        
        status = Label(root, text="Image {} of {}".format(count+1,len(image_list)),bd=1,relief=SUNKEN,anchor=E)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)    
    else:
        count = count
        print(count)
def back():
    global count
    global my_lable
    if count > 0:
        count -= 1
        print(count)
        my_lable.grid_forget()
        my_lable = Label(image=image_list[count])
        my_lable.grid(row=0,column=0,columnspan=3)
        
        status = Label(root, text="Image {} of {}".format(count+1,len(image_list)),bd=1,relief=SUNKEN,anchor=E)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    else:
        count = count
        print(count)
status = Label(root, text="Image {} of {}".format(count+1,len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_lable = Label(image=image_list[0])
my_lable.grid(row=0,column=0,columnspan=3)

button_back = Button(root,text="<<",command = back)
button_exit = Button(root,text="Exit",command =root.quit)
button_frwd = Button(root,text=">>",command = forward)
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_frwd.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()

