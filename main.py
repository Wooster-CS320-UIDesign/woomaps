from home import *
import tkinter as tk
from tools import Tools

tools = Tools()
tools.root.title('WooMaps')
tools.root.geometry("1450x850")
WooMap = tk.PhotoImage(file='WooMap.png')
tools.root.iconphoto(False, WooMap)
app = Home_page(tools)
