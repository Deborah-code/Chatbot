import tkinter
from tkinter import * 
import Chat_bot
window = tkinter.Tk()
window.geometry("450x300")
window.title('Depression Chatbot')
#label = tkinter.Label(window, text = Chat_bot.Intro).pack()
l1 = Label(window, text = Chat_bot.Intro, font = ('Arial Bold', 10))
l1.grid(column = 0, row = 0)

txt = Entry(window, width=10)
txt.grid(column =2, row = 0)

bt = Button(window, text = 'Send', command = Chat_bot.bot_response('Hi'))
bt.grid(column = 2, row = 10)

window.mainloop()