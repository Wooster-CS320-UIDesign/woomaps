import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import font as tkFont
from pygame import mixer


class Tools():
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.with_sound = True
        self.language_state = 0    # default language is English

        self.star = tk.PhotoImage(file='star.png').subsample(13, 13)
        
        # picture
        self.squirrel_pic = tk.PhotoImage(file='Squirrel.png')
        self.kittredge_pic = tk.PhotoImage(file='Kitt.png')
        self.knowlton_pic = tk.PhotoImage(
            file='Knowlton.png')
        self.lowrydining_pic = tk.PhotoImage(
            file='Lowry.png')
        self.macleod_pic = tk.PhotoImage(file='CStore.png')
        self.moms_pic = tk.PhotoImage(file='Moms.png')
        self.oldman_pic = tk.PhotoImage(file='OldMain.png')
        self.pops_pic = tk.PhotoImage(file='Pops.png')
        self.andrews_pic = tk.PhotoImage(file='Andrews.png')
        self.gault_pic = tk.PhotoImage(file='Gault.png')
        self.timken_pic = tk.PhotoImage(file='Timken.png')
        self.ebert_pic = tk.PhotoImage(file='Ebert.png')
        self.kauke_pic = tk.PhotoImage(file='Kauke.png')
        self.morgan_pic = tk.PhotoImage(file='Morgan.png')
        self.scheide_pic = tk.PhotoImage(file='Scheide.png')
        self.scovel_pic = tk.PhotoImage(file='Scovel.png')
        self.severance_pic = tk.PhotoImage(
            file='Severance.png')
        self.taylor_pic = tk.PhotoImage(file='Taylor.png')
        self.williams_pic = tk.PhotoImage(
            file='Williams.png')
        self.wishart_pic = tk.PhotoImage(file='Wishart.png')

        # text var
        self.wooster_name = tk.StringVar()
        self.wooster_intro = tk.StringVar()
        self.back_text = tk.StringVar()
        self.home_text = tk.StringVar()
        self.dining_text = tk.StringVar()     # right label
        self.lib_text = tk.StringVar()
        self.aca_text = tk.StringVar()
        self.guide_text = tk.StringVar()
        self.info_text = tk.StringVar()
        self.dining_left_text = tk.StringVar()     # left label
        self.lib_left_text = tk.StringVar()
        self.aca_left_text = tk.StringVar()
        self.guide_left_text = tk.StringVar()
        self.info_left_text = tk.StringVar()
        self.setting_text = tk.StringVar()    # setting
        self.language_text = tk.StringVar()
        self.about_text = tk.StringVar()
        self.product_text = tk.StringVar()
        self.go_back = tk.StringVar()
        self.moms_info = tk.StringVar()    # dining
        self.oldman_info = tk.StringVar()
        self.knowlton_info = tk.StringVar()
        self.lowrydining_info = tk.StringVar()
        self.kittredge_info = tk.StringVar()
        self.pops_info = tk.StringVar()
        self.macleod_info = tk.StringVar()
        self.lowry = tk.StringVar()           # navigation
        self.andrews = tk.StringVar()
        self.kauke = tk.StringVar()
        self.taylor = tk.StringVar()
        self.departure = tk.StringVar()
        self.destination = tk.StringVar()
        self.search = tk.StringVar()
        self.lowry_info = tk.StringVar()      # building info
        self.andrews_info = tk.StringVar()
        self.kauke_info = tk.StringVar()
        self.taylor_info = tk.StringVar()
        self.williams_info = tk.StringVar()
        self.severance_info = tk.StringVar()
        self.ebert_info = tk.StringVar()
        self.scheide_info = tk.StringVar()
        self.morgan_info = tk.StringVar()
        self.gault_info = tk.StringVar()
        self.wishart_info = tk.StringVar()
        self.scovel_info = tk.StringVar()
        self.timken_info = tk.StringVar()
        self.dining_info_text = tk.StringVar()
        self.lib_info_text = tk.StringVar()
        self.aca_info_text = tk.StringVar()
        self.llroute_text = tk.StringVar()    # route
        self.laroute_text = tk.StringVar()
        self.lkroute_text = tk.StringVar()
        self.ltroute_text = tk.StringVar()
        self.alroute_text = tk.StringVar()
        self.aaroute_text = tk.StringVar()
        self.akroute_text = tk.StringVar()
        self.atroute_text = tk.StringVar()
        self.klroute_text = tk.StringVar()
        self.karoute_text = tk.StringVar()
        self.kkroute_text = tk.StringVar()
        self.ktroute_text = tk.StringVar()
        self.tlroute_text = tk.StringVar()
        self.taroute_text = tk.StringVar()
        self.tkroute_text = tk.StringVar()
        self.ttroute_text = tk.StringVar()

    def language_update(self, language_index):    # 0 = English, 1 = Chinese
        if language_index == 0:
            self.wooster_name.set('''The College\nof Wooster''')    # intro
            self.wooster_intro.set('''This is an introduction of the College \
of Wooster. This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. \
This is an introduction of the College of Wooster. ''')
            self.home_text.set('Home')
            self.back_text.set('Back')
            self.dining_text.set('Campus\nDining')     # right label
            self.lib_text.set('Library')
            self.aca_text.set('Academic\nBuilding')
            self.guide_text.set('Navigation')
            self.info_text.set('Building\nInformation')
            self.dining_left_text.set('Campus Dining')     # left label
            self.lib_left_text.set('Library')
            self.aca_left_text.set('Academic Building')
            self.guide_left_text.set('Navigation')
            self.info_left_text.set('Building Information')
            self.setting_text.set('General')          # setting
            self.language_text.set('Language')
            self.about_text.set('About us')
            self.product_text.set('Made by: \nXiangping Ouyang, Yifan Huang')
            self.go_back.set('Press anywhere to go back')
            self.moms_info.set('''Mom's Truckstop\n\nA restaurant located in \
Lowry Student Center.''')          # dining
            self.oldman_info.set('''Old Main Café\n\nA café located in Kauke \
Hall.''')
            self.knowlton_info.set('''The Knowlton Café\n\nA café located in \
Williams Hall.''')
            self.lowrydining_info.set('''Lowry Center Dining Hall\n\nThe \
main dining hall on campus.''')
            self.kittredge_info.set('''Kittredge Dining Hall\n\nA dining \
hall located between Compton and Wagner Halls.''')
            self.pops_info.set('''Pop's Grab and Go Sandwich Shop\n\nA \
dining option located in Lowry Student Center.''')
            self.macleod_info.set('''MacLeod's Coffee Bar and Convenience \
Store\n\nA convenience store located in Lowry Student Center.''')
            self.lowry.set('Lowry')                   # navigation
            self.kauke.set('Kauke')
            self.andrews.set('Andrews')
            self.taylor.set('Taylor')
            self.departure.set('Departure')
            self.destination.set('Destination')
            self.search.set('Go!')
            # building information
            self.lowry_info.set('''Lowry Student Center\n\nThe main center \
of campus activity. Holds the main Dining hall and many other centers for \
campus activities.''')
            self.andrews_info.set('''Andrews Library\n\nOne of the main \
libraries on campus.''')
            self.kauke_info.set('''Kauke Hall\n\nAcademic building for \
History, and Social Sciences.''')
            self.taylor_info.set('''Taylor Hall\n\nAcademic building for \
Math, Physics, and Computer Science.''')
            self.williams_info.set('''Williams Hall of Life Science\n\n\
Academic building for Biology, Biochemistry & Molecular Biology, \
Environmental studies, and Neuroscience.''')
            self.severance_info.set('''Severance Hall\n\nAcademic building \
for Chemistry.''')
            self.ebert_info.set('''Ebert Art Center\n\nAcademic building for \
Art History, Design/Digital Communications, and Studio Art. Also the campus \
art museum.''')
            self.scheide_info.set('''Scheide Music Center\n\nAcademic \
building for Music.''')
            self.morgan_info.set('''Burton D. Morgan Hall\n\nAcademic \
building for Economics, \
Psychology, and Education. Also the center for campus Information \
Technology.''')
            self.gault_info.set('''Gault Library\n\nOne of the main \
libraries on campus. Also the center for APEX.''')
            self.wishart_info.set('''Wishart Hall\n\nAcademic building for \
Communications and Theatre and Dance.''')
            self.scovel_info.set('''Scovel Hall\n\nAcademic building for \
Earth Science and Philosophy.''')
            self.timken_info.set('''Timken Library in Frick Hall\n\nOne of \
the main libraries on campus focusing on the sciences.''')
            self.dining_info_text.set('''This is an overview of school \
campus dining.''')
            self.aca_info_text.set('''This is an overview of school academic \
building.''')
            self.lib_info_text.set('This is an overview of school library.')
            self.llroute_text.set('Same departure and destination.')    # route
            self.laroute_text.set('''Estimate time: 1.5min\n\n\
Exit from the west side of the building, head south on Beall, \
cross Beall to get to east door of Andrews Library.''')
            self.lkroute_text.set('''Estimate time: 2.5min\n\n\
Exit the west side of the building, cross Beall and follow the path west to \
reach the arch of Kauke.''')
            self.ltroute_text.set('''Estimate time: 5min\n\nExit the west \
side of the building, cross Beall and follow the path west, turn south at \
the end of the path and follow it to the north entrance of Taylor. ''')
            self.alroute_text.set('''Estimate time: 1.5min\n\nExit the east \
side of the building, cross Beall, head north on Beall to reach the east \
entrance of Lowry. ''')
            self.aaroute_text.set('''Same departure and destination''')
            self.akroute_text.set('''Estimate time: 1.5min\n\nExit the west \
side of the building, follow the path west past Timken, turn north, and \
follow the path to reach the east entrance of Kauke.''')
            self.atroute_text.set('''Estimate time: 4.5min\n\nExit the west \
side of the building, head north on the path, then turn west on the path \
follow that path to the end then turn south and head to the north entrance \
of Taylor.''')
            self.klroute_text.set('''Estimate time: 2.5min\n\nExit the \
building into the arch and go north, turn east on the path, follow the \
path across Beall to reach the east entrance of Lowry. ''')
            self.karoute_text.set('''Estimate time: 1.5min\n\nExit from the \
east side of the building, head south on the path toward Timken, turn east \
before timken and follow the path to the west entrance of Andrews Library.''')
            self.kkroute_text.set('''Same departure and destination.''')
            self.ktroute_text.set('''Estimate time: 2min\n\nExit the \
building into the arch and go north, turn west on the path, follow the path \
to the end, then turn south and follow that path to the north entrance of \
Taylor.''')
            self.tlroute_text.set('''Estimate time: 5min\n\nExit from the \
north side of the building, head north on the path between McGaw and the \
parking lot toward Kauke. Turn east on the path past Kauke, follow the path \
across Beall to reach the east entrance of Lowry. ''')
            self.taroute_text.set('''Estimate time: 4.5min\n\nExit from the \
north side of the building, head north on the path between McGaw and the \
parking lot toward Kauke. Turn east on the path past Kauke, turn south \
before Gault library, follow the path to the west entrance of Andrews \
Library. ''')
            self.tkroute_text.set('''Estimate time: 2min\n\nExit from the \
north side of the building, head north on the path between McGaw and the \
parking lot, turn east on the path and follow it to reach the arch of \
Kauke.''')
            self.ttroute_text.set('''Same departure and destination.''')
        elif language_index == 1:
            self.wooster_name.set('伍斯特学院')
            self.wooster_intro.set('''这是伍斯特学院的简介。这是伍斯特学院的简介。\
这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。\
这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。\
这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。\
这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。\
这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。这是伍斯特学院的简介。''')
            self.home_text.set('主页')
            self.back_text.set('返回')
            self.dining_text.set('餐饮')    # right label
            self.lib_text.set('图书馆')
            self.aca_text.set('教学楼')
            self.guide_text.set('导航')
            self.info_text.set(' 建筑信息 ')
            self.dining_left_text.set('餐饮')     # left label
            self.lib_left_text.set('图书馆')
            self.aca_left_text.set('教学楼')
            self.guide_left_text.set('导航')
            self.info_left_text.set('   建筑信息   ')
            self.setting_text.set('常规')    # setting
            self.language_text.set('语言')
            self.about_text.set('关于我们')
            self.product_text.set('制作人：\n欧阳湘萍，黄一凡')
            self.go_back.set('点击任意位置返回')
            self.moms_info.set('这是moms的介绍。')    # dining
            self.oldman_info.set('这是oldman的介绍。')
            self.knowlton_info.set('这是knowlton的介绍。')
            self.lowrydining_info.set('这是lowry dining的介绍。')
            self.kittredge_info.set('这是kittredge的介绍。')
            self.pops_info.set('这是pops的介绍。')
            self.macleod_info.set('这是macleod的介绍。')
            self.departure.set('出发地')    # navigation
            self.destination.set('目的地')
            self.search.set('出发')
            self.lowry_info.set('这是关于Lowry的信息。')    # building information
            self.andrews_info.set('这是关于andrews的信息。')
            self.kauke_info.set('这是关于kauke的信息。')
            self.taylor_info.set('这是关于taylor的信息。')
            self.williams_info.set('这是关于williams的信息。')
            self.severance_info.set('这是关于severance的信息。')
            self.ebert_info.set('这是关于ebert的信息。')
            self.scheide_info.set('这是关于scheide的信息。')
            self.morgan_info.set('这是关于morgan的信息。')
            self.gault_info.set('这是关于gault的信息。')
            self.wishart_info.set('这是关于wishart的信息。')
            self.scovel_info.set('这是关于scovel的信息。')
            self.timken_info.set('这是关于timken的信息。')
            self.dining_info_text.set('这是关于餐饮的信息。')
            self.aca_info_text.set('这是关于教学楼的信息。')
            self.lib_info_text.set('这是关于图书馆信息。')
            self.llroute_text.set('需要翻译')    # route
            self.laroute_text.set('需要翻译')
            self.lkroute_text.set('需要翻译')
            self.ltroute_text.set('需要翻译')
            self.alroute_text.set('需要翻译')
            self.aaroute_text.set('需要翻译')
            self.akroute_text.set('需要翻译')
            self.atroute_text.set('需要翻译')
            self.klroute_text.set('需要翻译')
            self.karoute_text.set('需要翻译')
            self.kkroute_text.set('需要翻译')
            self.ktroute_text.set('需要翻译')
            self.tlroute_text.set('需要翻译')
            self.taroute_text.set('需要翻译')
            self.tkroute_text.set('需要翻译')
            self.ttroute_text.set('需要翻译')

    def _from_rgb(self, rgb):
        '''translates an rgb tuple of int to a tkinter friendly color code
        '''
        return '#%02x%02x%02x' % rgb

    def helv(self, number):
        return tkFont.Font(family='Helvetica', size=number,
                           weight=tkFont.BOLD)

    def ariel(self, number):
        return tkFont.Font(family='Ariel', size=number,
                           weight=tkFont.NORMAL)

    def press_button_sound(self):
        if self.with_sound:
            mixer.init()
            mixer.music.load('Mouse_Click_Sound_Effect.mp3')
            mixer.music.play()

    def button_sound_update(self):
        if self.with_sound:
            self.with_sound = False
        else:
            self.with_sound = True

    def on_closing(self):
        if tkm.askokcancel('Quit', 'Do you want to quit WooMaps?'):
            self.root.destroy()
