from tkinter import*
from tkinter import messagebox
import random
root = Tk()
root.geometry('850x600+300+50')
root.title('Typing Speed Test')
root.configure(bg='black')

words = ['Loren', 'Ipsum', 'Married', ' dummy', 'School', 'Understand', 'typesetting', 'Software', 'arrangement', 'left'

      , 'Difficult', 'Worker', 'Teacher', 'Moon', 'Playboy']
random.shuffle(words)
def startGame(event):
    global score, miss
    if(timeLeft ==60):
        time()
    gamePlayDetailLabel.configure(text='Enjoy The Game')
    if(wordEntry.get() == wordLabel['text']):
      score += 1
      scoreCountLabel.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)

def time():
    global timeLeft, score,miss
    if(timeLeft >=11):
        pass
    else:
        timeCountLabel.configure(text=timeLeft)
    if(timeLeft >= 0):
        timeLeft -=1
        timeCountLabel.configure(text=timeLeft)
        timeCountLabel.after(1000, time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} , Miss ={} , Total Score = {}'.format(score, miss, score-miss))
        notific = messagebox.askretrycancel('Notification', 'For play please hit the Retry Button!')
        if(notific== True):
            score= 0
            timeleft= 60
            miss= 0
            timeCountLabel.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)

score= 0
miss= 0
timeLeft= 60
count= 0
sliderWrod= ''


titleLabel= Label(root, text='Welcome to typing speed testing game', bg='black', fg='lawn green', font=('arial', 33 ,'italic bold'))
titleLabel.place(x=10, y=10)


scoreLabel= Label(root, text='Your Score :', bg='black', fg='deep sky blue', font=('arial', 25 ,'italic bold'))
scoreLabel.place(x=10, y=100)
scoreCountLabel= Label(root, text=0, bg='black', fg='white', font=('arial', 25 ,'italic bold'))
scoreCountLabel.place(x=80, y=180)

timeLabel=Label(root, text='Time Left :', bg='black', fg='deep sky blue', font=('arial', 25 ,'italic bold'))
timeLabel.place(x=610, y=100)
timeCountLabel= Label(root, text='60', bg='black', fg='white', font=('arial', 25 ,'italic bold'))
timeCountLabel.place(x=680, y=180)


wordLabel= Label(root, text=words[0], bg='black', fg='red', font=('arial', 25 ,'italic bold'))
wordLabel.place(x=300, y=220)

wordEntry = Entry (root, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordEntry.place(x=220 ,y=300)
wordEntry.focus_set()

gamePlayDetailLabel=Label(root, text='Type Word & Hit Enter Button', bg='black', fg='white', font=('arial', 15 ,'italic bold'))
gamePlayDetailLabel.place(x=260, y=370)

root.bind('<Return>', startGame)
root.mainloop()