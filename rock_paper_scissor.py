from tkinter import *
import random

root = Tk()
root.title("Rock paper scissors!")


welcome_label = Label(root,text = "Welcome to Rock Paper Scissor",font = ("Helvetica",17))
welcome_label.grid(row = 0,column = 5)

play_label = Label(root,text = "Let's Play!",fg = 'green',font = ("Helvetica",12))
play_label.grid(row = 1,column =5,pady = 20)




# Rock function
def rock():
	lbl = Label(root,text = "Your choice: Rock",width = 20).grid(row = 4,column = 5)
	
	# randomise the choice
	choices = ["Rock","Paper","Scissor"]
	x = random.choice(choices)
	comp_label = Label(root,text = "The computer chose: " + x).grid(row = 6,column = 5)



	if x == "Rock":
		result = Label(root,text = "You won! :)",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)
		score += 1
	else:
		result = Label(root,text = "Sorry You Lost :(",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)

	# print the score
	#score_label = Label(root,text = "SCORE: " + str(score),font = ("Helvetica",15)).grid(row = 8,column = 5,pady = 10)


# paper function
def paper():
	lbl = Label(root,text = "Your choice: Paper",width = 20).grid(row = 4,column = 5)

	# randomise the choice
	choices = ["Rock","Paper","Scissor"]
	global x	
	x = random.choice(choices)

	global score

	score = 0

	comp_label = Label(root,text = "The computer chose: " + x).grid(row = 6,column = 5)

	if x == "Paper":
		result = Label(root,text = "You won! :)",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)
		score += 1
	else:
		result = Label(root,text = "Sorry You Lost :(",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)

	# print the score
	#score_label = Label(root,text = "SCORE: " + str(score),font = ("Helvetica",15)).grid(row = 8,column = 5,pady = 10)


# scissor function
def scissor():
	lbl = Label(root,text = "Your choice: Scissor",width = 20).grid(row = 4,column = 5)
	

	choices = ["Rock","Paper","Scissor"]

	# randomise the choice
	global x
	x = random.choice(choices)
	comp_label = Label(root,text = "The computer chose: " + x).grid(row = 6,column = 5)

	global score

	score = 0

	# if choice equals computer's then print result else otherwise
	if x == "Scissor":
		result = Label(root,text = "You won! :)",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)
		score += 1
	else:
		result = Label(root,text = "Sorry You Lost :(",width = 30,font = ("Helvetica",10)).grid(row = 7,column = 5)

	# print the score
	#score_label = Label(root,text = "SCORE: " + str(score),font = ("Helvetica",15)).grid(row = 8,column = 5,pady = 10)


# make rock,paper and scissor buttons
rock_btn = Button(root,text = "ROCK",width = 15,command = rock,bg= 'grey').grid(row = 3,column = 4,pady = 10)
paper_btn = Button(root,text = "PAPER",width = 15,command = paper,bg = 'pink').grid(row = 3,column = 5,pady = 10)
scissor_btn = Button(root,text = "SCISSOR",width = 15,command = scissor,bg = 'yellow').grid(row = 3,column = 6,pady = 10)
		


root.mainloop()
