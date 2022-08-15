from tkinter import *

root = Tk()
root.geometry("800x200")
root.title("Main Window")
root.option_add("*Font", "맑은고딕 20")

# def myClick():
#     myLabel = Label(root, text="Look! I clicked a Button!")
#     myLabel.pack()

# #creating a Label Widget
# myLabel1 = Label(root, text="Hello World")
# myLabel2 = Label(root, text="제 이름은 오영제 입니다.")
# myLabel1.pack()
# myLabel2.pack()

# myButton = Button(root, text="click me", command=myClick)

# myButton.pack()

#--------------- grid -------------------------------
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.grid(row=3, column=2)


#creating a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="제 이름은 오영제 입니다.")

myButton = Button(root, text="click me", command=myClick)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

myButton.grid(row=2, column=1)
#----------------------------------------------------
root.mainloop()
