from tkinter import *
root = Tk()
root.geometry("580x300")
root.title("Color Picker")


def red():
    lbl['bg'] = "red"
def steelblue():
    lbl['bg'] = "steelblue"
def black():
    lbl['bg'] = "black"
def grey():
    lbl['bg'] = "grey"
def orange():
    lbl['bg'] = "orange"
def yellow():
    lbl['bg'] = "yellow"
def blue():
    lbl['bg'] = "blue"
def lime():
    lbl['bg'] = "lime"
def chocolate():
    lbl['bg'] = "chocolate"
def skyblue():
    lbl['bg'] = "skyblue"
def lightgreen():
    lbl['bg'] = "lightgreen"
def green():
    lbl['bg'] = "green"
def brown():
    lbl['bg'] = "brown"
def white():
    lbl['bg'] = "white"

frame = Frame(root,borderwidth=5,bg="orange")
frame.grid(row=0,column=0)

btn1 = Button(frame,bg="red",width=10,height=5, command=red)
btn1.grid(row=0,column=0)
btn2 = Button(frame,bg="steelblue",width=10,height=5, command=steelblue)
btn2.grid(row=0,column=1)
btn3 = Button(frame,bg="black",width=10,height=5, command=black)
btn3.grid(row=0,column=2)
btn4 = Button(frame,bg="grey",width=10,height=5, command=grey)
btn4.grid(row=0,column=3)
btn5 = Button(frame,bg="orange",width=10,height=5, command=orange)
btn5.grid(row=0,column=4)
btn6 = Button(frame,bg="yellow",width=10,height=5, command=yellow)
btn6.grid(row=0,column=5)
btn7 = Button(frame,bg="blue",width=10,height=5, command=blue)
btn7.grid(row=0,column=6)

btn8 = Button(frame,bg="lime",width=10,height=5, command=lime)
btn8.grid(row=1,column=0)
btn9 = Button(frame,bg="chocolate",width=10,height=5, command=chocolate)
btn9.grid(row=1,column=1)
btn10 = Button(frame,bg="skyblue",width=10,height=5, command=skyblue)
btn10.grid(row=1,column=2)
btn11 = Button(frame,bg="lightgreen",width=10,height=5, command=lightgreen)
btn11.grid(row=1,column=3)
btn12 = Button(frame,bg="green",width=10,height=5, command=green)
btn12.grid(row=1,column=4)
btn13 = Button(frame,bg="brown",width=10,height=5, command=brown)
btn13.grid(row=1,column=5)
btn14 = Button(frame,bg="white",width=10,height=5, command=white)
btn14.grid(row=1,column=6)


lbl = Label(root,text="Change my Color",font=("lucida",14,"bold"))
lbl.grid()

root.mainloop()