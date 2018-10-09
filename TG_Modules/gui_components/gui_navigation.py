from tg_modules.gui_components.gui_base import selectable,navigable, io


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
    
    def place(self,selected = None):
        self.active = 1 # turn on button
        
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
    
    def __init__(self, x,y,width,height,cols,rows,radius = 0, move_mode = (1,1), superior = None,
                    x_gap = 3, y_gap = 3,
                    place = 1, select = 1,
                    color_clear = io.background_color,
                    background = io.background_color,
                     button_color = io.button_color_norm,
                     button_color_sel = io.button_color_sel,
                     button_text_color = io.text_color_norm,
                     button_text_color_sel = io.text_color_sel):
        
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
        
        if move_mode != (0,0):
            self.move_mode = move_mode
        else:
            move_mode = (1,1)
        
        self.selected = (0,0)
        
        #window that contains the panel that contains this nidos
        if superior:
            self.superior = superior
        else:
            self.superior = navigable(0,0)
        
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
        self.contents = tuple( self.contents)
        
        if place:
            self.place()
        if select:
            self.switch(0,0)
    
    def of(self,x,y):
        return self.contents[(self.cols*y)+x]
    
    def switch(self,x,y):
        self.of(*self.selected).deselect()
        self.selected = (x,y)
        self.of(*self.selected).select()
    
    def place(self):
        io.rect(self.x,self.y,self.width,self.height,self.background)
        for but in self.contents:
            but.place()
    
    def clear(self):
        for but in self.contents:
            but.clear()
        io.rect(self.x,self.y,self.width,self.height,self.background)
    
    def move(self,dir1,dir2 = 0):
        next_x = self.selected[0] + bool(self.move_mode[0])
        next_y = self.selected[1] + bool(self.move_mode[1])
        super().move(0,0)
    
    def press(self):
        self.of(*self.selected).press()
        