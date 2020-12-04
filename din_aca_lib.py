import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import font as tkFont


class Dining():
    def __init__(self, tools, main):
        self.back = tk.Button(main.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=5, height=2,
                              command=lambda: [main.default_page(tools),
                                               tools.press_button_sound(),
                                               self.quit(tools)])

        # dining function
        self.dining_label = tk.Label(main.right_frame,
                                     textvariable=tools.dining_text,
                                     bg=tools._from_rgb((210, 180, 140)),
                                     fg='white', font=tools.helv(24),
                                     width=14, height=2)
        self.dining_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.dining_info_text,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        
        # picture
        self.squirrel = tk.Label(main.right_frame, image=tools.squirrel_pic,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 width=200, height=150)
        self.kittredge_picture = tk.Label(main.right_frame,
                                          image=tools.kittredge_pic,
                                          bg=tools._from_rgb((255, 235, 205)),
                                          width=240, height=320)
        self.knowlton_picture = tk.Label(main.right_frame,
                                         image=tools.knowlton_pic,
                                         bg=tools._from_rgb((255, 235, 205)),
                                         width=240, height=320)
        self.lowrydining_picture = tk.Label(main.right_frame,
                                            image=tools.lowrydining_pic,
                                            bg=tools._from_rgb((255, 235,
                                                                205)),
                                            width=240, height=320)
        self.macleod_picture = tk.Label(main.right_frame,
                                        image=tools.macleod_pic,
                                        bg=tools._from_rgb((255, 235, 205)),
                                        width=240, height=320)
        self.moms_picture = tk.Label(main.right_frame, image=tools.moms_pic,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     width=240, height=320)
        self.oldman_picture = tk.Label(main.right_frame,
                                       image=tools.oldman_pic,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       width=240, height=320)
        self.pops_picture = tk.Label(main.right_frame, image=tools.pops_pic,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     width=240, height=320)

        # dining places
        self.kittredge = tk.Button(main.left_display_frame,
                                   text='Kittredge\nDining Hall',
                                   font=tools.helv(12),
                                   bg=tools._from_rgb((250, 240, 230)),
                                   width=8, height=2,
                                   command=lambda: [
                                       self.change_color(tools, 14),
                                       self.info_forget(),
                                       self.kittredge_info.pack(
                                           side='top', padx=20, pady=20),
                                       self.kittredge_picture.pack(
                                           side='top', padx=20, pady=20),
                                       self.map_buttons(14),
                                       tools.press_button_sound()])
        self.knowlton = tk.Button(main.left_display_frame,
                                  text='Knowlton\nCafé', font=tools.helv(12),
                                  bg=tools._from_rgb((250, 240, 230)),
                                  width=8, height=2,
                                  command=lambda: [
                                      self.change_color(tools, 15),
                                      self.info_forget(),
                                      self.knowlton_info.pack(
                                          side='top', padx=20, pady=20),
                                      self.knowlton_picture.pack(
                                          side='top', padx=20, pady=20),
                                      self.map_buttons(15),
                                      tools.press_button_sound()])
        self.lowrydining = tk.Button(main.left_display_frame,
                                     text='Lowry\nDining Hall',
                                     font=tools.helv(12),
                                     bg=tools._from_rgb((250, 240, 230)),
                                     width=8, height=2,
                                     command=lambda: [
                                         self.change_color(tools, 16),
                                         self.info_forget(),
                                         self.lowrydining_info.pack(
                                             side='top', padx=20, pady=20),
                                         self.lowrydining_picture.pack(
                                             side='top', padx=20, pady=20),
                                         self.map_buttons(16),
                                         tools.press_button_sound()])
        self.macleod = tk.Button(main.left_display_frame,
                                 text="MacLeod's\n C Store",
                                 font=tools.helv(12),
                                 bg=tools._from_rgb((250, 240, 230)),
                                 width=8, height=2,
                                 command=lambda: [
                                     self.change_color(tools, 17),
                                     self.info_forget(),
                                     self.macleod_info.pack(
                                         side='top', padx=20, pady=20),
                                     self.macleod_picture.pack(
                                         side='top', padx=20, pady=20),
                                     self.map_buttons(17),
                                     tools.press_button_sound()])
        self.moms = tk.Button(main.left_display_frame,
                              text="Mom's \nTruckstop",
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=8, height=2,
                              command=lambda: [
                                  self.change_color(tools, 18),
                                  self.info_forget(),
                                  self.moms_info.pack(
                                      side='top', padx=20, pady=20),
                                  self.moms_picture.pack(
                                      side='top', padx=20, pady=20),
                                  self.map_buttons(18),
                                  tools.press_button_sound()])
        self.oldman = tk.Button(main.left_display_frame,
                                text='Old Main\nCafé',
                                font=tools.helv(12),
                                bg=tools._from_rgb((250, 240, 230)),
                                width=8, height=2,
                                command=lambda: [
                                    self.change_color(tools, 19),
                                    self.info_forget(),
                                    self.oldman_info.pack(
                                        side='top', padx=20, pady=20),
                                    self.oldman_picture.pack(
                                        side='top', padx=20, pady=20),
                                    self.map_buttons(19),
                                    tools.press_button_sound()])
        self.pops = tk.Button(main.left_display_frame,
                              text="Pop's\n Shop",
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=8, height=2,
                              command=lambda: [
                                  self.change_color(tools, 20),
                                  self.info_forget(),
                                  self.pops_info.pack(
                                      side='top', padx=20, pady=20),
                                  self.pops_picture.pack(
                                      side='top', padx=20, pady=20),
                                  self.map_buttons(20),
                                  tools.press_button_sound()])

        # dining building info
        self.kittredge_info = tk.Label(main.right_frame,
                                       justify='left', wraplength=300,
                                       textvariable=tools.kittredge_info,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       fg='black', font=tools.helv(12),
                                       width=30, height=10)
        self.knowlton_info = tk.Label(main.right_frame,
                                      justify='left', wraplength=300,
                                      textvariable=tools.knowlton_info,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      fg='black', font=tools.helv(12),
                                      width=30, height=10)
        self.lowrydining_info = tk.Label(main.right_frame,
                                         justify='left', wraplength=300,
                                         textvariable=tools.lowrydining_info,
                                         bg=tools._from_rgb((255, 235, 205)),
                                         fg='black', font=tools.helv(12),
                                         width=30, height=10)
        self.macleod_info = tk.Label(main.right_frame,
                                     justify='left', wraplength=300,
                                     textvariable=tools.macleod_info,
                                     bg=tools._from_rgb((255, 235, 205)),
                                     fg='black', font=tools.helv(12),
                                     width=30, height=10)
        self.moms_info = tk.Label(main.right_frame,
                                  justify='left', wraplength=300,
                                  textvariable=tools.moms_info,
                                  bg=tools._from_rgb((255, 235, 205)),
                                  fg='black', font=tools.helv(12),
                                  width=30, height=10)
        self.oldman_info = tk.Label(main.right_frame,
                                    justify='left', wraplength=300,
                                    textvariable=tools.oldman_info,
                                    bg=tools._from_rgb((255, 235, 205)),
                                    fg='black', font=tools.helv(12),
                                    width=30, height=10)
        self.pops_info = tk.Label(main.right_frame,
                                  justify='left', wraplength=300,
                                  textvariable=tools.pops_info,
                                  bg=tools._from_rgb((255, 235, 205)),
                                  fg='black', font=tools.helv(12),
                                  width=30, height=10)
        # labels on map
        self.kittredge_button = tk.Label(main.center_frame, image=tools.star,
                                         bg='white')
        self.knowlton_button = tk.Label(main.center_frame, image=tools.star,
                                        bg='white')
        self.lowrydining_button = tk.Label(main.center_frame,
                                           image=tools.star, bg='white')
        self.macleod_button = tk.Label(main.center_frame, image=tools.star,
                                       bg='white')
        self.moms_button = tk.Label(main.center_frame, image=tools.star,
                                    bg='white')
        self.oldman_button = tk.Label(main.center_frame, image=tools.star,
                                      bg='white')
        self.pops_button = tk.Label(main.center_frame, image=tools.star,
                                    bg='white')

        # shown in main
        self.dining_label.pack(side='top', fill='x')
        self.dining_info.pack(side='top', padx=20, pady=20)
        self.back.pack(side='top', padx=20, pady=30)
        self.squirrel.pack_forget()
        self.squirrel.pack(side='top', padx=20, pady=20)
        self.kittredge.pack(side='top', padx=20, pady=20)
        self.knowlton.pack(side='top', padx=20, pady=0)
        self.lowrydining.pack(side='top', padx=20, pady=20)
        self.macleod.pack(side='top', padx=20, pady=0)
        self.moms.pack(side='top', padx=20, pady=20)
        self.oldman.pack(side='top', padx=20, pady=0)
        self.pops.pack(side='top', padx=20, pady=20)

    # red star on the map
    def map_buttons(self, x):
        if x == 14:
            self.kittredge_button.pack(side='right', anchor='ne',
                                       padx=170, pady=70)
        elif x == 15:
            self.knowlton_button.pack(side='left', anchor='se',
                                      padx=310, pady=80)
        elif x == 16:
            self.lowrydining_button.pack(side='right', anchor='se',
                                         padx=200, pady=350)
        elif x == 17:
            self.macleod_button.pack(side='right', anchor='se',
                                     padx=200, pady=350)
        elif x == 18:
            self.moms_button.pack(side='right', anchor='se',
                                  padx=200, pady=350)
        elif x == 19:
            self.oldman_button.pack(side='left', anchor='se',
                                    padx=250, pady=310)
        elif x == 20:
            self.pops_button.pack(side='right', anchor='se',
                                  padx=200, pady=350)

    # change to blue color if the button is selected,
    # and change other buttons to pink (default) color
    def change_color(self, tools, x):
        self.kittredge['bg'] = tools._from_rgb((250, 240, 230))
        self.knowlton['bg'] = tools._from_rgb((250, 240, 230))
        self.lowrydining['bg'] = tools._from_rgb((250, 240, 230))
        self.macleod['bg'] = tools._from_rgb((250, 240, 230))
        self.moms['bg'] = tools._from_rgb((250, 240, 230))
        self.oldman['bg'] = tools._from_rgb((250, 240, 230))
        self.pops['bg'] = tools._from_rgb((250, 240, 230))
        if x == 14:
            self.kittredge['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 15:
            self.knowlton['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 16:
            self.lowrydining['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 17:
            self.macleod['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 18:
            self.moms['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 19:
            self.oldman['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 20:
            self.pops['bg'] = tools._from_rgb((175, 238, 238))

    # forget all the information shown on the right
    def info_forget(self):
        self.squirrel.pack_forget()
        self.dining_info.pack_forget()    # information
        self.kittredge_info.pack_forget()
        self.knowlton_info.pack_forget()
        self.lowrydining_info.pack_forget()
        self.macleod_info.pack_forget()
        self.moms_info.pack_forget()
        self.oldman_info.pack_forget()
        self.pops_info.pack_forget()
        self.kittredge_button.pack_forget()    # button
        self.knowlton_button.pack_forget()
        self.lowrydining_button.pack_forget()
        self.macleod_button.pack_forget()
        self.moms_button.pack_forget()
        self.oldman_button.pack_forget()
        self.pops_button.pack_forget()
        self.kittredge_picture.pack_forget()    # picture
        self.knowlton_picture.pack_forget()
        self.lowrydining_picture.pack_forget()
        self.macleod_picture.pack_forget()
        self.moms_picture.pack_forget()
        self.oldman_picture.pack_forget()
        self.pops_picture.pack_forget()

    # destructor, exit the dining system
    def quit(self, tools):
        self.dining_label.pack_forget()
        self.back.pack_forget()
        self.kittredge.pack_forget()
        self.knowlton.pack_forget()
        self.lowrydining.pack_forget()
        self.macleod.pack_forget()
        self.moms.pack_forget()
        self.oldman.pack_forget()
        self.pops.pack_forget()
        self.info_forget()
        self.change_color(tools, 100)


class Library():
    def __init__(self, tools, main):
        self.back = tk.Button(main.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=5, height=2,
                              command=lambda: [main.default_page(tools),
                                               tools.press_button_sound(),
                                               self.quit(tools)])

        # lib function
        self.lib_label = tk.Label(main.right_frame,
                                  textvariable=tools.lib_text,
                                  bg=tools._from_rgb((147, 112, 219)),
                                  fg='white', font=tools.helv(24),
                                  width=14, height=2)
        self.lib_info = tk.Label(main.right_frame,
                                 justify='left', wraplength=300,
                                 textvariable=tools.lib_info_text,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 fg='black', font=tools.helv(12),
                                 width=30, height=10)
        
        # picture
        self.squirrel = tk.Label(main.right_frame, image=tools.squirrel_pic,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 width=200, height=150)
        self.andrews_picture = tk.Label(main.right_frame,
                                        image=tools.andrews_pic,
                                        bg=tools._from_rgb((255, 235, 205)),
                                        width=240, height=320)
        self.gault_picture = tk.Label(main.right_frame, image=tools.gault_pic,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      width=240, height=320)
        self.timken_picture = tk.Label(main.right_frame,
                                       image=tools.timken_pic,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       width=240, height=320)

        # lib places
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

        # lib building info
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

        self.andrews_button = tk.Label(main.center_frame, image=tools.star,
                                       bg='white')
        self.gault_button = tk.Label(main.center_frame, image=tools.star,
                                     bg='white')
        self.timken_button = tk.Label(main.center_frame, image=tools.star,
                                      bg='white')

        self.lib_label.pack(side='top', fill='x')
        self.lib_info.pack(side='top', padx=20, pady=20)
        self.back.pack(side='top', padx=20, pady=30)
        self.andrews.pack(side='top', padx=20, pady=20)
        self.gault.pack(side='top', padx=20, pady=0)
        self.timken.pack(side='top', padx=20, pady=20)
        self.squirrel.pack_forget()
        self.squirrel.pack(side='top', padx=20, pady=20)

    def change_color(self, tools, x):
        self.andrews['bg'] = tools._from_rgb((250, 240, 230))
        self.gault['bg'] = tools._from_rgb((250, 240, 230))
        self.timken['bg'] = tools._from_rgb((250, 240, 230))
        if x == 2:
            self.andrews['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 3:
            self.gault['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 4:
            self.timken['bg'] = tools._from_rgb((175, 238, 238))

    def map_buttons(self, x):
        if x == 2:
            self.andrews_button.pack(side='right', anchor='se',
                                     padx=360, pady=250)
        elif x == 3:
            self.gault_button.pack(side='right', anchor='se',
                                   padx=360, pady=320)
        elif x == 4:
            self.timken_button.pack(side='left', anchor='se',
                                    padx=350, pady=230)

    def info_forget(self):
        self.squirrel.pack_forget()
        self.lib_info.pack_forget()
        self.andrews_info.pack_forget()
        self.gault_info.pack_forget()
        self.timken_info.pack_forget()
        self.andrews_button.pack_forget()
        self.gault_button.pack_forget()
        self.timken_button.pack_forget()
        self.andrews_picture.pack_forget()
        self.gault_picture.pack_forget()
        self.timken_picture.pack_forget()

    def quit(self, tools):
        self.lib_label.pack_forget()
        self.back.pack_forget()
        self.andrews.pack_forget()
        self.gault.pack_forget()
        self.timken.pack_forget()
        self.info_forget()
        self.change_color(tools, 100)


class Academic():
    def __init__(self, tools, main):
        self.back = tk.Button(main.left_frame, textvariable=tools.back_text,
                              font=tools.helv(12),
                              bg=tools._from_rgb((250, 240, 230)),
                              width=5, height=2,
                              command=lambda: [main.default_page(tools),
                                               tools.press_button_sound(),
                                               self.quit(tools)])

        # academic function
        self.aca_label = tk.Label(main.right_frame,
                                  textvariable=tools.aca_text,
                                  bg=tools._from_rgb((100, 149, 237)),
                                  fg='white', font=tools.helv(24),
                                  width=14, height=2)
        self.aca_info = tk.Label(main.right_frame,
                                 justify='left', wraplength=300,
                                 textvariable=tools.aca_info_text,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 fg='black', font=tools.helv(12),
                                 width=30, height=10)
        
        # picture
        self.squirrel = tk.Label(main.right_frame, image=tools.squirrel_pic,
                                 bg=tools._from_rgb((255, 235, 205)),
                                 width=200, height=150)
        self.ebert_picture = tk.Label(main.right_frame, image=tools.ebert_pic,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      width=240, height=320)
        self.kauke_picture = tk.Label(main.right_frame, image=tools.kauke_pic,
                                      bg=tools._from_rgb((255, 235, 205)),
                                      width=240, height=320)
        self.morgan_picture = tk.Label(main.right_frame,
                                       image=tools.morgan_pic,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       width=240, height=320)
        self.scheide_picture = tk.Label(main.right_frame,
                                        image=tools.scheide_pic,
                                        bg=tools._from_rgb((255, 235, 205)),
                                        width=240, height=320)
        self.scovel_picture = tk.Label(main.right_frame,
                                       image=tools.scovel_pic,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       width=240, height=320)
        self.severance_picture = tk.Label(main.right_frame,
                                          image=tools.severance_pic,
                                          bg=tools._from_rgb((255, 235, 205)),
                                          width=240, height=320)
        self.taylor_picture = tk.Label(main.right_frame,
                                       image=tools.taylor_pic,
                                       bg=tools._from_rgb((255, 235, 205)),
                                       width=240, height=320)
        self.williams_picture = tk.Label(main.right_frame,
                                         image=tools.williams_pic,
                                         bg=tools._from_rgb((255, 235, 205)),
                                         width=240, height=320)
        self.wishart_picture = tk.Label(main.right_frame,
                                        image=tools.wishart_pic,
                                        bg=tools._from_rgb((255, 235, 205)),
                                        width=240, height=320)

        # academic places
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

        # academic building info
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

        self.ebert_button = tk.Label(main.center_frame, image=tools.star,
                                     bg='white')
        self.kauke_button = tk.Label(main.center_frame, image=tools.star,
                                     bg='white')
        self.morgan_button = tk.Label(main.center_frame, image=tools.star,
                                      bg='white')
        self.scheide_button = tk.Label(main.center_frame, image=tools.star,
                                       bg='white')
        self.scovel_button = tk.Label(main.center_frame, image=tools.star,
                                      bg='white')
        self.severance_button = tk.Label(main.center_frame, image=tools.star,
                                         bg='white')
        self.taylor_button = tk.Label(main.center_frame, image=tools.star,
                                      bg='white')
        self.williams_button = tk.Label(main.center_frame, image=tools.star,
                                        bg='white')
        self.wishart_button = tk.Label(main.center_frame, image=tools.star,
                                       bg='white')

        self.aca_label.pack(side='top', fill='x')
        self.aca_info.pack(side='top', padx=20, pady=20)
        self.back.pack(side='top', padx=20, pady=30)
        self.ebert.pack(side='top', padx=20, pady=20)
        self.kauke.pack(side='top', padx=20, pady=0)
        self.morgan.pack(side='top', padx=20, pady=20)
        self.scheide.pack(side='top', padx=20, pady=0)
        self.scovel.pack(side='top', padx=20, pady=20)
        self.severance.pack(side='top', padx=20, pady=0)
        self.taylor.pack(side='top', padx=20, pady=20)
        self.williams.pack(side='top', padx=20, pady=0)
        self.wishart.pack(side='top', padx=20, pady=20)
        self.squirrel.pack_forget()
        self.squirrel.pack(side='top', padx=20, pady=20)

    def change_color(self, tools, x):
        self.ebert['bg'] = tools._from_rgb((250, 240, 230))
        self.kauke['bg'] = tools._from_rgb((250, 240, 230))
        self.morgan['bg'] = tools._from_rgb((250, 240, 230))
        self.scheide['bg'] = tools._from_rgb((250, 240, 230))
        self.scovel['bg'] = tools._from_rgb((250, 240, 230))
        self.severance['bg'] = tools._from_rgb((250, 240, 230))
        self.taylor['bg'] = tools._from_rgb((250, 240, 230))
        self.williams['bg'] = tools._from_rgb((250, 240, 230))
        self.wishart['bg'] = tools._from_rgb((250, 240, 230))
        if x == 5:
            self.ebert['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 6:
            self.kauke['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 7:
            self.morgan['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 8:
            self.scheide['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 9:
            self.scovel['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 10:
            self.severance['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 11:
            self.taylor['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 12:
            self.williams['bg'] = tools._from_rgb((175, 238, 238))
        elif x == 13:
            self.wishart['bg'] = tools._from_rgb((175, 238, 238))

    def map_buttons(self, x):
        if x == 5:
            self.ebert_button.pack(side='left', anchor='ne',
                                   padx=250, pady=310)
        elif x == 6:
            self.kauke_button.pack(side='left', anchor='se',
                                   padx=250, pady=310)
        elif x == 7:
            self.morgan_button.pack(side='left', anchor='se',
                                    padx=190, pady=45)
        elif x == 8:
            self.scheide_button.pack(side='right', anchor='se',
                                     padx=220, pady=110)
        elif x == 9:
            self.scovel_button.pack(side='left', anchor='se',
                                    padx=190, pady=115)
        elif x == 10:
            self.severance_button.pack(side='left', anchor='se',
                                       padx=310, pady=118)
        elif x == 11:
            self.taylor_button.pack(side='left', anchor='se',
                                    padx=95, pady=235)
        elif x == 12:
            self.williams_button.pack(side='left', anchor='se',
                                      padx=310, pady=45)
        elif x == 13:
            self.wishart_button.pack(side='left', anchor='se',
                                     padx=80, pady=120)

    def info_forget(self):
        self.squirrel.pack_forget()
        self.aca_info.pack_forget()    # info
        self.ebert_info.pack_forget()
        self.kauke_info.pack_forget()
        self.morgan_info.pack_forget()
        self.scheide_info.pack_forget()
        self.scovel_info.pack_forget()
        self.severance_info.pack_forget()
        self.taylor_info.pack_forget()
        self.williams_info.pack_forget()
        self.wishart_info.pack_forget()
        self.ebert_button.pack_forget()    # button
        self.kauke_button.pack_forget()
        self.morgan_button.pack_forget()
        self.scheide_button.pack_forget()
        self.scovel_button.pack_forget()
        self.severance_button.pack_forget()
        self.taylor_button.pack_forget()
        self.williams_button.pack_forget()
        self.wishart_button.pack_forget()
        self.ebert_picture.pack_forget()    # picture
        self.kauke_picture.pack_forget()
        self.morgan_picture.pack_forget()
        self.scheide_picture.pack_forget()
        self.scovel_picture.pack_forget()
        self.severance_picture.pack_forget()
        self.taylor_picture.pack_forget()
        self.williams_picture.pack_forget()
        self.wishart_picture.pack_forget()

    def quit(self, tools):
        self.aca_label.pack_forget()
        self.back.pack_forget()
        self.ebert.pack_forget()
        self.kauke.pack_forget()
        self.morgan.pack_forget()
        self.scheide.pack_forget()
        self.scovel.pack_forget()
        self.severance.pack_forget()
        self.taylor.pack_forget()
        self.williams.pack_forget()
        self.wishart.pack_forget()
        self.info_forget()
        self.change_color(tools, 100)
