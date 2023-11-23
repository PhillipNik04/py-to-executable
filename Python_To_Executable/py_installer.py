import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import threading
import time

#create the defs for browsing

def browseFiles():
    global pyfile
    filename = fd.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Python files","*.py*"),("all files","*.*")))
    pyfile=str(filename)
    global file_name
    file_name=pyfile.split('/')[-1]
    global label_loc
    if len(file_name)==0:
        label_loc = tk.Label(root, text="Empty", bg="SteelBlue4", fg="white")
        label_loc.config(font=('helvetica', 14))
        canvas1.create_window(120, 60, window=label_loc)
        threading3()
    else:
        label_loc = tk.Label(root, text=file_name, bg="SteelBlue4", fg="white")
        label_loc.config(font=('helvetica', 14))
        canvas1.create_window(120, 60, window=label_loc)



def BrowseImage():
    global file_image
    filename_image = fd.askopenfilename(initialdir = "/", title = "Select an Image", filetypes = (("Icon","*.ico*"),("all files","*.*")))
    global file_image
    file_image=str(filename_image)
    file_name_image=file_image.split('/')[-1]
    global name_label_image
    if len(file_image)==0:
        name_label_image = tk.Label(root, text="Empty", bg="SteelBlue4", fg="white")
        name_label_image.config(font=('helvetica', 14))
        canvas1.create_window(120, 180, window=name_label_image)
        threading5()
    else:
        name_label_image = tk.Label(root, text=file_name_image, bg="SteelBlue4", fg="white")
        name_label_image.config(font=('helvetica', 14))
        canvas1.create_window(120, 180, window=name_label_image)

def image():
    if image_checked.get() == 1:
        button_image.configure(state=NORMAL)
    else:
        button_image.configure(state=DISABLED)
    
def timer1():
    time.sleep(5)
    label1.destroy()

def timer2():
    time.sleep(5)
    label_loc.destroy()

def timer3():
    time.sleep(5)
    label3.destroy()

def timer4():
    time.sleep(5)
    name_label_image.destroy()

def timer5():
    time.sleep(5)
    label4.destroy()

def run():
    if onefile_checked.get() == 1 and noconsole_checked.get() == 1 :
        onefilestate = " --onefile"
        noconsolestate = " --noconsole"
    elif onefile_checked.get() == 1 and noconsole_checked.get() == 0 :
        onefilestate = " --onefile"
        noconsolestate = " "
    elif onefile_checked.get() == 0 and noconsole_checked.get() == 1 :
        onefilestate = " "
        noconsolestate = " --noconsole"
    elif onefile_checked.get() == 0 and noconsole_checked.get() == 0:
        onefilestate = " "
        noconsolestate = " "
    
    try:
        if image_checked.get() == 1:
            if len(file_image)==0:
                global label4
                label4 = tk.Label(root, text="No Image or py", bg="SteelBlue4", fg="white")
                label4.config(font=('helvetica', 14))
                canvas1.create_window(120, 375, window=label4)
                threading6() 
            else:
                filepath=fd.askdirectory(initialdir=r"" ,title="Where to save the Dist folder")
                convert = "pyinstaller" + " --clean --distpath " + filepath + " " + onefilestate + noconsolestate + " --icon=" + file_image + " " + pyfile
                threading5()
        
        
        
        else:
            if len(file_name)==0:
               global label3
               label3 = tk.Label(root, text="No Image or py", bg="SteelBlue4", fg="white")
               label3.config(font=('helvetica', 14))
               canvas1.create_window(120, 375, window=label3)
               threading4() 
            else:    
                filepath=fd.askdirectory(initialdir=r"" ,title="Where to save the Dist folder")
                convert = "pyinstaller" + " --clean --distpath " + filepath + " " + onefilestate + noconsolestate + " " + pyfile
        threading3()
        os.system(' start cmd /k ' + convert)
    except:
         global label1
         label1 = tk.Label(root, text="No Image or py", bg="SteelBlue4", fg="white")
         label1.config(font=('helvetica', 14))
         canvas1.create_window(120, 375, window=label1)
         threading2()

def threading1():
   work1=threading.Thread(target=run)
   work1.start()

def threading2():
    work2=threading.Thread(target=timer1)
    work2.start()


def threading3():
    work3=threading.Thread(target=timer2)
    work3.start()

def threading4():
    work4=threading.Thread(target = timer3)
    work4.start()

def threading5():
    work4=threading.Thread(target=timer4)
    work4.start()

def threading6():
    work5=threading.Thread(target= timer5)
    work5.start()

#creation of the window/canva and labels

root= tk.Tk()
root.resizable(0,0)
root.title("Py Installer")

canvas1 = tk.Canvas(root,highlightthickness=0, width = 240, height = 400, bg="SteelBlue4", relief = 'raised')
canvas1.pack()


# Create a File Explorer and clear buttons
button_explore = Button(root,text = "  Browse File  ",command = browseFiles,bg='green', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(123, 110, window=button_explore)


button_image = Button(root, text="Browse Image",command = BrowseImage,bg="gold",fg="white",font=('helvetica', 14, 'bold'),state=DISABLED)
canvas1.create_window(125,225, window=button_image)


button_run = Button(root, text="Run", command = threading1, bg= "orange", fg = "white", font=('helvetica', 14, 'bold'))
canvas1.create_window(105, 335, window=button_run)

# Create checkbuttons

image_checked = tk.IntVar()
noconsole_checked = tk.IntVar()
onefile_checked = tk.IntVar()

check_image = Checkbutton(root, text = "Image", onvalue = 1, offvalue = 0,variable = image_checked, command = image, bg="SteelBlue4",fg="black",activebackground="SteelBlue4")
canvas1.create_window(85, 150, window=check_image)

check_console = Checkbutton(root, text = "No Console", onvalue = 1, offvalue = 0,variable = noconsole_checked, bg="SteelBlue4",fg="black",activebackground="SteelBlue4")
canvas1.create_window(99, 275, window=check_console)

check_onefile = Checkbutton(root, text = "One File", onvalue = 1, offvalue = 0, variable = onefile_checked, bg = "SteelBlue4", fg = "black", activebackground = "SteelBlue4")
canvas1.create_window(89, 295, window=check_onefile)


root.mainloop()