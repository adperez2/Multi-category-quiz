import tkinter as tk        #allows us to run the gui
import json                 #allows us to connect .json files to the gui
import sys
from PIL import ImageTk

class MegaQuiz(tk.Tk):          #initializing class variable for quiz

    def __init__(self, *args, **kwargs):            #creating a variable to present arguments
        tk.Tk.__init__(self, *args, **kwargs)       #args uses keywords

        tk.Tk.wm_title(self, "MegaFun Quiz!")       #title of quiz
        self.geometry("500x300")                        #size of gui
        self.highlightbackground="#b19cd9"              #background color
        self.resizable(0,0)                 #unable to open whole tab to resize
        self.correct = 0                #access attributes and instances
        container = tk.Frame(self)          #creating frame for varible container
        container.pack(side="top", fill="both", expand=True)        #background fill
        container.grid_rowconfigure(0, weight=1)        #placement on gui using grid
        container.grid_columnconfigure(0, weight=1)     #placement on gui using grid

        self.frames = {}                #created frames for questions
        for F in (MainPage, MathsQ1, MathsQ2, MathsQ3, MathsQ4, MathsQ5, MathsEnd, MathsQ1A, MathsQ2A,MathsQ3A, MathsQ4A,MathsQ5A,
                  MathsEndA, MathsQ1B, MathsQ2B, MathsQ3B, MathsQ4B, MathsQ5B, MathsEndB, MathsQ1C, MathsQ2C, MathsQ3C, MathsQ4C, MathsQ5C,
                  MathsEndC):           #listed all the frames that will be used throughout the quiz
            page_name = F.__name__               #attribute for page name created
            frame = F(parent=container, controller=self)        #tk frame = container
            self.frames[page_name] = frame          #connects page_names with frame
            frame.grid(row=0, column=0, sticky="nsew")      #placement on gui

        self.show_frame("MainPage")         #display Mainpage

    def show_frame(self, page_name):        #created de function to show the frame in gui
        frame = self.frames[page_name]      #page name
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#b19cd9")
        self.title = tk.Message(self, text="===Welcome to our Quiz!===", anchor="center", width=500, font=100, bg="red")
        self.title.place(x=150,y=0)
        self.title.configure(bg="#ADD8E6")
        self.image = ImageTk.PhotoImage(file="csumbtransparent.png")
        self.img = tk.Label(self, image=self.image, width=500,height=300, bg="#b19cd9", anchor="center")
        self.img.place(x=0,y=0)
        #Play BUTTON
        #these buttons allow user to click on the category they would like to be quized on
        tk.Button(self, text="NBA", width=10,
                        command = lambda: controller.show_frame("MathsQ1"), bg="red", fg="white").grid(column=1, row=11, columnspan=8, pady=20, sticky="nesw")
        tk.Button(self, text="Science", width=10,
                  command=lambda: controller.show_frame("MathsQ1A"), bg="blue",fg="white").grid(column=1, row=15, columnspan=8, pady=20, sticky="nesw")
        tk.Button(self, text="Soccer", width=10,
                  command=lambda: controller.show_frame("MathsQ1B"),bg="yellow",fg="black").grid(column=1, row=19, columnspan=8, pady=20, sticky="nesw")
        tk.Button(self, text="Geography", width=10,
                  command=lambda: controller.show_frame("MathsQ1C"), bg="green",fg="black").grid(column=1, row=23, columnspan=8,  pady=20, sticky="nesw")

class MathsQ1(tk.Frame):            #initialzing variable for NBA category
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffe0")        #background color
        self.q_no = 0
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()
        with open("NBA.json") as f:         #accessing .json file to display NBA questions
            data = json.load(f)             #loads file
        # set the question, options, and answer
        question = (data['question'])           #connects to questions
        options = (data['options'])             #connects to options

        tk.Label(self, text="NBA Question 1") .grid(column=2, row=0)            #label for Math quiz

        tk.Label(self, text=question[self.q_no]) .grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right) .grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong) .grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong) .grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong) .grid(column=6, row=5, sticky="nesw")
    def wrong(self):
        self.controller.show_frame("MathsQ2")
    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEnd'].update_label()
        self.controller.show_frame('MathsQ2')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.
    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:          #when time reaches zero
            sys.exit(self)         #exits gui


class MathsQ2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 1
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()
        with open("NBA.json") as f:
            data = json.load(f)
        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])
        tk.Label(self, text="NBA Question 2") .grid(column=2, row=0)
        tk.Label(self, text=question[self.q_no]) .grid(column=4, row=1, columnspan=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong) .grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right) .grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong) .grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong) .grid(column=6, row=5, sticky="nesw")
    def wrong(self):
        self.controller.show_frame("MathsQ3")
    def right(self):
        self.controller.correct += 1
        # update score label
        self.controller.frames['MathsEnd'].update_label()
        self.controller.show_frame('MathsQ3')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 2
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('NBA.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="NBA Question 3").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.right).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ4")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEnd'].update_label()
        self.controller.show_frame('MathsQ4')

    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 3
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('NBA.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="NBA Question 4").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.right).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ5")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEnd'].update_label()
        self.controller.show_frame('MathsQ5')

    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 4
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('NBA.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="NBA Question 5").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsEnd")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEnd'].update_label()
        self.controller.show_frame('MathsEnd')

    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsEnd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")

        # create label, pack seperately so it can be configured later
        self.score = tk.Label(self)
        self.score.grid(column=1, row=1)
        # initalise using method
        self.update_label()
        tk.Button(self, text="Back To Home",
                        command = lambda: controller.show_frame("MainPage")).grid(column=6, row=10, sticky="nesw", pady=10)

    # new method to update label contents
    def update_label(self):
        self.score.config(text='Congrats you got %s/5' % self.controller.correct)




# This is for button 2
class MathsQ1A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 0
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("Science.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Science Question 1").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ2A")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndA'].update_label()
        self.controller.show_frame('MathsQ2A')

    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ2A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 1
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("Science.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Science Question 2").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ3A")

    def right(self):
        self.controller.correct += 1
        # update score label
        self.controller.frames['MathsEndA'].update_label()
        self.controller.show_frame('MathsQ3A')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ3A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 2
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('Science.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Science Question 3").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.right).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ4A")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndA'].update_label()
        self.controller.show_frame('MathsQ4A')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ4A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 3
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('Science.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Science Question 4").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ5A")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndA'].update_label()
        self.controller.show_frame('MathsQ5A')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ5A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 4
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('Science.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Science Question 5").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsEndA")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndA'].update_label()
        self.controller.show_frame('MathsEndA')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsEndA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")

        # create label, pack seperately so it can be configured later
        self.score = tk.Label(self)
        self.score.grid(column=1, row=1)
        # initalise using method
        self.update_label()
        tk.Button(self, text="Back To Home",
                  command=lambda: controller.show_frame("MainPage")).grid(column=6, row=10, sticky="nesw", pady=10)

    # new method to update label contents

    def update_label(self):
        self.score.config(text='Congrats you got %s/5' % self.controller.correct)




# This is for button 3


class MathsQ1B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 0
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("soccer.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Soccer Question 1").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ2B")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndB'].update_label()
        self.controller.show_frame('MathsQ2B')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ2B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 1
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("soccer.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Soccer Question 2").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.right).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ3B")

    def right(self):
        self.controller.correct += 1
        # update score label
        self.controller.frames['MathsEndB'].update_label()
        self.controller.show_frame('MathsQ3B')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ3B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 2
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('soccer.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Soccer Question 3").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ4B")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndB'].update_label()
        self.controller.show_frame('MathsQ4B')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ4B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 3
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('soccer.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Soccer Question 4").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ5B")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndB'].update_label()
        self.controller.show_frame('MathsQ5B')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui


class MathsQ5B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 4
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('soccer.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Soccer Question 5").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.right).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsEndB")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndB'].update_label()
        self.controller.show_frame('MathsEndB')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsEndB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")

        # create label, pack seperately so it can be configured later
        self.score = tk.Label(self)
        self.score.grid(column=1, row=1)
        # initalise using method
        self.update_label()

        tk.Button(self, text="Back To Home",
                  command=lambda: controller.show_frame("MainPage")).grid(column=6, row=10, sticky="nesw", pady=10)

    # new method to update label contents
    def update_label(self):
        self.score.config(text='Congrats you got %s/5' % self.controller.correct)

# This is for button 4


class MathsQ1C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 0
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("geography.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Geography Question 1").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.right).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ2C")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndC'].update_label()
        self.controller.show_frame('MathsQ2C')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ2C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 1
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open("geography.json") as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Geography Question 2").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.right).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ3C")

    def right(self):
        self.controller.correct += 1
        # update score label
        self.controller.frames['MathsEndC'].update_label()
        self.controller.show_frame('MathsQ3C')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ3C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 2
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('geography.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Geography Question 3").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.right).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ4C")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndC'].update_label()
        self.controller.show_frame('MathsQ4C')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ4C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 3
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('geography.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Geography Question 4").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.right).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.wrong).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")

    def wrong(self):
        self.controller.show_frame("MathsQ5C")

    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndC'].update_label()
        self.controller.show_frame('MathsQ5C')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.

    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui

class MathsQ5C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        self.q_no = 4
        self.timeleft = 90
        self.timeLabel = tk.Label(self)
        self.timeLabel.grid(row=3, column=7)
        self.startGame()

        with open('geography.json') as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])

        tk.Label(self, text="Geography Question 5").grid(column=2, row=0)

        tk.Label(self, text=question[self.q_no]).grid(column=4, row=1, columnspan=5, sticky="nesw")

        tk.Button(self, text=options[self.q_no][0],
                  command=self.wrong).grid(column=4, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][1],
                  command=self.wrong).grid(column=4, row=5, sticky="nesw")
        tk.Button(self, text=options[self.q_no][2],
                  command=self.right).grid(column=6, row=3, sticky="nesw")
        tk.Button(self, text=options[self.q_no][3],
                  command=self.wrong).grid(column=6, row=5, sticky="nesw")
    def wrong(self):
        self.controller.show_frame("MathsEndC")
    def right(self):
        self.controller.correct += 1
        self.q_no += 1
        # update score label
        self.controller.frames['MathsEndC'].update_label()
        self.controller.show_frame('MathsEndC')
    def startGame(self):        #attribute for timer
        if self.timeleft == 90:     #how many seconds
            self.countdown()        # start the countdown timer.
    def countdown(self):                #attribute for countdown
        global timeleft                 #timer displayed
        if self.timeleft > 0:           # if a game is in play
            self.timeleft -= 1          # decrement the timer.
            self.timeLabel.config(text="Time left: " + str(self.timeleft))  # update the time left label
            self.timeLabel.after(1000, self.countdown)  # run the function again after 1 second.
        if self.timeleft == 0:  # when time reaches zero
            sys.exit(self)  # exits gui
class MathsEndC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#FFC2B5")
        # create label, pack seperately so it can be configured later
        self.score = tk.Label(self)
        self.score.grid(column=1, row=1)
        # initalise using method
        self.update_label()
        tk.Button(self, text="Back To Home",
                  command=lambda: controller.show_frame("MainPage")).grid(column=6, row=10, sticky="nesw", pady=10)
    # new method to update label contents
    def update_label(self):
        self.score.config(text='Congrats you got %s/5' % self.controller.correct)
#RUNNING PROGRAM
app = MegaQuiz()
app.mainloop()