from tkinter import *
app=Tk()
app.title('Ico converter')
app.geometry('300x200')
def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img

    app.img_dir=filedialog.askopenfilename(initialdir='c:',title='select your icon image',filetypes=(
                                                                                          ('PNG Images','*.png'),('JPG Images','*.jpg'),
                                                                                          ('All files','*.*')
                                           ))
    img=Image.open(app.img_dir)
def convt_img():
    from PIL import Image
    img.save(f'{ico_name.get()}.ico',format='ICO',size=[(ico_size.get(), ico_size.get())])

    success=Toplevel()
    success.title('success')

    msg=Label(success, text='Conversion completed!')
    msg.pack()
    success.mainloop()

def Preview():
    prev=Toplevel()
    prev.title('Icon preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')

    prev_lbl=Label(prev,text='chechout your icon!')
    prev_lbl.pack()

    prev.mainloop()

ChooseL=Label(app,text='select your image:')
ChooseL.grid(row=0, column=0,pady=10)
ChooseB=Button(app,text='choose',command=open_img)
ChooseB.grid(row=0, column=1,pady=10)

sizeL=Label(app,text='select a size for the icon')
sizeL.grid(row=1,column=0,pady=10)

ico_size=IntVar()
sizes_option=[16,24,32,48,64,128,255,500]
ico_size.set(32)
size_menu=OptionMenu(app,ico_size,*sizes_option)
size_menu.grid(row=1,column=1,pady=10)

Fnamel=Label(app,text='Enter the icon name:')
Fnamel.grid(row=2, column=0,pady=10)
ico_name=Entry(app)
ico_name.grid(row=2, column=1)
convB=Button(app,text='convert', command=convt_img)
convB.grid(row=3,column=0,pady=10)

prevB=Button(app,text='Preview',command=Preview)
prevB.grid(row=3,column=1,pady=10)
app.mainloop()