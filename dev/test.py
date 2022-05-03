from tkinter import *

main = Tk()
main.geometry('800x600')
main.title('YDITS for Twitter  Ver -')

#Console
console = '----------'

text_log_title = Label(main, text=' <Console log> ')
text_log = Label(main, width = 50, text=console)

text_log_title.grid(row=0, column=0)
text_log.grid(row=1, column=0)

#Settings
text_Settings = Label(main, text=' <Settings> ')
text_Settings.grid(row=0, column=1, columnspan=2)

text_CK = Label(main, text='CONSUMER_KEY')
text_CS = Label(main, text='CONSUMER_SECRET')
text_AT = Label(main, text='ACCESS_TOKEN')
text_AS = Label(main, text='ACCESS_TOKEN_SECRET')

text_CK.grid(row = 1, column = 1)
text_CS.grid(row = 2, column = 1)
text_AT.grid(row = 3, column = 1)
text_AS.grid(row = 4, column = 1)

box_CK = Entry(width=50)
box_CS = Entry(width=50)
box_AT = Entry(width=50)
box_AS = Entry(width=50)

box_CK.grid(row = 1, column = 2)
box_CS.grid(row = 2, column = 2)
box_AT.grid(row = 3, column = 2)
box_AS.grid(row = 4, column = 2)

btn_Settings_save = Button(main, width=20, text='Save')
btn_Settings_save.grid(row=5, column=2)

#main
main.mainloop()
