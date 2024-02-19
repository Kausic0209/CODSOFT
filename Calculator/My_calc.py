#Lets make Calculator

#for provide GUI 
from tkinter import *

# click function
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            if scvalue.get().isnumeric():
                value = int(scvalue.get())
            else:
                value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
 
 #geometrical size of calc
root = Tk()
root.geometry("400x450")
root.title("Kausic Calc.")  #for Title

#for input the characters
scvalue = StringVar()
scvalue.set("")
#font of buttons
screen = Entry(root, textvar=scvalue, font=("Arial", 24), bd=5, relief=RIDGE)
screen.pack(fill=X, ipadx=10, ipady=10, padx=10)

#frame of calc button
f = Frame(root, bg="light grey")

#size&font of "7" button
b = Button(f, text="7", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "8" button
b = Button(f, text="8", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "9" button
b = Button(f, text="9", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "+" button
b = Button(f, text="+", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="light grey")

#size&font of "4" button
b = Button(f, text="4", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "5" button
b = Button(f, text="5", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "6" button
b = Button(f, text="6", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "-" button
b = Button(f, text="-", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="light grey")

#size&font of "1" button
b = Button(f, text="1", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "2" button
b = Button(f, text="2", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "3" button
b = Button(f, text="3", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "*" button
b = Button(f, text="*", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="light grey")

#size&font of "0" button
b = Button(f, text="0", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "." button
b = Button(f, text=".", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "/" button
b = Button(f, text="/", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "%" button
b = Button(f, text="%", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="light grey")

#size&font of "=" button
b = Button(f, text="=", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

#size&font of "C" button
b = Button(f, text="C", padx=15, pady=10, font=("Arial", 16), bd=3, relief=RAISED)
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
#THANK YOU