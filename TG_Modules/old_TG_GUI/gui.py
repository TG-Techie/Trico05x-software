from tg_modules.tasking import task, thread_list
from TG_Modules import screen_io as io

#--------------------------------------------------------------------------------------------------
#initial structure
#--------------------------------------------------------------------------------------------------
class pject(): 
    #placable object

    def __init__(self,x,y, place_func, place_arg, clear_func, clear_arg):
        self.x = x
        self.y = y

        self.place_list = thread_list(1)
        self.place_list.add_task(place_func, place_arg)
        
        self.clear_list = thread_list(1)
        self.clear_list.add_task(clear_func, clear_arg)
        
        del x,y, place_func, place_arg

    def place(self):
        self.place_list.chug(delete = False)
        
    def clear(self):
        self.clear_list.chug(delete = False)

    def add_touch_target(self):
        pass

    def touched(self):
        pass

'''class uject():
    
    def__init__(self, upade_func, ):
        self.update_func = update_func'''


class selectable(pject):
    #selectable and placable object
    
    def __init__(self,x,y, place_func,place_arg, clear_func, clear_arg,
                 sel_func,sel_arg, inact_func,inact_arg):
        
        self.x = x
        self.y = y
        
        pject.__init__(self,self.x,self.y, self.place_func, self.place_arg,self.clear_func,self.clear_arg)

        
        self.selected = False
        self.active = True
        
        self.place_func = place_func
        self.place_arg = place_arg
        self.clear_func = clear_func
        self.clear_arg = clear_arg
        
        self.sel_func = sel_func
        self.sel_arg = sel_arg
        self.inact_func = inact_func
        self.inact_arg = inact_arg
        
        self.format_lists()
        
        del self,x,y, place_func,place_arg, clear_func, clear_arg, sel_func,sel_arg, inact_func,inact_arg

    
    def format_lists(self):
        
        pject.__init__(self,self.x,self.y, self.place_func, self.place_arg,self.clear_func,self.clear_arg)
        
        self.sel_list = thread_list(1)
        self.sel_list.add_task(self.sel_func, self.sel_arg)

        self.inact_list = thread_list(1)
        self.inact_list.add_task(self.inact_func, self.inact_arg)

        
        
    def place(self):
        if self.active == False:
            self.inact_list.chug(delete = False)
        elif self.selected :
            self.sel_list.chug(delete = False)
        else:
            self.place_list.chug(delete = False)
    

    def select(self, place = 1):
        self.selected = True
        if place:
            self.place()

    def deselect(self, place = 1):
        self.selected = False
        if place:
            self.place()

    def activate(self, place = 1):
        self.active = True
        if place:
            self.place()

    def deactivate(self, place = 1):
        self.active = False
        if place:
            self.place()

#--------------------------------------------------------------------------------------------------
#buttons
#--------------------------------------------------------------------------------------------------
class button(selectable):
    def __init__(self,x,y, width, height, r ,purpose_func, purpose_arg,
                 color = io.button_color_norm,
                 clear_color = io.button_clear_color,
                 color_sel = io.button_color_sel,
                 color_inact = io.button_color_inact):
            
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
        self.r = r
                              
        self.color = color
        self.clear_color = clear_color
        self.color_sel = color_sel
        self.color_inact = color_inact
        
        self.format()
        
        self.purpose_list = thread_list(1)
        self.purpose_list.add_task(purpose_func, purpose_arg)
        
        selectable.__init__(self,
                            self.x, self.y,
                            io.if_rect, (self.x,self.y,self.width,self.height,self.r,self.color),
                            io.if_rect, (self.x,self.y,self.width, self.height, self.r, self.clear_color),
                            io.if_rect, (self.x,self.y,self.width,self.height,self.r,self.color_sel),#selected placing
                            io.if_rect, (self.x,self.y,self.width,self.height,self.r,self.color_inact))#inactive placing

        del x,y, width, height, r ,purpose_func, purpose_arg, color, clear_color, color_sel, color_inact
        
    def format(self): #, extra_task_list = None):        
        self.place_func = io.if_rect
        self.place_arg = (self.x,self.y,self.width,self.height,self.r,self.color)
        
        self.clear_func = io.if_rect
        self.clear_arg = (self.x,self.y,self.width, self.height, self.r, self.clear_color)
        
        self.sel_func = io.if_rect
        self.sel_arg = (self.x,self.y,self.width,self.height,self.r,self.color_sel)
        
        self.inact_func = io.if_rect
        self.inact_arg = (self.x,self.y,self.width,self.height,self.r,self.color_inact)
        
        self.format_lists()
    
    def implement(self):
        self.format()
    
    #def clear(self):
        #io.if_rect(self.x,self.y,self.width,self.height,self.r,self.clear_color)
    
    def repurpose(self, new_Purpose_func, new_purpose_arg):
        self.purpose_list = thread_list(1)
        self.purpose_list.add_task(new_Purpose_func, new_purpose_arg)
        
        
    def relocate(self,x,y, place = 0, implement = 1):#, extra_task_list = None):
        self.x = x
        self.y = y
        if place:
            self.clear()
        if implement:
            self.format()
            if place:
                self.place()
        
    def recolor(self,
                 color = io.button_color_norm,
                 clear_color = io.button_clear_color,
                 color_sel = io.button_color_sel,
                 color_inact = io.button_color_inact, 
                 place = 0, implement = 1):
        
        self.color = color
        self.clear_color = clear_color
        self.color_sel = color_sel
        self.color_inact = color_inact
        if implement:
            self.format()
        if place:
            self.place()
        
    def reshape(self, width, height, r = None, place = 1, implement = 1):
        self.width = width
        self.height = height
        self.r = r
        if place:
            self.clear()
        if implement:
            self.format()
            if place:
                self.place()
    
    def press_animation(self):
        self.place_list.chug(delete = False)
        self.sel_list.chug(delete = False)
    
    def press(self):
         if self.active and self.selected:  
            self.press_animation() 
            self.purpose_list.chug(delete = False)
            
#--------------------------------------------------------
# text button
class text_button(button):

    def __init__(self,x,y, width, height, r , text ,purpose_func, purpose_arg,
                x_offset = 0, y_offset = 0,
                color = io.button_color_norm,
                clear_color = io.button_clear_color,
                color_sel = io.button_color_sel,
                color_inact = io.button_color_inact,
                text_color = io.text_color_norm,
                text_color_sel = io.text_color_sel,
                text_color_inact = io.text_color_inact):

        button.__init__(self,x,y, width, height, r ,purpose_func, purpose_arg,
                 color , clear_color, color_sel, color_inact)

        self.text = text
        self.text_color = text_color
        self.text_color_sel = text_color_sel
        self.text_color_inact = text_color_inact
        
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.format()
        self.format_text()
    
    def format_text(self):
        
        try:
            self.place_list.thread_list[1].pop(0)
            self.sel_list.thread_list[1].pop(0)
            self.inact_list.thread_list[1].pop(0)
        except IndexError:
            pass
        
        text_dim = io.text_dimensions(self.x,self.y,self.text)
        
        self.place_list.add_task(io.text,(int(self.x + self.x_offset+(self.width - text_dim[0])/2)
                                ,int(self.y + self.y_offset+(self.height-text_dim[1])/2),self.text,
                                self.text_color,self.color), priority = 1)
        self.sel_list.add_task(io.text,(int(self.x + self.x_offset+(self.width - text_dim[0])/2)
                                ,int(self.y + self.y_offset+(self.height-text_dim[1])/2),self.text,
                                self.text_color_sel,self.color_sel), priority = 1)
        self.inact_list.add_task(io.text,(int(self.x + self.x_offset+(self.width - text_dim[0])/2)
                                ,int(self.y + self.y_offset+(self.height-text_dim[1])/2),self.text,
                                self.text_color_inact,self.color_inact), priority = 1)
        
        self.text_dim = text_dim[0:2]
        
        
    def implement(self):
        button.implement(self)
        self.format_text()
    
    def relocate(self, x,y, place = 1, implement = 1):
        if place:
            self.clear()
        button.relocate(self,x,y, place = 0, implement = 0)
        if implement:
            self.format()
            self.format_text()
            if place:
                self.place()
    
    def recolor(self, 
                 color = io.button_color_norm,
                 clear_color = io.button_clear_color,
                 color_sel = io.button_color_sel,
                 color_inact = io.button_color_inact,
                 text_color = io.text_color_norm,
                 text_color_sel = io.text_color_sel,
                 text_color_inact = io.text_color_inact,
                 place = 1, implement = 1):
        
        button.recolor(self,
                        color, 
                        clear_color, 
                        color_sel,
                        color_inact,
                        place = 0, implement = 0)
        
        self.text_color = text_color
        self.text_color_sel = text_color_sel
        self.text_color_inact = text_color_inact
        
        if implement:
            self.format()
            self.format_text()
            if place:
                self.place()
        
    def change_text(self, new_text, x_offset = 0, y_offset = 0, place = 1, implement = 1):
        self.text = new_text
        self.x_offset = x_offset
        self.y_offset = y_offset
        if implement:
            self.format_text()
            if place:
                self.place()
        
    
    
    def reshape(self, width, height, r, place = 1):
        if place:
            self.clear()
        button.reshape(self,width,height,r,0)
        self.format_text()
        if place:
            self.place()
  



  
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #ADD SYMBOL PLACING BUTTON AHAHAHAHAHAHAHAHAH LATER
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#-----------------------------------------------------------------------------------------------
#menus shterff(stuff)
#-----------------------------------------------------------------------------------------------



class nidos():
    # navagatble information dispensing object system
    
    def __init__(self, x,y, width, height, cols, rows, x_gap, y_gap, init_func, init_arg, subject_r,
                    background = io.nidos_background, place = 0, output = 0):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background
        
        self.output = output
        
        self.selected = (0,0)
        
        self.cols = cols
        self.rows = rows
        
        self.subject_width = int((width - (cols+1)*x_gap)/cols)
        self.subject_height = int((height- (rows+1)*y_gap )/rows)
        self.subject_r = subject_r
        
        ###########
        #place
        #io.rect(self.x,self.y,width, height, background)
                
        #################
        #buttoning
        self.ido_list = []
        
    
        #print(self.ido_list)
        for x in range(self.cols): 
            self.ido_list.append([])
            for y in range(self.rows):
                
                self.ido_list[x].append(init_func(*init_arg))
                
                pointer = self.of(x,y)
                
                pointer.reshape(self.subject_width, self.subject_height, self.subject_r, place = 0 )
                
                pointer.relocate( (self.x+((x+1)*x_gap) + (x*self.subject_width)) ,
                            (self.y+((y+1)*y_gap) + (y*self.subject_height)), place = 0  )
                            
                #pointer.recolor(clear_color = background, place = 0)
                
                pointer.implement()
                #pointer.place()
                
                del pointer
                if output:
                    print('claculated nidos: (',x,',',y )
                
        if place:
            self.place()
        
        self.select(*self.selected, place = 0)
            
    def of(self,x,y):
        return self.ido_list[x][y]
    
    def place(self):
        
        io.rect(self.x,self.y,self.width, self.height, self.background)
        
        for x in range(self.cols): 
            for y in range(self.rows):
                self.of(x,y).activate(place = 1)
                #print(self.of(x,y).active)
    
    
    def unplace(self):
        for x in range(self.cols): 
            for y in range(self.rows):
                self.of(x,y).deactivate(place = 0)
    
    def select(self,x,y, place = 1):
        if self.selected != (x,y):
            self.of(*self.selected).deselect(place)
        self.of(x,y).select(place)
        self.selected = (x,y)

    def move(self, dir_x, dir_y):
        test_x = self.selected[0] 
        test_y = self.selected[1]
        
        for i in range(1+max(self.cols,self.rows)):
            test_x += dir_x
            test_y += dir_y
                    
           
            if test_x <= -1:
                test_x += self.cols
                        
            elif test_x >= self.cols:
                test_x -= self.cols 
                        
            elif test_y <= -1:
                test_y += self.rows 
                        
            elif test_y >= self.rows :
                test_y -= self.rows 
            
            if self.of(test_x, test_y).active:
                self.select(test_x,test_y)
                break
            #except IndexError:
                #return 'unable to move'
                #break
                
        try:
            return({(1,0):'right',(-1,0):'left',(0,1):'down',(0,-1):'up'}[(dir_x, dir_y)])
        except KeyError:
            return '???move command output not known???'
        del test_x,test_y,dir_x,dir_y
        
    def click(self, deactivate = 1):
        pointer = self.of(*self.selected)
        if (pointer.active == True) and ( pointer.selected == True):
            if deactivate:
                self.unplace()
            pointer.press_animation()
            pointer.purpose_list.chug(delete = False)
            return('clicked')
        else:
            return('unable to click,  reason: inactive or unselected')    
########################################################
# page
########################################################

def not_filled_page(ret_var):
    disp.fill(color(255,0,0))
    disp.text(0,0,'this button has no purpose yet, this is because it has not been set yet',color = 0,background = color(255,0,0))
    time.sleep(.25)
    try:
        ret_var.place()
    except AttributeError:
        pass

'''n = gui.nidos(0,0,disp.width,disp.height,1,5,5,5,gui.text_button,
            (10,10, 30, 25, 3,'', not_filled_page, () ), 0,place = 0, output = 0)'''

class page():
    def __init__(self, x,y,width, height, cols, rows, rad, gap,splitx_start = 0, splity_start = 0,
                splitx_end =  None, splity_end = None, background = io.background_color,
                clear_color = io.background_color):
        
        if splitx_end == None:
            splitx_end = width
            
        if splity_end == None:
            splity_end = height
        
        self.menu = nidos(x,y,splitx_end,splitx_end,cols,rows,gap,gap, text_button, 
                            (0,0, 8, 8, 3,'', not_filled_page, (self) ),  rad, place = 0, output = 0)
        
        self.menu.place()
        
    def place(self):
        print('page place activated')


    