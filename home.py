import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import font as tkFont
from tools import Tools
from setting import Setting
from din_aca_lib import Dining, Library, Academic
from navi_info import Navigation, Information


class Home_page():
    def __init__(self, tools):
        self.departure_num = 0
        self.destination_num = 0
        self.building_num = 0
        tools.language_update(0)    # 0 = English, 1 = Chinese

        # create frames
        self.wooster = tk.PhotoImage(file='center.png')
        self.empty_frame_left = tk.Frame(
            tools.root, bg=tools._from_rgb((255, 235, 205)))
        self.left_frame = tk.Frame(
            tools.root, bg=tools._from_rgb((255, 235, 205)))
        self.left_display_frame = tk.Frame(
            tools.root, bg=tools._from_rgb((255, 235, 205)))
        self.center_frame = tk.Frame(tools.root)
        self.right_frame = tk.Frame(tools.root,
                                    bg=tools._from_rgb((255, 235, 205)))

        # place frames
        self.empty_frame_left.place(x=0, y=0, width=30, height=850)
        self.left_frame.place(x=30, y=0, width=120, height=850)
        self.left_display_frame.place(x=150, y=0, width=150, height=850)
        self.center_frame.place(x=300, y=0, width=860, height=850)
        self.right_frame.place(x=1100, y=0, width=350, height=850)

        # wooster map
        tk.Label(self.center_frame, image=self.wooster).place(x=0, y=0)

        self.back = tk.Button(self.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((255, 235, 205)),
                              width=5, height=2,
                              command=lambda: [self.default_page(tools),
                                               tools.press_button_sound()])
        self.home = tk.Label(self.left_frame, textvariable=tools.home_text,
                             font=tools.helv(16),
                             bg=tools._from_rgb((255, 235, 205)),
                             fg=tools._from_rgb((96, 96, 96)),
                             width=6, height=1)
        self.empty = tk.Label(self.left_display_frame, text='   ',
                              font=tools.helv(16),
                              bg=tools._from_rgb((255, 235, 205)),
                              width=6, height=1)

        # introduction of wooster
        self.wooster_name = tk.Label(self.right_frame,
                                     textvariable=tools.wooster_name,
                                     bg=tools._from_rgb((0, 0, 0)),
                                     fg=tools._from_rgb((255, 215, 0)),
                                     font=tools.helv(24), height=2)
        self.wooster_intro_text = tk.Label(self.right_frame, wraplength=300,
                                           justify='left',
                                           textvariable=tools.wooster_intro,
                                           font=tools.ariel(12),
                                           bg=tools._from_rgb((255, 235, 205)),
                                           height=4, width=50)
        self.squirrel_pic = tk.PhotoImage(file='Squirrel.png')
        self.squirrel = tk.Label(self.right_frame, image=self.squirrel_pic,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 width=200, height=150)

        # dining
        self.dining = tk.PhotoImage(file='dining.png').subsample(3, 3)
        self.dining_button = tk.Button(self.left_frame, image=self.dining,
                                       width=80, height=70,
                                       command=lambda: [
                                           self.default_page(tools),
                                           self.button_label_forget(),
                                           self.main_page_buttons_forget(),
                                           self.empty.pack(
                                               side='top', padx=3, pady=35),
                                           Dining(tools, self),
                                           self.change_status(1),
                                           tools.press_button_sound()])
        self.dining_left_label = tk.Label(self.left_display_frame,
                                          textvariable=tools.dining_text,
                                          bg=tools._from_rgb((255, 235, 205)),
                                          font=tools.helv(15), height=2)

        # lib
        self.lib = tk.PhotoImage(file='lib.png').subsample(11, 13)
        self.lib_button = tk.Button(self.left_frame, image=self.lib,
                                    width=80, height=70,
                                    command=lambda: [
                                        self.default_page(tools),
                                        self.button_label_forget(),
                                        self.main_page_buttons_forget(),
                                        self.empty.pack(
                                            side='top', padx=3, pady=35),
                                        Library(tools, self),
                                        self.change_status(2),
                                        tools.press_button_sound()])
        self.lib_left_label = tk.Label(self.left_display_frame,
                                       textvariable=tools.lib_text,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       font=tools.helv(15), height=2)

        # academic
        self.aca = tk.PhotoImage(file='classroom.png').subsample(2, 2)
        self.aca_button = tk.Button(self.left_frame, image=self.aca,
                                    width=80, height=70,
                                    command=lambda: [
                                        self.default_page(tools),
                                        self.button_label_forget(),
                                        self.main_page_buttons_forget(),
                                        self.empty.pack(
                                            side='top', padx=3, pady=35),
                                        Academic(tools, self),
                                        self.change_status(3),
                                        tools.press_button_sound()])
        self.aca_left_label = tk.Label(self.left_display_frame,
                                       textvariable=tools.aca_text,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       font=tools.helv(15), height=2)

        # guide
        self.guide = tk.PhotoImage(file='guide.png').subsample(11, 11)
        self.guide_button = tk.Button(self.left_frame, image=self.guide,
                                      width=80, height=70,
                                      command=lambda: [
                                          self.default_page(tools),
                                          self.button_label_forget(),
                                          self.main_page_buttons_forget(),
                                          self.empty.pack(
                                               side='top', padx=3, pady=35),
                                          Navigation(tools, self),
                                          self.change_status(4),
                                          tools.press_button_sound()])

        self.guide_left_label = tk.Label(self.left_display_frame,
                                         textvariable=tools.guide_text,
                                         bg=tools._from_rgb((255, 235, 205)),
                                         font=tools.helv(15), height=2)

        # building information
        self.info = tk.PhotoImage(file='info.png').subsample(7, 7)
        self.info_button = tk.Button(self.left_frame, image=self.info,
                                     width=80, height=70,
                                     command=lambda: [
                                         self.default_page(tools),
                                         self.button_label_forget(),
                                         self.main_page_buttons_forget(),
                                         Information(tools, self),
                                         self.change_status(5),
                                         tools.press_button_sound()])
        self.info_left_label = tk.Label(self.left_display_frame,
                                        textvariable=tools.info_text,
                                        bg=tools._from_rgb((255, 235, 205)),
                                        font=tools.helv(15), height=2)

        # setting
        self.setting = tk.PhotoImage(file='settings.png').subsample(8, 8)
        self.setting_button = tk.Button(self.left_frame, image=self.setting,
                                        width=50,
                                        command=lambda: [
                                            tools.press_button_sound(),
                                            Setting(tools)])

        # place all the buttons with its label
        self.main_page_buttons()
        self.default_page(tools)
        self.setting_button.pack(side='bottom', anchor='w', padx=25, pady=35)

        # ask for quit
        tools.root.protocol('WM_DELETE_WINDOW', tools.on_closing)
        tools.root.mainloop()

    # main page
    def main_page_buttons(self):
        self.home.pack(side='top', padx=0, pady=30)
        self.dining_button.pack(side='top', padx=0, pady=30)
        self.lib_button.pack(side='top', padx=0, pady=0)
        self.aca_button.pack(side='top', padx=0, pady=30)
        self.guide_button.pack(side='top', padx=0, pady=0)
        self.info_button.pack(side='top', padx=0, pady=30)

    def main_page_buttons_forget(self):
        self.home.pack_forget()
        self.back.pack_forget()
        self.empty.pack_forget()
        self.dining_button.pack_forget()
        self.lib_button.pack_forget()
        self.aca_button.pack_forget()
        self.guide_button.pack_forget()
        self.info_button.pack_forget()

    def default_page(self, tools):
        self.change_status(100)
        self.main_page_buttons_forget()    # main page
        self.main_page_buttons()
        self.empty.pack(side='top', padx=3, pady=30)
        self.dining_left_label.pack(side='top', padx=3, pady=30)
        self.lib_left_label.pack(side='top', padx=3, pady=20)
        self.aca_left_label.pack(side='top', padx=3, pady=20)
        self.guide_left_label.pack(side='top', padx=3, pady=20)
        self.info_left_label.pack(side='top', padx=3, pady=20)
        self.wooster_name.pack(side='top', fill='x')
        self.squirrel.pack(side='bottom')
        self.wooster_intro_text.pack(side='left', fill='y', padx=15, pady=15)

    def button_label_forget(self):
        self.dining_left_label.pack_forget()
        self.lib_left_label.pack_forget()
        self.aca_left_label.pack_forget()
        self.guide_left_label.pack_forget()
        self.info_left_label.pack_forget()
        self.wooster_name.pack_forget()
        self.squirrel.pack_forget()
        self.wooster_intro_text.pack_forget()

    def change_status(self, x):
        self.dining_button['state'] = 'normal'
        self.lib_button['state'] = 'normal'
        self.aca_button['state'] = 'normal'
        self.guide_button['state'] = 'normal'
        self.info_button['state'] = 'normal'
        if x == 1:
            self.dining_button.pack(side='top', padx=0, pady=0)
            self.dining_button['state'] = 'disable'
        elif x == 2:
            self.lib_button.pack(side='top', padx=0, pady=0)
            self.lib_button['state'] = 'disable'
        elif x == 3:
            self.aca_button.pack(side='top', padx=0, pady=0)
            self.aca_button['state'] = 'disable'
        elif x == 4:
            self.guide_button.pack(side='top', padx=0, pady=0)
            self.guide_button['state'] = 'disable'
        elif x == 5:
            self.info_button.pack(side='top', padx=0, pady=0)
            self.info_button['state'] = 'disable'
