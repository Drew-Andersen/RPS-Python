from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import random

win = Tk()

win.title('Rock, Paper, Scissors')
win.geometry('800x680')

canvas = Canvas(win, width=800, height=680)
canvas.grid(row=0, column=0)

# name = input('Enter your name: ')

l1 = Label(win, text='Player 1', font=('serif', 25)) # Can change Player 1 to name later
l2 = Label(win, text='Computer', font=('serif', 25))
l3 = Label(win, text='VS', font=('serif', 40))

l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

# Start Image
img_start = Image.open('./images/start-img.jpeg')
img_start = img_start.resize((300, 300))

rev_start = img_start.transpose(Image.FLIP_LEFT_RIGHT)

img_start = ImageTk.PhotoImage(img_start)
rev_start = ImageTk.PhotoImage(rev_start)

# Rock Image
rock = Image.open('./images/rock-img.jpeg')
rock = rock.resize((300, 300))

rev_rock = rock.transpose(Image.FLIP_LEFT_RIGHT)

rock = ImageTk.PhotoImage(rock)
rev_rock = ImageTk.PhotoImage(rev_rock)

# Paper Image
paper = Image.open('./images/paper-img.jpeg')
paper = paper.resize((300, 300))

rev_paper = paper.transpose(Image.FLIP_LEFT_RIGHT)

paper = ImageTk.PhotoImage(paper)
rev_paper = ImageTk.PhotoImage(rev_paper)

# Scissors Image
scissor = Image.open('./images/scissor-img.jpeg')
scissor = scissor.resize((300, 300))

rev_scissor = scissor.transpose(Image.FLIP_LEFT_RIGHT)

scissor = ImageTk.PhotoImage(scissor)
rev_scissor = ImageTk.PhotoImage(rev_scissor)

# Selection Image
selection = Image.open('./images/RPS-select.jpeg')
selection = selection.resize((300, 130))

selection = ImageTk.PhotoImage(selection)

# Placing Starting Images
canvas.create_image(0, 100, anchor=NW, image=img_start)
canvas.create_image(500, 100, anchor=NW, image=rev_start)
canvas.create_image(0, 400, anchor=NW, image=selection)
canvas.create_image(500, 400, anchor=NW, image=selection)

# Game Time
def game(player):
    select = [1, 2, 3]
    computer = random.choice(select)

    # Placing player images
    if player == 1:
        canvas.create_image(0, 100, anchor=NW, image=rock)
    elif player == 2:
        canvas.create_image(0, 100, anchor=NW, image=paper)
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor)
    
    # Placing computer images
    if computer == 1:
        canvas.create_image(500, 100, anchor=NW, image=rev_rock)
    elif computer == 2:
        canvas.create_image(500, 100, anchor=NW, image=rev_paper)
    else:
        canvas.create_image(500, 100, anchor=NW, image=rev_scissor)

    # Functionallity of the game (Who wins: if else)
    if player == computer:
        result = 'Draw'
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        result = 'Player wins!'
    else:
        result = 'Computer wins!'
    
    # Placing result on the canvas
    canvas.create_text(390, 600, text='Result: ' + result, fill="black", font=('serif', 25), tag='result')


# Clear the screen
def clear_screen():
    # remove the result
    canvas.delete('result')

    # Refresh the screen to play again
    canvas.create_image(0, 100, anchor=NW, image=img_start)
    canvas.create_image(500, 100, anchor=NW, image=rev_start)

# Create selections for the game
rock_button = Button(win, text='Rock', command=lambda: game(1))
rock_button.place(x=0, y=505)

paper_button = Button(win, text='Paper', command=lambda: game(2))
paper_button.place(x=100, y=505)

scissors_button = Button(win, text='Scissors', command=lambda: game(3))
scissors_button.place(x=200, y=505)

# Create a clear button
clear_button = Button(win, text='Clear', font=('Times', 15), command=clear_screen, width=50)
clear_button.place(x=370, y=30)

win.mainloop()