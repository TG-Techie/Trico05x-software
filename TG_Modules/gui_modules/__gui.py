from tg_modules.tasking import task, thread_list
from TG_Modules import screen_io as io
import time

### blank gui object####
#### empty gui object
class ego():
    '''Empty GUI Object:
This is the base class with specified formatting for an all purpose gui object. 
this can also be used as a an identifier to see if an object is a gui one'''
    _type_id = 'ego'
    
    def __init__(self,x = 0,y = 0 ,width = 0,height = 0,**kwargs):
        #self.output = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        for key,val in kwargs.items():
            setattr(self,key,val)
    
    def place(self):
        pass
             
    def clear(self):
        pass
        
    def refresh(self):
        pass


### blank gui object####
#### empty gui object
class igo(ego):
    
    _type_id = 'igo'
    
    def move(self):
        pass
    
    def switch(self):
        pass
    
            
#make abutton class with methods to set colors, location, shape, size and other feteures outside of init
##############################
#button
##################################
class button(ego):
    def __init__(self,x,y, width, height, r , text = '' , purpose_func = None, purpose_tup = (),
                    x_offset = 0, y_offset = 0, implement = 1,
                    color = io.button_color_norm,
                    clear_color = io.button_clear_color,
                    color_sel = io.button_color_sel,
                    text_color = io.text_color_norm,
                    text_color_sel = io.text_color_sel):            
        
        #initial posiiton
        self.selected = 0
        self.active = 1
            
        #always set color beasue the naming is horrible 
        #also becasue how often does every singel  button have a different color
        self.color = io.button_color_norm
        self.clear_color = io.button_clear_color
        self.color_sel = io.button_color_sel
        self.text_color = io.text_color_norm
        self.text_color_sel = io.text_color_sel
        
        #if told to (ie save toime by not implementing )

            #position
        self.x = x
        self.y = y
        #shape
        self.width = width
        self.height = height
        self.r = r
        #content
        self.text = text
        # text offsets
        self.x_offset = x_offset 
        self.y_offset = y_offset
        
        if purpose_tasks == None:
            purpose_tasks = (  (print,('button: ', self, ' pressed')),  )
            
        self.set_purpose(purpose_func,purpose_tup)
            
        
    def change_text(self, text,  x_offset = 0, y_offset = 0, place = 0):
        if len(text) == 0:
            self.text = ' '
        else:
            self.text = text
            
        self.x_offset = x_offset
        self.y_offset = y_offset
        if place:
            self.place()
            
    def relocate(self, x,y):
        self.clear()
        self.x = x
        self.y = y
        
    def set_shape(self,width, height, r):
        self.clear()
        self.width = width
        self.height = height
        self.r = r
    
    def recolor(self,color = io.button_color_norm,
                    clear_color = io.button_clear_color,
                    color_sel = io.button_color_sel,
                    text_color = io.text_color_norm,
                    text_color_sel = io.text_color_sel):
                    
        self.color = io.color_norm
        self.clear_color = io.clear_color
        self.color_sel = io.color_sel
        self.text_color = io.text_color
        self.text_color_sel = io.text_color_sel
    
    def set_purpose(self, func, tup):
        #make thread
        self.purpose_func = func
        self.purpose_tup = tup
    
    def select(self, place = 1):
        self.selected = 1
        if place:
            self.place()
    
    def deselect(self, place = 1):
        self.selected = 0
        if place:
            self.place()
    
    def activate(self,place = 1):
        self.active = 1
        if place:
            self.place()
    
    def deactivate(self, clear = 1):
        self.active = 0
        if clear:
            self.clear()
    
    def clear(self):
        try:
            io.if_rect(self.x,self.y,self.width, self.height, self.r, self.clear_color)
        except AttributeError:
            pass
        
    def place(self, active = None, selected = None):
        if active == None:
            active = self.active
        if selected == None:
            selected = self.selected
        if active:
            if selected:
                cur_color = self.color_sel
                cur_text = self.text_color_sel
            else:
                cur_color = self.color
                cur_text = self.text_color
            
            text_dim = io.text_dimensions(self.x,self.y,self.text)
            text_x = int(self.x + self.x_offset+(self.width  -text_dim[0])/2)
            text_y = int(self.y + self.y_offset+(self.height -text_dim[1])/2)
            
            io.if_rect(self.x,self.y,self.width,self.height,self.r,cur_color)
            io.text(text_x,text_y,self.text,cur_text,cur_color)
    
    #def press_animation():
    
    
            
    def press(self, delay = 0):
        if self.active and self.selected:
            self.place(selected = 0)
            time.sleep(delay)
            self.place(selected = 1)
            time.sleep(delay)
            #self.purpose_list.chug(delete = 0)
            #print(self.purpose_list)
            self.purpose_func(*(self.purpose_tup))
    
    def switch(self, x,y):
        self.select(x,y)

        
        
    
##########################################
#NIDOS - navagatable information dispensing object system
##########################################

def nidos_error(init_menu,x, y, width, height, duration = 2.5,
                message = '''the ido pressed has no assigned purpose returning to nidos...'''):
    io.rect(x,y,width,height, io.red)
    io.text(x,y,message,io.black, io.red)
    time.sleep(duration)
    try:
        init_menu.place()
    except:
        pass

class nidos(igo):
    
    def __init__(self,x,y,width,height, rows, cols, radius = 0, move_lock = 0, move_mode = 0, superior = None,
                    x_gap = 3, y_gap = 3, background = io.nidos_background, 
                    place = 0, output = 0, select = 0, ido_class = button):
        
        self.ido_list = []
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.rows = rows
        self.cols = cols
        
        self.x_gap = x_gap
        self.y_gap = y_gap
        self.background = background
        
        self.move_mode = move_mode
        self.move_lock = move_lock
        self.superior = superior
        
        self.selected = (0,0)
        
        #for later to save space
        #but_template = button(0,0,0,0,0,'',((io.fill,255),(io.fill,0)), implement =0 )
        
        ido_width = int(((width-x_gap) / cols) - x_gap)
        ido_height =int(((height - y_gap) / rows) - y_gap)
        cur_x = x+x_gap
        for make_x in range(cols):
            
            self.ido_list.append([])# make a sub list for x,y referencing
            
            cur_y = y+y_gap 
            for make_y in range(rows):
                #for later to save space
                #self.ido_list[make_x].append(but_template.copy())
                self.ido_list[make_x].append(ido_class(0,0,0,0,0,' ',nidos_error,(self,x,y,width,height), implement =0, clear_color = background ))
                pointer = self.ido_list[make_x][make_y]
                pointer.relocate(cur_x, cur_y)
                
                cur_y += y_gap+ido_height
                pointer.set_shape(ido_width,ido_height,radius)
                pointer.change_text(' ', place=0)
                pointer.set_purpose(nidos_error,(self,x,y,width,height))
                #print(pointer)
                #pointer.place()
            cur_x += x_gap+ido_width
        
            #self.place()
        if place:
            self.place()
        if select:
            self.select(*(self.selected), place = 0)
        
    def place(self):
        self.select(0,0, place = 0)
        io.rect(self.x, self.y, self.width, self.height, self.background)
        for col in self.ido_list:
            for cur_button in col:
                cur_button.activate(place = 1)
    
    def clear(self):
        io.rect(self.x, self.y, self.width, self.height, self.background)
        for col in self.ido_list:
            for cur_button in col:
                cur_button.deactivate(clear = 0)
    
    def of(self,x,y):
        return(self.ido_list[x][y])
    
    def select(self,x,y, place = 1): 
        self.of(*self.selected).deselect(place = place) # visually deselect old ido
        self.selected = (x,y)# select (data wise) the new ido
        self.of(x,y).select(place = place) # visually change new ido to selected
        self.current = self.of(x,y)
        
    def press(self, clear = 0, delay = .05):
        if clear :
            self.clear()
            self.of(*self.selected).activate(place = 0)
        self.of(*self.selected).press(delay)
        
    def _move(self,dir_x,dir_y):
        cur_pos = self.selected
        next_x = cur_pos[0] + dir_x
        try:
            next_y = cur_pos[1] + dir_y
        except TypeError:
            raise TypeError("TG:GuiError: move() if missing 1 of 2 positional arguments: 'y'")
            
        
        if next_x >= self.cols:
            if self.superior:
                self.superior.move(1)
            elif self.move_lock:
                next_x -= dir_x
            else:
                next_x = 0
                
        elif next_x < 0:
            if self.superior:
                self.superior.move(-1)
            elif self.move_lock:
                next_x =0
            else:
                next_x = self.cols - 1
        
        if next_y >= self.rows:
            if self.move_lock:
                next_y =- dir_y
            else:
                next_y = 0
        elif next_y < 0:
            if self.move_lock:
                next_y += dir_y
            else:
                next_y = self.rows - 1
        
        self.select(next_x, next_y)
    
    def _vmove(self,direction, fault_input = None):
        cur_pos = self.selected
        next_y = cur_pos[1] + direction
        next_x = cur_pos[0] 
        
        if next_y < 0:
            next_y = self.rows - 1
            next_x -= 1
        elif next_y >= self.rows:
            next_y = 0
            next_x+= 1
        
        if next_x >= self.cols:
            next_x = 0
        elif next_x < 0:
            next_x = self.cols -1
        
        self.select(next_x, next_y)

    def _hmove(self,direction, fault_input = None):
        cur_pos = self.selected
        next_y = cur_pos[1] 
        next_x = cur_pos[0] + direction
        
        if next_x < 0:
            next_x = self.cols - 1
            next_y -= 1
        elif next_x >= self.cols:
            next_x = 0
            next_y+= 1
        
        if next_y >= self.rows:
            next_y = 0
        elif next_y < 0:
            next_y = self.rows -1
        
        self.select(next_x, next_y)
        
    def move(self, dir_m, dir_y = None):
        [self._move, self._hmove, self._vmove][self.move_mode](dir_m,dir_y)
            
####################################################
#nidos and object container
class naoc(ego):
    def __init__(self, x, y, width, height, background = io.background_color,
                clear_color = io.background_color, place = 0, implement = 1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background
        self.clear_color = clear_color
        self.init_place = place
        #self.nav_place = nav_place
        
        self.contents = []
        self._focas = 0
        self.nav = None
        
        if self.init_place:
            self.place()
    
    def add(self, **kwargs):
        #print(self.__dict__)
        for key,value in kwargs.items():
            #make a new self.'name'
            setattr(self, key, value)
            #add the new value the contents list
            pointer = getattr(self, key)
            self.contents.append( pointer )
            try:
                if pointer._type_id == 'igo':
                    self.nav = pointer
            except:
                pass
            
        
    
    def place(self, nav = 1 ):
        #io.rect(self.x,self.y,self.width,self.height,self.background)
        io.rect(self.x,self.y,self.width,self.height,self.background)
        #if self.nav_place + nav:
            #for i in nav_list:
                #i.place()
        for i in self.contents:
            #print(i)
            try:
                i.place()
            except AttributeError:
                pass
    
    def refresh(self):
        for i in self.contents:
            try:
                i.refresh()
            except:
                pass
    
    def clear(self):
        io.rect(self.x,self.y,self.width,self.height,self.background)
        for i in self.contents:
            try:
                i.clear()
            except:
                pass
        io.rect(self.x,self.y,self.width,self.height,self.clear_color)
                
                
    '''@property
    def focas(self):
        return self.contents[self._focas]
    
    @focas.setter
    def focas(self, num):
        if num >= len(self.contents):
            num = 0
        elif num < 0:
            num = len(self.contents) -1
        self._focas = num'''
        
    
    def fill(self,color):
        io.rect(self.x, self.y, self.width, self.height, color)
        
        
#####################################################################
# swapable panelized object container
class spoc(igo):
    def __init__(self, x, y, width, height, number_panels = 1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.contents = []
        
        for i in range(number_panels):
            self.add_panel()
            
        self.current = self.contents[0]
        
    def add_panel(self):
        std_name = 'panel'+str(len(self.contents))
        setattr(self, std_name , naoc(self.x,self.y,self.width,self.height))
        self.contents.append(getattr(self, std_name))
        return getattr(self, std_name)
    
    def add_named_panel(self, name, index = 1):
        pointer = self.add_panel()
        setattr(self, name, pointer)
        if not index:
            self.deindex_panel(name)
        return pointer
    
    def _get_panel(self,target):
        try:
            return getattr(self, target)
        except:
            return(target)
    
    
    def deindex_panel(self, target):
        try:
            self.contents.pop(self.contents.index(self._get_panel(target))) 
        except:
            return 'unable to deindex: "'+str(target)+'"'
    
    def place(self):
        self.current.place()
    
    def clear(self):
        self.current.clear()
        
    
    def move(self,direction):
        self.current.clear()
        self.current = self.contents[(self.contents.index(self.current) + direction) % len(self.contents)]
        self.current.place()
    
    def switch(self, target, place = 1):
        if place:
            self.current.clear()
        self.current = self.contents[ self.contents.index(self._get_panel(target)) ]
        if place:
            self.current.place()
    
    
    