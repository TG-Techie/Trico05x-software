 # use this to adapt your dispay libaray to TG_GUI compatible code
#this means please do not change the line stating with define in this document
#only change the contense of the funct s

#DEFAULTS AT BOTTOM


# my choosen scrren library:
from staging.disp import disp,color as disp_color

####enter these:
screen_width = disp.width
screen_height = disp.height

def color(r,g,b):
    # you will get 255 data !!!!!!
    return disp_color(r,g,b)

def rect(x,y,width,height,color):
    disp.rect(x,y,width,height,color)
    del x,y,width,height,color

#NEED THIS 
def round_rect(x,y,width,height,r,color):
    disp.round_rect(x,y,width,height,r,color)
    del x,y,width,height,r,color
#NEED THIS ^^^^

def if_rect(x,y,width,height,r,color):
    if r:
        round_rect(x,y,width,height,r,color)
    else:
        rect(x,y,width,height,color)
    del x,y,width,height,r,color

def text(x,y,text,color = color(255,255,255),background = 0, size = 1):
    disp.text(x,y,text,color=color,background=background, size=size)
    del x,y,text,color,background, size

def text_dimensions(x,y,text, size = 1):
    tup = disp.text_dimension (x,y,text, size)
    del x,y,text, size
    return tup
    del tup

def fill(color):
    disp.fill(color)
    del color



# Defaults:
#general:
red = color(255,0,0)
orange = color(255,128,0)
yellow = color(255,255,0)
green = color(0,255,0)
blue = color(0,0,255)
purple = color(128,0,255)
white = color(255,255,255)
black = color(0,0,0)


background_color =  color(0,0,0)

#menus and nidos' (navigatable informat  dispensing object systems)
nidos_background =  background_color

standard_color =  color(5,85,110)

#buttons:
button_color_norm = standard_color
button_clear_color = nidos_background
button_color_sel =  color(128,255,255)

text_color_norm =  color(255,255,255)
text_color_sel =  color(0,0,0)