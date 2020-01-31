import random
import tkinter


my_colors = ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'white', 'purple', 'pink']
score = 0
time = 30


def color_game(event):
    if time == 30:
        countdown()

    nextColor()


def nextColor():
    global score
    global time

    if time > 0:
        e.focus_set()

        if e.get().lower() == my_colors[1].lower():
            score += 1

        e.delate(0, tkinter.END)
        random.shuffle(my_colors)

        label.config(fg=str(my_colors[1]), text=str(my_colors[0]))

        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global time

    if time > 0:
        time -= 1

        timeLabel.config(text="Time left: "
                              + str(time))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLOR_GAME")

root.geometry("375x200")

instructions = tkinter.Label(root, text="Type in the colour" 
                                        "of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(time), font=('Helvetica', 12))

timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', color_game)
e.pack()

e.focus_set()

root.mainloop()
