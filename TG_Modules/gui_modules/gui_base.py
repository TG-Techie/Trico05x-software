from TG_Modules import screen_io as io

class gui_obj():
    is_gui_obj = True
    
    def __init__(self,x,y,clear_color = io.background_color):
        #save them to class instance 
        pass
    
    #put the item on the screen
    def place(self):
        raise NotImplementedError('TG: place method not implemented for:'+str(type(self)))
    
    #cover the item with the "color_clear"
    def clear(self):
        raise NotImplementedError('TG: clear method not implemented for:'+str(type(self)))
    
class valued(gui_obj):
    has_value = True
    is_selectable = False
    is_navigable = False
    is_refreshable = False
    
    def __init__(self,x,y,value,clear_color = io.background_color):
        self._value = value
        #save rest to the class instance as the same name
        pass
    
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self,new_val):
        if new_val != self._value:
            #self.clear() #SHOULD HAVE THIS??
            self._value = new_val
            self.place()
        

class selectable(gui_obj):
    has_value =  False
    is_selectable = True
    is_navigable = False
    is_refreshable = False
    
    def __init__(self,x,y,purpose_func = None,purpose_tup = (),clear_color = io.background_color):
        
        if purpose_func: # boolean logic checker
            self.purpose_func = purpose_func
            self.purpose_tup = purpose_tup
        else:
            self.purpose_func = 'you_put_function_here' 
            #!!!!!!#put default func ^^^^^^^
            self.purpose_tup = (self,) 
        
        #save rest to the class instance as the same name
        
        #selectable states
        self.selected = 0
        self.active = 1
        
    def set_purpose(self, func, tup):
        self.purpose_func = func
        self.purpose_tup = tup
    
    def place(self):
        self.active = 1
        #check selected state and and place accordingly
        raise NotImplementedError('TG: place method not implemented for:'+str(type(self)))

        
    def clear(self):
        self.active = 0
        #cover with self.color_clear
        raise NotImplementedError('TG: clear method not implemented for:'+str(type(self)))
    
    def select(self, place = 1):
        if place:
            self.clear()
        self.selected = 1
        if place:
            self.place()
    
    def deselect(self, place = 1):
        if place:
            self.clear()
        self.selected = 0
        if place:
            self.place()
    
    def press(self):
        if self.active and self.selected:
            self.purpose_func(*self.purpose_tup)
    

class navigable(gui_obj):
    has_value = False
    is_selectable = False
    is_navigable = True
    is_refreshable = False
    
    def move(self, dir_1, dir_2 = None):
        #take the dirs and move acordingly, not not all systemns have up and down
        raise NotImplementedError('TG: move method not implemented for:'+str(type(self)))
    
    def switch(self, coord_1, coord_2 = None):
        #instead of moving switch directly to the coords
        raise NotImplementedError('TG: switch method not implemented for:'+str(type(self)))
    

        