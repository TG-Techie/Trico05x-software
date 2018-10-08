from tg_modules import tg_gui as gui
from staging import gui_parameters as params
#from staging.sensor import time

container = gui.naoc(params.sys_bar_x, params.sys_bar_y, params.sys_bar_width,
                params.sys_bar_height - params.sys_bar_line_height,
                params.gui_background)

'''def place():
    gui.io.rect(params.sys_bar_x, params.sys_bar_y, params.sys_bar_width,
                params.sys_bar_height - params.sys_bar_line_height,
                params.gui_background)
    
    gui.io.rect(params.sys_bar_x,
                params.sys_bar_y + params.sys_bar_height - params.sys_bar_line_height,
                params.sys_bar_width, params.sys_bar_line_height,
                params.sys_bar_line_color)
    
    refresh()

import random
def refresh():
    gui.io.text(params.sys_bar_x, params.sys_bar_y,
    'this is filler:'+str(random.randrange(1000, 9999)) + ' __bata4__ ;-)')

def clear():
    gui.io.rect(params.sys_bar_x, params.sys_bar_y, params.sys_bar_width,
                params.sys_bar_height, params.gui_background)'''