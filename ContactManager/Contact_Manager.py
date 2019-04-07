from tkinter import *
from phones import *

def whichSelected(): # A function that returns the index I mark, so that I can update and delete it
    print("At %s of %d" % (select.curselection(), len(phonelist))) # Let me know what value ן am doing 
    return int(select.curselection()[0]) # Will return the value to me as int that We can send it to other functions

def addEntry(): # To add people
    phonelist.append([nameVar.get(),phoneVar.get()]) # add to the last list
    setSelect() # Reset the scroll box(text box)

def loadEntry(): # show that contact we looking
    name, phone = phonelist[whichSelected()] # take contact from phonelist and put it on variables
    nameVar.set(name)
    phoneVar.set(phone)

def updateEntry():
    phonelist[whichSelected()] = [nameVar.get(),phoneVar.get()]
    setSelect()

def deleteEntry():
    del phonelist[whichSelected()]
    setSelect()

# A function that will create all the widgets (system graphics components)
def makeWindow():
    global nameVar, phoneVar , select #nameVar include name, phoneVar include phone number and select for hower choice
    win =Tk()

    frame1 = Frame(win) # border
    frame1.pack() 

    Label(frame1, text="Name").grid(row=0,column=0, sticky=W) # Create a label that enter frame1 with text name
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar) #text box that we cant write a name
    name.grid(row=0,column=1,sticky=W)

    Label(frame1, text="Phone").grid(row=1,column=0, sticky=W) # Create a label that enter frame1 with text name
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar) #text box that we cant write a phone number
    phone.grid(row=1,column=1,sticky=W)

    frame2 = Frame(win) # window Row for buttons in same frame
    frame2.pack()
    b1 = Button(frame2, text = "Add ", command=addEntry) # first parmeter is for that button inside frame2,parmeter 3 i give the button command to run function when i press it 
    b2 = Button(frame2, text = "Update", command=updateEntry)
    b3 = Button(frame2, text = "Delete", command=deleteEntry)
    b4 = Button(frame2, text = "Load", command=loadEntry)

    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)

    frame3 = Frame(win) # Selection of names
    frame3.pack()
    scroll = Scrollbar(frame3,orient=VERTICAL)
    select = Listbox(frame3, height=6) # text box that contain rows that we can choose the variable
    scroll.config(command=select.yview()) # every time that i want scroll than he give in y line
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)


    return win

def setSelect():
    phonelist.sort() 
    select.delete(0,END) # delete all scroll bar
    for name, phone in phonelist: # loop that run phonelist after sort
        select.insert(END, name) # enter the phoneList by sorted

win = makeWindow()
setSelect()
win.mainloop()