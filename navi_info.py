import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import font as tkFont
from din_aca_lib import *


class Navigation():
    def __init__(self, tools, main):
        self.back = tk.Button(main.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=5, height=2,
                              command=lambda: [
                                  main.default_page(tools),
                                  tools.press_button_sound(),
                                  self.departure_label.pack_forget(),
                                  self.destination_label.pack_forget(),
                                  self.op_dest.pack_forget(),
                                  self.llroute.pack_forget(),
                                  self.laroute.pack_forget(),
                                  self.lkroute.pack_forget(),
                                  self.ltroute.pack_forget(),
                                  self.alroute.pack_forget(),
                                  self.aaroute.pack_forget(),
                                  self.akroute.pack_forget(),
                                  self.atroute.pack_forget(),
                                  self.klroute.pack_forget(),
                                  self.karoute.pack_forget(),
                                  self.kkroute.pack_forget(),
                                  self.ktroute.pack_forget(),
                                  self.tlroute.pack_forget(),
                                  self.taroute.pack_forget(),
                                  self.tkroute.pack_forget(),
                                  self.ttroute.pack_forget(),
                                  self.search.pack_forget(),
                                  self.back.pack_forget(),
                                  self.guide_label.pack_forget()])
        self.guide_label = tk.Label(
            main.right_frame,
            textvariable=tools.guide_text,
            bg=tools._from_rgb((219, 112, 147)),
            fg='white', font=tools.helv(24),
            width=14, height=2)

        self.llroute = tk.Label(main.right_frame, text='Same departure and destination',
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='red', font=tools.helv(12),
                                width=30, height=10)
        self.laroute = tk.Label(main.right_frame, textvariable=tools.laroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.lkroute = tk.Label(main.right_frame, textvariable=tools.lkroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.ltroute = tk.Label(main.right_frame, textvariable=tools.ltroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.alroute = tk.Label(main.right_frame, textvariable=tools.alroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.aaroute = tk.Label(main.right_frame, textvariable=tools.aaroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='red', font=tools.helv(12),
                                width=30, height=10)
        self.akroute = tk.Label(main.right_frame, textvariable=tools.akroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.atroute = tk.Label(main.right_frame, textvariable=tools.atroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.klroute = tk.Label(main.right_frame, textvariable=tools.klroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.karoute = tk.Label(main.right_frame, textvariable=tools.karoute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.kkroute = tk.Label(main.right_frame, textvariable=tools.kkroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='red', font=tools.helv(12),
                                width=30, height=10)
        self.ktroute = tk.Label(main.right_frame, textvariable=tools.ktroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.tlroute = tk.Label(main.right_frame, textvariable=tools.tlroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.taroute = tk.Label(main.right_frame, textvariable=tools.taroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.tkroute = tk.Label(main.right_frame, textvariable=tools.tkroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='black', font=tools.helv(12),
                                width=30, height=10)
        self.ttroute = tk.Label(main.right_frame, textvariable=tools.ttroute_text,
                                justify='left', wraplength=300,
                                bg=tools._from_rgb((255, 235, 205)),
                                fg='red', font=tools.helv(12),
                                width=30, height=10)
        
        # departure + destination
        option_depa = ['Lowry', 'Andrews', 'Kauke', 'Taylor']
        option_dest = ['Lowry', 'Andrews', 'Kauke', 'Taylor']
        self.clicked = tk.StringVar(main.left_display_frame)
        self.clicked.set(option_depa[0])
        self.clicked1 = tk.StringVar(main.left_display_frame)
        self.clicked1.set(option_dest[0])
        self.op_depa = tk.OptionMenu(main.left_display_frame,self.clicked, *option_depa)
        self.op_depa.config(bg=tools._from_rgb((250, 240, 230)),
                                fg='black', font=tools.helv(10),
                                width=40, height=2)
        self.op_dest = tk.OptionMenu(main.left_display_frame,self.clicked1, *option_depa)
        self.op_dest.config(bg=tools._from_rgb((250, 240, 230)),
                                fg='black', font=tools.helv(10),
                                width=40, height=2)
        self.departure_label = tk.Label(main.left_display_frame,
                                        textvariable=tools.departure,
                                        bg=tools._from_rgb((219, 112, 147)),
                                        fg='white', font=tools.helv(12),
                                        width=10, height=2)
        self.destination_label = tk.Label(main.left_display_frame,
                                          textvariable=tools.destination,
                                          bg=tools._from_rgb((219, 112, 147)),
                                          fg='white', font=tools.helv(12),
                                          width=10, height=2)
        self.search = tk.Button(main.left_display_frame,
                                textvariable=tools.search,
                                font=tools.helv(12), fg='white',
                                bg=tools._from_rgb((219, 112, 147)),
                                width=8, height=2,
                                command=lambda: [self.clear_route(),
                                                 self.route(),
                                                 tools.press_button_sound()])
        # pack
        self.guide_label.pack(side='top', fill='x')
        self.back.pack(side='top', padx=20, pady=30)
        main.guide_button.pack(side='top', padx=0, pady=0)
        self.departure_label.pack(side='top', padx=10, pady=30)
        self.op_depa.pack(side='top', padx=20, pady=10)
        self.destination_label.pack(side='top', padx=10, pady=30)
        self.op_dest.pack(side='top', padx=20, pady=10)
        self.search.pack(side='top', padx=20, pady=20)

    def route(self):
        if self.clicked.get() == 'Lowry':
            if self.clicked1.get() == 'Lowry':
                self.llroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Andrews':
                self.laroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Kauke':
                self.lkroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Taylor':
                self.ltroute.pack(side='top', padx=0, pady=35)
        elif self.clicked.get() == 'Andrews':
            if  self.clicked1.get() == 'Lowry':
                self.alroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Andrews':
                self.aaroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Kauke':
                self.akroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Taylor':
                self.atroute.pack(side='top', padx=0, pady=35)
        elif self.clicked.get() == 'Kauke':
            if self.clicked.get() == 'Lowry':
                self.klroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Andrews':
                self.karoute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Kauke':
                self.kkroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Taylor':
                self.ktroute.pack(side='top', padx=0, pady=35)
        elif self.clicked.get() == 'Taylor':
            if self.clicked.get() == 'Lowry':
                self.tlroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Andrews':
                self.taroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Kauke':
                self.tkroute.pack(side='top', padx=0, pady=35)
            elif self.clicked1.get() == 'Taylor':
                self.ttroute.pack(side='top', padx=0, pady=35)

    def clear_route(self):
        self.llroute.pack_forget()
        self.laroute.pack_forget()
        self.lkroute.pack_forget()
        self.ltroute.pack_forget()
        self.alroute.pack_forget()
        self.aaroute.pack_forget()
        self.akroute.pack_forget()
        self.atroute.pack_forget()
        self.klroute.pack_forget()
        self.karoute.pack_forget()
        self.kkroute.pack_forget()
        self.ktroute.pack_forget()
        self.tlroute.pack_forget()
        self.taroute.pack_forget()
        self.tkroute.pack_forget()
        self.ttroute.pack_forget()


class Information():
        # navigation route
    def __init__(self, tools, main):
        self.back = tk.Button(main.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=5, height=2,
                              command=lambda:  [main.default_page(tools),
                                                tools.press_button_sound(),
                                                self.info_forget(),
                                                self.lowry.pack_forget(),
                                                self.andrews.pack_forget(),
                                                self.gault.pack_forget(),
                                                self.timken.pack_forget(),
                                                self.ebert.pack_forget(),
                                                self.kauke.pack_forget(),
                                                self.morgan.pack_forget(),
                                                self.scheide.pack_forget(),
                                                self.scovel.pack_forget(),
                                                self.severance.pack_forget(),
                                                self.taylor.pack_forget(),
                                                self.williams.pack_forget(),
                                                self.wishart.pack_forget(),
                                                self.back.pack_forget(),
                                                self.change_color(tools, 100),
                                                self.info_label.pack_forget()])
        self.lowry = tk.Button(
            main.left_display_frame,
            text='Lowry',
            font=tools.helv(12),
            bg=tools._from_rgb((250, 240, 230)),
            width=8, height=1,
            command=lambda: [
                self.change_color(tools, 1),
                self.info_forget(),
                self.lowry_info.pack(
                    side='top', padx=20, pady=20),
                self.lowry_picture.pack(
                    side='top', padx=20, pady=20),
                self.map_buttons(1),
                tools.press_button_sound()])
        self.andrews = tk.Button(main.left_display_frame, text='Andrews',
                                 font=tools.helv(12),
                                 bg=tools._from_rgb((250, 240, 230)),
                                 width=8, height=1,
                                 command=lambda: [
                                     self.change_color(tools, 2),
                                     self.info_forget(),
                                     self.andrews_info.pack(
                                         side='top', padx=20, pady=20),
                                     self.andrews_picture.pack(
                                         side='top', padx=20, pady=20),
                                     self.map_buttons(2),
                                     tools.press_button_sound()])
        self.gault = tk.Button(main.left_display_frame, text='Gault',
                               font=tools.helv(12),
                               bg=tools._from_rgb((250, 240, 230)),
                               width=8, height=1,
                               command=lambda: [
                                   self.change_color(tools, 3),
                                   self.info_forget(),
                                   self.gault_info.pack(
                                       side='top', padx=20, pady=20),
                                   self.gault_picture.pack(
                                       side='top', padx=20, pady=20),
                                   self.map_buttons(3),
                                   tools.press_button_sound()])
        self.timken = tk.Button(main.left_display_frame, text='Timken',
                                font=tools.helv(12),
                                bg=tools._from_rgb((250, 240, 230)),
                                width=8, height=1,
                                command=lambda: [
                                    self.change_color(tools, 4),
                                    self.info_forget(),
                                    self.timken_info.pack(
                                        side='top', padx=20, pady=20),
                                    self.timken_picture.pack(
                                        side='top', padx=20, pady=20),
                                    self.map_buttons(4),
                                    tools.press_button_sound()])
        self.ebert = tk.Button(main.left_display_frame, text='Ebert',
                               font=tools.helv(12),
                               bg=tools._from_rgb((250, 240, 230)),
                               width=8, height=1,
                               command=lambda: [
                                   self.change_color(tools, 5),
                                   self.info_forget(),
                                   self.ebert_info.pack(
                                       side='top', padx=20, pady=20),
                                   self.ebert_picture.pack(
                                       side='top', padx=20, pady=20),
                                   self.map_buttons(5),
                                   tools.press_button_sound()])
        self.kauke = tk.Button(main.left_display_frame, text='Kauke',
                               font=tools.helv(12),
                               bg=tools._from_rgb((250, 240, 230)),
                               width=8, height=1,
                               command=lambda: [
                                   self.change_color(tools, 6),
                                   self.info_forget(),
                                   self.kauke_info.pack(
                                       side='top', padx=20, pady=20),
                                   self.kauke_picture.pack(
                                       side='top', padx=20, pady=20),
                                   self.map_buttons(6),
                                   tools.press_button_sound()])
        self.morgan = tk.Button(main.left_display_frame, text='Morgan',
                                font=tools.helv(12),
                                bg=tools._from_rgb((250, 240, 230)),
                                width=8, height=1,
                                command=lambda: [
                                    self.change_color(tools, 7),
                                    self.info_forget(),
                                    self.morgan_info.pack(
                                        side='top', padx=20, pady=20),
                                    self.morgan_picture.pack(
                                        side='top', padx=20, pady=20),
                                    self.map_buttons(7),
                                    tools.press_button_sound()])
        self.scheide = tk.Button(main.left_display_frame, text='Schide',
                                 font=tools.helv(12),
                                 bg=tools._from_rgb((250, 240, 230)),
                                 width=8, height=1,
                                 command=lambda: [
                                     self.change_color(tools, 8),
                                     self.info_forget(),
                                     self.scheide_info.pack(
                                         side='top', padx=20, pady=20),
                                     self.scheide_picture.pack(
                                         side='top', padx=20, pady=20),
                                     self.map_buttons(8),
                                     tools.press_button_sound()])
        self.scovel = tk.Button(main.left_display_frame, text='Scovel',
                                font=tools.helv(12),
                                bg=tools._from_rgb((250, 240, 230)),
                                width=8, height=1,
                                command=lambda: [
                                    self.change_color(tools, 9),
                                    self.info_forget(),
                                    self.scovel_info.pack(
                                        side='top', padx=20, pady=20),
                                    self.scovel_picture.pack(
                                        side='top', padx=20, pady=20),
                                    self.map_buttons(9),
                                    tools.press_button_sound()])
        self.severance = tk.Button(main.left_display_frame, text='Severance',
                                   font=tools.helv(12),
                                   bg=tools._from_rgb((250, 240, 230)),
                                   width=8, height=1,
                                   command=lambda: [
                                       self.change_color(tools, 10),
                                       self.info_forget(),
                                       self.severance_info.pack(
                                           side='top', padx=20, pady=20),
                                       self.severance_picture.pack(
                                           side='top', padx=20, pady=20),
                                       self.map_buttons(10),
                                       tools.press_button_sound()])
        self.taylor = tk.Button(main.left_display_frame, text='Taylor',
                                font=tools.helv(12),
                                bg=tools._from_rgb((250, 240, 230)),
                                width=8, height=1,
                                command=lambda: [
                                    self.change_color(tools, 11),
                                    self.info_forget(),
                                    self.taylor_info.pack(
                                        side='top', padx=20, pady=20),
                                    self.taylor_picture.pack(
                                        side='top', padx=20, pady=20),
                                    self.map_buttons(11),
                                    tools.press_button_sound()])
        self.williams = tk.Button(main.left_display_frame, text='Williams',
                                  font=tools.helv(12),
                                  bg=tools._from_rgb((250, 240, 230)),
                                  width=8, height=1,
                                  command=lambda: [
                                      self.change_color(tools, 12),
                                      self.info_forget(),
                                      self.williams_info.pack(
                                          side='top', padx=20, pady=20),
                                      self.williams_picture.pack(
                                          side='top', padx=20, pady=20),
                                      self.map_buttons(12),
                                      tools.press_button_sound()])
        self.wishart = tk.Button(main.left_display_frame, text='Wishart',
                                 font=tools.helv(12),
                                 bg=tools._from_rgb((250, 240, 230)),
                                 width=8, height=1,
                                 command=lambda: [
                                     self.change_color(tools, 13),
                                     self.info_forget(),
                                     self.wishart_info.pack(
                                         side='top', padx=20, pady=20),
                                     self.wishart_picture.pack(
                                         side='top', padx=20, pady=20),
                                     self.map_buttons(13),
                                     tools.press_button_sound()])
        self.lowry_info = tk.Label(main.right_frame,
                                   justify='left', wraplength=300,
                                   textvariable=tools.lowry_info,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   fg='black', font=tools.helv(12),
                                   width=30, height=2)
        self.lowry_info = tk.Label(main.right_frame,
                                   justify='left', wraplength=300,
                                   textvariable=tools.lowry_info,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   fg='black', font=tools.helv(12), anchor='e',
                                   width=30, height=10)
        self.andrews_info = tk.Label(main.right_frame,
                                     justify='left', wraplength=300,
                                     textvariable=tools.andrews_info,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     fg='black', font=tools.helv(12),
                                     width=30, height=10)
        self.gault_info = tk.Label(main.right_frame,
                                   justify='left', wraplength=300,
                                   textvariable=tools.gault_info,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   fg='black', font=tools.helv(12),
                                   width=30, height=10)
        self.timken_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.timken_info,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.ebert_info = tk.Label(main.right_frame,
                                   justify='left', wraplength=300,
                                   textvariable=tools.ebert_info,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   fg='black', font=tools.helv(12),
                                   width=30, height=10)
        self.kauke_info = tk.Label(main.right_frame,
                                   justify='left', wraplength=300,
                                   textvariable=tools.kauke_info,
                                   bg=tools._from_rgb((255, 235, 205)),
                                   fg='black', font=tools.helv(12),
                                   width=30, height=10)
        self.morgan_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.morgan_info,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.scheide_info = tk.Label(main.right_frame,
                                     justify='left', wraplength=300,
                                     textvariable=tools.scheide_info,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     fg='black', font=tools.helv(12),
                                     width=30, height=10)
        self.scovel_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.scovel_info,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.severance_info = tk.Label(main.right_frame,
                                       justify='left', wraplength=300,
                                       textvariable=tools.severance_info,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       fg='black', font=tools.helv(12),
                                       width=30, height=10)
        self.taylor_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.taylor_info,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.williams_info = tk.Label(main.right_frame,
                                      justify='left', wraplength=300,
                                      textvariable=tools.williams_info,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      fg='black', font=tools.helv(12),
                                      width=30, height=10)
        self.wishart_info = tk.Label(main.right_frame,
                                     justify='left', wraplength=300,
                                     textvariable=tools.wishart_info,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     fg='black', font=tools.helv(12),
                                     width=30, height=10)

        self.lowry_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.andrews_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.gault_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.timken_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.ebert_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.kauke_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.morgan_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.scheide_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.scovel_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.severance_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.taylor_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.williams_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        self.wishart_button = tk.Label(
            main.center_frame,
            image=tools.star, bg='white')
        
        self.lowry_picture = tk.Label(main.right_frame, image= tools.lowrydining_pic, width=240, height=320)
        self.andrews_picture = tk.Label(main.right_frame, image= tools.andrews_pic, width=240, height=320)
        self.gault_picture = tk.Label(main.right_frame, image= tools.gault_pic, width=240, height=320)
        self.timken_picture = tk.Label(main.right_frame, image= tools.timken_pic, width=240, height=320)
        self.ebert_picture = tk.Label(main.right_frame, image= tools.ebert_pic, width=240, height=320)
        self.kauke_picture = tk.Label(main.right_frame, image= tools.kauke_pic, width=240, height=320)
        self.morgan_picture = tk.Label(main.right_frame, image= tools.morgan_pic, width=240, height=320)
        self.scheide_picture = tk.Label(main.right_frame, image= tools.scheide_pic, width=240, height=320)
        self.scovel_picture = tk.Label(main.right_frame, image= tools.scovel_pic, width=240, height=320)
        self.severance_picture = tk.Label(main.right_frame, image= tools.severance_pic, width=240, height=320)
        self.taylor_picture = tk.Label(main.right_frame, image= tools.taylor_pic, width=240, height=320)
        self.williams_picture = tk.Label(main.right_frame, image= tools.williams_pic, width=240, height=320)
        self.wishart_picture = tk.Label(main.right_frame, image= tools.wishart_pic, width=240, height=320)
        
        self.squirrel = tk.Label(main.right_frame, image=tools.squirrel_pic,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 width=200, height=150)
        self.info_label = tk.Label(
            main.right_frame,
            textvariable=tools.info_text,
            bg=tools._from_rgb((100, 149, 237)),
            fg='white', font=tools.helv(24),
            width=14, height=2)
        self.info_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.info_text,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.info_label.pack(side='top', fill='x')
        self.info_info.pack(side='top')
        self.squirrel.pack(side='top')
        self.back.pack(side='top', padx=20, pady=30)
        main.info_button.pack(side='top', padx=0, pady=0)
        self.lowry.pack(side='top', padx=20, pady=20)
        self.andrews.pack(side='top', padx=20, pady=0)
        self.gault.pack(side='top', padx=20, pady=20)
        self.timken.pack(side='top', padx=20, pady=0)
        self.ebert.pack(side='top', padx=20, pady=20)
        self.kauke.pack(side='top', padx=20, pady=0)
        self.morgan.pack(side='top', padx=20, pady=20)
        self.scheide.pack(side='top', padx=20, pady=0)
        self.scovel.pack(side='top', padx=20, pady=20)
        self.severance.pack(side='top', padx=20, pady=0)
        self.taylor.pack(side='top', padx=20, pady=20)
        self.williams.pack(side='top', padx=20, pady=0)
        self.wishart.pack(side='top', padx=20, pady=20)

    def map_buttons(self, x):
        if x == 1:
            self.lowry_button.pack(side='right', anchor='se', padx=200, pady=350)
        elif x == 2:
            self.andrews_button.pack(side='right', anchor='se', padx=360, pady=250)
        elif x == 3:
            self.gault_button.pack(side='right', anchor='se', padx=360, pady=320)
        elif x == 4:
            self.timken_button.pack(side='left', anchor='se', padx=350, pady=230)
        elif x == 5:
            self.ebert_button.pack(side='left', anchor='ne', padx=250, pady=310)
        elif x == 6:
            self.kauke_button.pack(side='left', anchor='se', padx=250, pady=310)
        elif x == 7:
            self.morgan_button.pack(side='left', anchor='se', padx=190, pady=45)
        elif x == 8:
            self.scheide_button.pack(side='right', anchor='se', padx=220, pady=110)
        elif x == 9:
            self.scovel_button.pack(side='left', anchor='se', padx=190, pady=115)
        elif x == 10:
            self.severance_button.pack(side='left', anchor='se', padx=310, pady=118)
        elif x == 11:
            self.taylor_button.pack(side='left', anchor='se', padx=95, pady=235)
        elif x == 12:
            self.williams_button.pack(side='left', anchor='se', padx=310, pady=45)
        elif x == 13:
            self.wishart_button.pack(side='left', anchor='se', padx=80, pady=120)

    def change_color(self, tools, x):
        self.lowry['bg'] = tools._from_rgb((250, 240, 230))
        if x == 1:
            self.lowry['bg'] = tools._from_rgb((175, 238, 238))
        Library.change_color(self, tools, x)
        Academic.change_color(self, tools, x)

    def info_forget(self):
        self.lowry_picture.pack_forget()
        self.andrews_picture.pack_forget()
        self.gault_picture.pack_forget()
        self.timken_picture.pack_forget()
        self.ebert_picture.pack_forget()
        self.kauke_picture.pack_forget()
        self.morgan_picture.pack_forget()
        self.scheide_picture.pack_forget()
        self.scovel_picture.pack_forget()
        self.severance_picture.pack_forget()
        self.taylor_picture.pack_forget()
        self.williams_picture.pack_forget()
        self.wishart_picture.pack_forget()

        self.squirrel.pack_forget()
        self.info_info.pack_forget()

        self.lowry_info.pack_forget()
        self.andrews_info.pack_forget()
        self.gault_info.pack_forget()
        self.timken_info.pack_forget()
        self.ebert_info.pack_forget()
        self.kauke_info.pack_forget()
        self.morgan_info.pack_forget()
        self.scheide_info.pack_forget()
        self.scovel_info.pack_forget()
        self.severance_info.pack_forget()
        self.taylor_info.pack_forget()
        self.williams_info.pack_forget()
        self.wishart_info.pack_forget()

        self.lowry_button.pack_forget()
        self.andrews_button.pack_forget()
        self.gault_button.pack_forget()
        self.timken_button.pack_forget()
        self.ebert_button.pack_forget()
        self.kauke_button.pack_forget()
        self.morgan_button.pack_forget()
        self.scheide_button.pack_forget()
        self.scovel_button.pack_forget()
        self.severance_button.pack_forget()
        self.taylor_button.pack_forget()
        self.williams_button.pack_forget()
        self.wishart_button.pack_forget()
