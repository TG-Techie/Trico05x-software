from system.programs.__blank__program import *
#from tg_modules import tg_gui as gui
#from staging import sen_brd as sensor
from staging import sensor
import time

#container.fill(gui.io.blue)
#gui.io.fill(gui.io.color(0,0,255))

#make a thermal display and add it to the program visula container 


container.panel0.add( menu = gui.nidos(cont_x + 96, cont_y, cont_width - 96, 96 + 3, 3, 1))

container.panel0.add(therm = gui.thermal_display(cont_x,cont_y,96,96,sensor.thermal_cam_data, (),
                                    border = 4, flip_x = 1, units_out = 2, place = 0), select = params.init_select)


#this section is to customise my nidos
pointer = container.panel0.menu.of(0,0) #makes it easier to type

pointer.change_text('''Units:
C/F/K''')
#make a function to set at what the button does  (b/c i suck at lamdas)
def therm_unit_toggle():
    container.panel0.therm.units_out = (container.panel0.therm.units_out +1)%3 + 1
    container.panel0.therm.refresh()
#pass the function to the button
pointer.set_purpose(therm_unit_toggle,())


#next button
#this one toglles weather or not the photo shoudl be refreshed
pointer = container.panel0.menu.of(0,1)
pointer.change_text(""" cont.
refresh""")
def toggle_refresh():
    prog_wants_refresh = not bool(container.prog_wants_refresh)
pointer.set_purpose(toggle_refresh,())


#next button
#this one refreshes the image once
pointer = container.panel0.menu.of(0,2)
pointer.change_text('''Single
Refresh''')
pointer.set_purpose(container.panel0.therm.refresh,())


"""this section is important if you want to have controls in your program"""
#finish upper
#change this at anytime to swich what menu will recieve button presses



