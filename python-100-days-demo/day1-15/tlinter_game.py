"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: tlinter_game.py
@time: 2020-5-16 下午 2:00

I'm a green hand
"""

import tkinter
import tkinter.messagebox


def main():
    flag = True

    def change_text():
        nonlocal flag
        flag = not flag
        color, text = ('red', 'hello world') if flag else ('black', 'goodbye world')
        label.config(text=text,fg=color)

    def quit_tkinter():
        if tkinter.messagebox.askokcancel('Tips','are you sure for quit?'):
            top.quit()

    top = tkinter.Tk()
    top.geometry('200x100')
    top.title('little game')

    label = tkinter.Label(top, text='hello world', font='Arial -32', fg='red')
    label.pack(expand=1)

    panel = tkinter.Frame(top)
    panel.pack(side='bottom')
    modify = tkinter.Button(panel, text='modify', command=change_text)
    modify.pack(side='left')

    quit = tkinter.Button(panel, text='quit', command = quit_tkinter)
    quit.pack(side='right')

    tkinter.mainloop()




if __name__ == '__main__':
    main()