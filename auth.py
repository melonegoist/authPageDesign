from tkinter import * 
from widget_winfo import widget_w, widget_h
import sqlite3

w = 400
h = 300

bg = '#1F1D36'
purple = '#3f3351' 
pink = '#864879'
peach = '#e9a6a6'

sc = Tk()
sc.geometry(f"{w}x{h}")
sc.resizable(False, False)
sc.configure(bg = f'{bg}')


counter = 1
def dark_toggle():
    global counter, theme
    if counter % 2 == 1:
        theme = 'dark'
        dark_toggle_bttn['bg'] = f'{purple}'
        dark_toggle_label['text'] = 'off'
        dark_toggle_label['bg'] = f'{purple}'
    else:
        theme = 'light'
        dark_toggle_bttn['bg'] = f'{pink}'
        dark_toggle_label['bg'] = f'{pink}'
        dark_toggle_label['text'] = 'on'

    counter += 1

    


def go():
    global theme
    login = login_e.get()
    password = password_e.get()
    

    db = sqlite3.connect('db2.db')
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT,
        password TEXT,
        theme TEXT
    )""")
    db.commit()

    sql.execute(f"SELECT login FROM users WHERE login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES ('{login}', '{password}', '{theme}')")
        db.commit()
    else:
        print('this user is already registered')


    user_list = []

    for user in sql.execute("SELECT * FROM users"):
        user_list.insert(len(user_list), user)

    print(user_list)

    for i in range(0, len(user_list)):
        for j in range(0,2):
            if user_list[i][j] == login:
                theme = user_list[i][2]
                break
    
    print(theme)




login_l = Label(text = 'Login', bg = f'{bg}',
            fg = f'{peach}', font = ('Verdana', 15),
            width = 20)

password_l = Label(text = 'Password', bg = f'{bg}',
            fg = f'{peach}', font = ('Verdana', 15),
            width = 20)


login_e = Entry(
    font = ('Verdana', 20), bg = f'{purple}',
    relief = 'flat', width = 15,
    justify='center', insertbackground='#f9da7f',
    fg = '#f9da7f'
)

password_e = Entry(
    font = ('Verdana', 20), bg = f'{purple}',
    relief = 'flat', width = 15,
    justify='center', insertbackground='#f9da7f',
    fg = '#f9da7f', show = '*'
)


login_b = Button(
    text = 'Log in', bg = f'{pink}',
    relief = 'flat', font = ('Verdana', 19),
    fg = '#c0c0c0', command = go,
    width = 15, height = 1,
    overrelief = 'solid'
)


dark_toggle_bttn = Button(
    text = 'dark theme', bg = f'{pink}',
    fg = 'white', relief = 'flat',
    overrelief = 'solid', command = dark_toggle,
    height=2, pady=4
)

dark_toggle_label = Label(
    text = 'on', bg = f'{pink}',
    fg = 'white', font = ('Verdana', 7), pady = 1)

dtbw = widget_w(dark_toggle_bttn)
dark_toggle_bttn.place(x = w - dtbw, y = 0)
dark_toggle_label.place(x = w - dtbw + dtbw/2 - widget_w(dark_toggle_label)/2,
y = 29)













w_h = widget_h(login_l)
h_y = 10

login_l.place(x = w/2 - widget_w(login_l)/2, y = h_y)
login_e.place(x = w/2 - widget_w(login_e)/2, y = h_y + 10 + w_h)

password_l.place(x = w/2 - widget_w(password_l)/2, y = h_y + 30 + 2.5*w_h )
password_e.place(x = w/2 - widget_w(password_e)/2, y = h_y + 50 + 3*w_h)

login_b.place(x = w/2 - widget_w(login_b)/2, y = h_y + 3*w_h + 70 + widget_h(login_b))

sc.mainloop()