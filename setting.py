import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import font as tkFont


class Setting():
    def __init__(self, tools):
        self.tools = tools
        # open setting window
        self.setting_page = tk.Toplevel(tools.root)
        self.setting_page.title('Setting')
        self.setting_page.geometry('500x500')
        self.setting_page.resizable(0, 0)

        # background button
        tk.Button(self.setting_page, width=360, height=500,
                  bg=tools._from_rgb((255, 235, 205)),
                  command=lambda: [self.back_to_main(),
                                   self.menu_name.pack(side='top', pady=50),
                                   self.language.pack(side='top', pady=0),
                                   self.about.pack(side='top', pady=20),
                                   self.sound_button(tools)]).place(x=0, y=0)

        # setting menu setup: menu + language + about
        self.menu_name = tk.Label(self.setting_page,
                                  textvariable=tools.setting_text,
                                  bg=tools._from_rgb((255, 235, 205)),
                                  font=tools.helv(36))
        
        self.language_name = tk.Label(self.setting_page,
                                      textvariable=tools.language_text,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      font=tools.helv(16))
        self.options = ['English', '中文']
        self.clicked = tk.StringVar(self.setting_page)
        self.clicked.set(self.options[tools.language_state])
        self.language = tk.OptionMenu(self.setting_page, self.clicked, *self.options)
        self.language.config(bg=tools._from_rgb((250, 240, 230)),
                                fg='black', font=tools.helv(24),
                                width=8, height=1)
#        menu = self.nametowidget(chooseTest.menuname)
#        menu.config(font=helv35)
        drop_down = self.language(self.options)
        drop_down.config(bg=tools._from_rgb((250, 240, 230)),
                                fg='black', font=tools.helv(24)
                         )
        
        self.about = tk.Button(self.setting_page,
                               textvariable=tools.about_text,
                               bg=tools._from_rgb((250, 240, 230)),
                               font=tools.helv(24), width=9,
                               command=lambda: [
                                   self.forget_main(tools),
                                   self.about_name.pack(side='top', pady=50),
                                   self.product_team.pack(side='top'),
                                   self.product_picture.pack(side='top',
                                                             pady=20),
                                   self.back.pack(side='top')])

        # setting menu setup: play sound
        self.sound_play = tk.PhotoImage(file='music.png').subsample(12, 12)
        self.sound_play_button = tk.Button(
            self.setting_page, image=self.sound_play, width=50, bg='white',
            command=lambda: [
                self.sound_no_play_button.pack(side='top', pady=0),
                self.sound_play_button.pack_forget(),
                tools.button_sound_update()])

        # setting menu setup: no sound
        self.sound_no_play = tk.PhotoImage(
            file='no_music.png').subsample(4, 4)
        self.sound_no_play_button = tk.Button(
            self.setting_page, image=self.sound_no_play, width=50, bg='white',
            command=lambda: [
                self.sound_no_play_button.pack_forget(),
                self.sound_play_button.pack(side='top', pady=0),
                tools.button_sound_update(),
                tools.press_button_sound()])

        # place buttons and label
        self.menu_name.pack(side='top', pady=50)
        self.language_name.pack(side='top')
        self.language.pack(side='top', pady=0)
        self.about.pack(side='top', pady=20)
        self.sound_button(tools)

        # about us
        self.about_name = tk.Label(self.setting_page,
                                   textvariable=tools.about_text,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   font=tools.helv(36))
        self.product_team = tk.Label(self.setting_page,
                                     textvariable=tools.product_text,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     justify='left',
                                     font=tools.helv(16))
        self.product_pic = tk.PhotoImage(file='WooMap.png').subsample(5,5)
        self.product_picture = tk.Label(self.setting_page,
                                        image=self.product_pic,
                                        width=160,
                                        bg=tools._from_rgb((255, 235, 205)))

        self.back = tk.Label(self.setting_page, textvariable=tools.go_back,
                             bg=tools._from_rgb((255, 235, 205)),
                             font=tools.helv(12))

        # enable main page while setting closed
        self.setting_page.protocol('WM_DELETE_WINDOW',
                                   func=lambda: self.enable_main_page(tools))

        # disable main page while setting opened
        tools.root.attributes('-disabled', True)
        
        
    def sound_button(self, tools):
        if tools.with_sound:
            self.sound_play_button.pack(side='top', pady=0)
        else:
            self.sound_no_play_button.pack(side='top', pady=0)

    def enable_main_page(self, tools):
        tools.root.attributes('-disabled', False)
        self.setting_page.destroy()

    def back_to_main(self):
        self.sound_play_button.pack_forget()
        self.sound_no_play_button.pack_forget()
        self.language_name.pack_forget()
        self.about_name.pack_forget()
        self.product_team.pack_forget()
        self.product_picture.pack_forget()
        self.back.pack_forget()

    def forget_main(self, tools):
        self.menu_name.pack_forget()
        self.language.pack_forget()
        self.about.pack_forget()
        tools.press_button_sound()
        self.sound_play_button.pack_forget()
        self.sound_no_play_button.pack_forget()

    def my_show(self, *args):
        if self.clicked.get() == 'English':
            self.tools.language_state = 0
            self.tools.press_button_sound()
            self.tools.language_update(0)
            self.tools.language_state = 0
            self.clicked.set(self.options[0])
        if self.clicked.get() == '中文':
            self.tools.language_state = 1
            self.tools.press_button_sound()
            self.tools.language_update(1)
            self.clicked.set(self.options[1])
            self.tools.language_state = 1