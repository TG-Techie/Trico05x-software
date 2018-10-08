from tg_modules import tg_gui as gui
from staging import gui_parameters as params
from system.handler import load as load_program

#this is to make it easier to code 
def color(a,b,c):
    return gui.io.color(abc)

#shape param to make it easier fro coder
cont_x = params.prog_cont_x
cont_y = params.prog_cont_y
cont_width = params.prog_cont_width
cont_height = params.prog_cont_height
# the the x and y should always be added to new componets ina dditon to otehr xs ans ys    

#the blank container used for all progs
container = gui.spoc(params.prog_cont_x, params.prog_cont_y,
                    params.prog_cont_width, params.prog_cont_height)



#start with the screen all white so scren whipes
gui.io.rect(params.prog_cont_x, params.prog_cont_y,
            params.prog_cont_width, params.prog_cont_height,
            params.gui_white)



#default things for the user to change. like 'keep on refreshing me'
setattr(container,'wants_refresh',True)
#READ BELOW!!!!!
# to turn refreshing off do: container.wants_refresh = False

def container_move(buttons):
    pass

def buttons_pressed(buttons):
    pass