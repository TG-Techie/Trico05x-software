#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from tg_modules.gui_modules.gui_base import selectable,navigable,gui_obj, io
import time

#button assignments:
# up, down, left, right, enter

try:
    from tg_modules.tg_tools import get_direction
except:
    def get_direction(val):
        if val < 0:
            return -1
        elif val == 0:
            return 0
        else:
            return 1

def _button_error(but):
    io.if_rect(but.x,but.y,but.width,but.height,but.radius,io.red)
    io.text(but.x+but.radius,but.y+but.radius,'Err', background = io.red)
    time.sleep(1)
    but.place()

class button(selectable):
    def __init__(self,x,y,width,height,radius = 0, text = ' ', purpose_func = None, purpose_tup = (),
                    x_offset = 0, y_offset = 0, place = 1,
                    color = io.button_color_norm,
                    color_clear = io.button_clear_color,
                    color_sel = io.button_color_sel,
                    text_color = io.text_color_norm,
                    text_color_sel = io.text_color_sel):
        self._set_id() # YOU MUST DO THIS
        
        #physical params
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self._text = text
        
        if purpose_func:
            self.purpose_func = purpose_func
            self.purpose_tup = purpose_tup
        else:
            self.purpose_func = _button_error
            self.purpose_tup = (self,)
        
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        #color params
        self.color = color
        self.color_clear = color_clear
        self.color_sel = color_sel
        self.text_color = text_color
        self.text_color_sel = text_color_sel
        
        self.selected = 0
        self.active = 0
        
        if place:
            self.place()
    
    def place(self,selected = None, active = None):
        
        if active == None:
            self.active = 1
            active = 1# turn on button
        
        if active:
            if selected == None:
                selected = self.selected
                
            if selected:
                cur_color = self.color_sel
                cur_text = self.text_color_sel
            else:
                cur_color = self.color
                cur_text = self.text_color
            
            #place base shape for button
            io.if_rect(self.x,self.y,self.width,self.height,self.radius,cur_color)
            
            if self.text != ' ':
                #find/calc text dimension and location
                text_dim = io.text_dimensions(self.x,self.y,self.text)
                text_x = int(self.x + self.x_offset+(self.width  -text_dim[0])/2) - 1
                text_y = int(self.y + self.y_offset+(self.height -text_dim[1])/2) - 1 
                
                #place text
                io.text(text_x,text_y,self.text,cur_text,cur_color)
    
    def clear(self):
        self.active = 0
        io.if_rect(self.x,self.y,self.width,self.height,self.radius,self.color_clear)
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self,new_text):
        #ensure length isn't zero
        if not len(new_text):
            new_text = ' '
        
        self._text = new_text
        
        if self.active:
            self.place()

class nidos(navigable):
    "move_mode variable input: (1,1) = move in x & y, (1,0) = move in x, (0,1) = move in y"
    
    def __init__(self, x,y,width,height,cols,rows,radius = 0, move_mode = (1,1), superior = navigable(0,0,0,0,place = 0),
                    x_gap = 3, y_gap = 3,
                    place = 1, select = 1,
                    color_clear = io.background_color,
                    background = io.background_color,
                     button_color = io.button_color_norm,
                     button_color_sel = io.button_color_sel,
                     button_text_color = io.text_color_norm,
                     button_text_color_sel = io.text_color_sel):
        self._set_id() # YOU MUST DO THIS
        
        #physical params
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        #self.radius = radius
        #self.x_gap = x_gap
        #self.y_gap = y_gap
        
        self.background = background
        self.color_clear = color_clear
        
        if move_mode == (0,0):
            move_mode = (1,1)
            
        self.move_mode = move_mode
        
        self.selected = (0,0)
        self.active = 0
        
        #window that contains the panel that contains this nidos
        #if superior:
        self.superior = superior
        #else:
            #self.superior = navigable(0,0,0,0)
        
        #list containing buttons
        self.contents = []
        
        but_width = int(((width - x_gap) / cols) - x_gap)
        but_height =int(((height - y_gap) / rows) - y_gap)
        
        for cur_y in range(self.rows):
            for cur_x in range(self.cols):
                self.contents.append(button( x+(cur_x*x_gap + x_gap)+(cur_x*but_width),# x coord
                                            y+(cur_y*y_gap + y_gap)+(cur_y*but_height),# y coord
                                            but_width, but_height, radius, place = 0, 
                                            color_clear = color_clear,
                                            color = button_color,
                                            color_sel = button_color_sel,
                                            text_color = button_text_color,
                                            text_color_sel = button_text_color_sel))
        # this is lremoved to allow the user to cahnge the button types
        #self.contents = tuple( self.contents) # space saving
        
        if place:
            self.place()
        
        #print(place)
        if select:
            self.switch(0,0, force = place)
            self.of(*self.selected).active = place
            self.of(*self.selected).select()
                
    
    def of(self,x,y):
        return self.contents[(self.cols*y)+x]
    
    def switch(self,x,y, force = 0):
        if ((x,y) != self.selected) or (force):
            self.of(*self.selected).deselect()
            self.selected = (x,y)
            self.of(*self.selected).select()
    
    def place(self):
        self.active = 1
        io.rect(self.x,self.y,self.width,self.height,self.background)
        for but in self.contents:
            but.place()
    
    def clear(self):
        self.active = 0
        for but in self.contents:
            but.clear()
        io.rect(self.x,self.y,self.width,self.height,self.background)
    
    def move(self,dirx,diry = 0):
        
        if self.move_mode == (0,1): diry = (dirx or diry)
        
        #starting locations
        nextx = self.selected[0]
        nexty = self.selected[1] 
        
        #if that directin is acitvated in move mode add 
        #the direction of the inputs to the next coords
        if self.move_mode[0]:
            nextx += get_direction(dirx)
        if self.move_mode[1]:
            nexty += get_direction(diry)
        
        chgx = 0
        chgy = 0
        
        #check if on my movement method superior needs to movw pages
        if (self.move_mode[0]) and not (0 <= nextx < self.cols):
            chgy += get_direction(nextx)
        if (self.move_mode[1]) and not (0 <= nexty < self.rows):
            chgx += get_direction(nexty)
        
        #print(chgx,chgy)
        
        try:
            self.superior.move(get_direction(sup_dir) * bool(abs(sup_dir) == (self.selected[0] + self.selected[1] )))
            #self.superior.move(chgx,chgy)
        except:
            pass 
        
        self.switch((nextx+chgx) % self.cols, (nexty+chgy) % self.rows) 
        
        del nextx, nexty, chgx, chgy
    
    def press(self, animate = 1):
        if self.active:
            pointer = self.of(*self.selected)
            if animate:
                pointer.place( selected = True, active = pointer.active)
                time.sleep(.075)
                pointer.place( selected = False, active = pointer.active)
                time.sleep(.075)
                pointer.place( selected = True, active = pointer.active)
            pointer.press()

class panel(gui_obj):
        
    def __init__(self,x,y,width,height, place = 1, overwite_move = 1, color_clear = io.background_color,
                background = io.background_color):
        self._set_id() # YOU MUST DO THIS
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.color_clear = color_clear
        self.background = background
        
        self.active = 0
        self.overwite_move = overwite_move
        
        self.contents = []
        self._nav = navigable(0,0,0,0,place = 0)
        self.cmd_dict = {}#{'<' : (self.nav.move , (-1,0)) , '>' : (self.nav.move , (1,0)) ,'^' : (self.nav.move ,(-1,0)) , 'V' : (self.nav.move , (0,1)) , 
                            #'E' : (self.nav.press ,())}
        
        if place:
            self.place()
        
    def place(self):
        self.active = 1
        io.rect(self.x,self.y,self.width,self.height,self.background)
        for pointer in self.contents:
            pointer.place()
    
    def clear(self):
        self.active = 0
        for pointer in self.contents:
            pointer.clear()
        io.rect(self.x,self.y,self.width,self.height,self.color_clear)
    
    def add(self, **kwargs):
        for key,value in kwargs.items():
            if hasattr(value, 'is_gui_obj') and hasattr(value,'_gui_id'):
                #set into this panel isntance
                setattr(self, key, value)
                #add the new value the contents list
                pointer = getattr(self, key)
                self.contents.append( pointer )
                
                #print('is navigable: ',pointer.is_navigable)
                if pointer.is_navigable:
                    self.nav = pointer
                
    
    def refresh(self):
        if self.active:
            for item in self.contents:
                try:
                    item.refresh()
                except:
                    pass
    
    @property
    def nav(self):
        return self._nav
        
    @nav.setter
    def nav(self,val, overwite_move = None):
        if val in self.contents:
            self._nav = val
            if overwite_move == None:
                overwite_move = self.overwite_move
            if overwite_move:
                self.cmd_dict['<'] = (self.nav.move , (-1,0))
                self.cmd_dict['>'] = (self.nav.move , (1,0))
                self.cmd_dict['^'] = (self.nav.move ,(0,-1))
                self.cmd_dict['V'] = (self.nav.move , (0,1))
                self.cmd_dict['E'] = (self.nav.press ,())
        else:
            raise TypeError("TG: tried to set panel's nav to object not already in panel")
    
    def command(self,*args):
        if self.active:
            for cur_val in args:
                try:
                    tup_pointer = self.cmd_dict[cur_val]
                    tup_pointer[0](*tup_pointer[1])
                except: raise KeyError("TG: cmd key given to panel has no assigned function")
                
    #def add_cmd():
    
class window(gui_obj):
    
    
    def __init__(self,x,y,width,height,color_clear = io.background_color, background = io.background_color):
        self._set_id()
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.color_clear = color_clear
        self.background = background
        
        self.active = 0
        
        self.contents = []
        
        self.add_panel()
    
    def place(self):
        self.active = 1
        
        io.rect( self.x, self.y, self.width, self.height, self.background)
        
        #for loop here
        
    def clear(self):
        self.active = 0
        
        # for loop here
        
        io.rect( self.x, self.y, self.width, self.height, self.color_clear)
        
    def add_panel(self, *args):
        
        #decide what to iternat thorugh, if no args do once with no name
        if not len(args):
            iterant = range(1)
        elif type(args[0]) == int:
            iterant = range(args[0])
        else:
            iterant = args
            
        for val in iterant:
            #find internal panel number
            panel_num = len(self.contents)
            #name the std name
            panel_name = '_panel'+str(panel_num)
            
            #add std named panel to self
            setattr(self,panel_name, panel(self.x,self.y,self.width,self.height, color_clear = self.color_clear,
                background = self.background))
                
            #add to contents
            self.contents.append(getattr(self,panel_name))
                
            # if val is str set and panel name
            
            
    def move(self,direction):
        pass
        
        
        