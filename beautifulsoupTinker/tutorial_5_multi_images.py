from tkinter import *
from PIL import ImageTk, Image

root = Tk()

my_img1 = ImageTk.PhotoImage(Image.open("images/banana.jpg").resize((400, 400)))
my_img2 = ImageTk.PhotoImage(Image.open("images/bird.png").resize((400, 400)))
my_img3 = ImageTk.PhotoImage(Image.open("images/coffee.jpg").resize((400, 400)))
my_img4 = ImageTk.PhotoImage(Image.open("images/puffin.jpg").resize((400, 400)))
my_img5 = ImageTk.PhotoImage(Image.open("images/puffin2.jpg").resize((400, 400)))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# images display
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
# status bar
status = Label(text="image 1 of 5")

current_position = 0  # current image

#forward button
def forward():
    global current_position
    global my_label
    
    if current_position >= 0 and current_position < len(image_list)-1:
        current_position += 1
    else:
        current_position = 0 
        
    status = Label(text=f"image {current_position+1} of {len(image_list)}")
    
    my_label.grid_forget()
    my_label = Label(image=image_list[current_position])
    my_label.grid(row=0, column=0, columnspan=3)
    status.grid(row=2, column=0, columnspan=3)
    return

# backward button
def backward():
    global current_position
    global my_label

    if current_position > 0 and current_position < len(image_list):
        current_position -= 1
    else:
        current_position = len(image_list) - 1
        
    status = Label(text=f"image {current_position+1} of {len(image_list)}")

    my_label.grid_forget()
    my_label = Label(image=image_list[current_position])
    my_label.grid(row=0, column=0, columnspan=3)
    status.grid(row=2, column=0, columnspan=3)
    return

button_back = Button(root, text="<<", command=backward)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

# back, forward button
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3)

root.mainloop()
