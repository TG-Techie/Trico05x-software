
from system.programs.__blank__program import *
from system import handler
from os import listdir
from sys import stdin
from math import ceil
import time

container.wants_refresh = False

prog_list = []

for prog in listdir('./lib/programs'):
    #print(prog)
    #print(prog[-3:])
    #print(prog[0:2])
    if (prog[0:2] != '._') and (prog[0:2] != '__') and (prog[-3:] == '.py'):
        prog_list.append(prog[0:-3])

#VVV buttons per page VVV
bpp = params.launcher_cols * params.launcher_rows  -2
prog_to_assign = 0

#this removes all pages from the container to have a fresh start
container.contents = []

#locations of lower corners in menus
prev_but_pos = (0,params.launcher_rows-1)
next_but_pos = (params.launcher_cols-1,params.launcher_rows-1)

#a func for if a button has no prog in it
def no_prog_button(but):
    gui.io.if_rect(but.x,but.y,but.width,but.height,but.r, gui.io.red)
    gui.io.text(but.x+but.r,but.y+but.r,'No\nProg', background = gui.io.red)
    time.sleep(2)
    but.place()

for page_num in range(1 + ceil(  len(prog_list)/bpp ) ):
    #add a page to the launcher and set a pointer to it, not named bup called panel then soem number
    page_pointer = container.add_panel()
    
    #ass a menu (nidos) to the page
    page_pointer.add(menu = gui.nidos(cont_x,cont_y,cont_width, cont_height,
                params.launcher_rows, params.launcher_cols, move_mode = params.gui_move_mode,
                select = params.init_select, superior = container))
    
    #point the the created menu, which now has the name menu
    menu_pointer = page_pointer.menu
    
    #for each in x,y coords of buttons
    for but_x in range(menu_pointer.cols):
        for but_y in range(menu_pointer.rows):
            
            #point the the current button
            but_pointer = menu_pointer.of(but_x,but_y)
            #check if the button isn't a lower corder button
            if ((but_x,but_y) != prev_but_pos) and  ((but_x,but_y) != next_but_pos):
                try:
                    but_pointer.change_text(prog_list[prog_to_assign].replace('__','\n'))
                    but_pointer.set_purpose(handler.load,(prog_list[prog_to_assign],))
                    prog_to_assign += 1
                except:
                    #print('no prog in this but')
                    but_pointer.set_purpose(no_prog_button,(but_pointer,))
            #lower left
            elif but_pointer == menu_pointer.of(*prev_but_pos):
                but_pointer.change_text('''prev\npage''')
                but_pointer.set_purpose(container.move,(-1,))
            #lower right
            elif but_pointer == menu_pointer.of(*next_but_pos):
                but_pointer.change_text('''next\npage''')
                but_pointer.set_purpose(container.move,(1,))
            #put a function in any buttons w/out a purpose

container.switch(container.contents[0], place = 0)



#THIS CODE WAS USED TO TEST FEATURES: DELETE LATER
''''#while 1:
container.current.menu.move_mode = 2
while 1:
    container.current.menu.press()
    for i in range(3):
        container.current.menu.move(-1,0)
        time.sleep(.1)'''
    

#print(container.current.contents[0].of(0,-1).text)
#container.current.menu.press()