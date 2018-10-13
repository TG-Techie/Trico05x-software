#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

''' this is a module that expands on the tg_modules' gui library and 
provides basic gui objects for displaying data'''

from TG_modules.gui_components.gui import io, nidos, button, ego # empty gui object

from tg_modules.gui_components.gui_value_displays import grid_display

####TODOS:
# make switch_x_y in grid_display
# make a thermal verison of grid
# make flip_Y work

class gui_sensor(ego):
    def __init__(self, x,y,width, height, get_data_func, get_data_tup, 
                background = io.standard_color, 
                clear_color = io.background_color, place = 1):
        pass # remove this line
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height
        
        #self.get_data_func = get_data_func
        #self.get_data_tup = get_data_tup
        
        #if place: # the variable place (command tense) like 'place that object down'
            #self.place()
        
    
    def place(self):
        pass # remove this line
        #put down the basics/ unchanging items of your gui object
        #self.refresh()
    
    def refresh(self):
        pass # remove this line
        #data = self.get_data_func(*self.get_data_tup)
        #put data on screen
    
    def clear(self):
        pass # remove this line
        # deactivate all button and nidoss
        #place a clear_color rect ovwer the whole thing
        
        


def _c2f(temp):
    return 1.8*temp + 32
    
def _f2c(temp):
    return (temp-32)/1.8    
    
class thermal_display(grid_display):
    """UNITS: use this for units_in and units_out: None=0, Celsius=1, faren=2, kelvin=3 
    None will not chage the numbers at all ** defaults to celsius"""
    def __init__(self, x,y,width, height, get_data_func, get_data_tup, color_mask = 4, border = 3,
                background = io.standard_color, clear_color = io.background_color, ave_val = 25, text_active = 1,
                text_size = 1, units_in = 1, units_out = 1, 
                flip_x = 0, flip_y = 0, switch_x_y = 0, place = 1):
        
        self.units_in = units_in
        self.units_out = units_out
        
        super().__init__(x,y,width, height, get_data_func, get_data_tup, color_mask, border,
                background, clear_color, ave_val, text_active,
                text_size, flip_x, flip_y, switch_x_y, place)
    
    def place_text(self, val_tup):
        tmin = val_tup[0]
        tmax = val_tup[1]
        
        if self.units_in != self.units_out:
            #convert to c
            if self.units_in == 2:
                tmin = _f2c(tmin)
                tmax = _f2c(tmax)
            elif self.units_in == 3:
                tmin = tmin - 273
                tmax = tmax - 273
            #convert to output desired from c
            if self.units_out == 2:
                tmin = _c2f(tmin)
                tmax = _c2f(tmax)
            elif self.units_out == 3:
                tmin = tmin + 273
                tmax = tmax + 273
        
        append_str = ('','c','F', 'K')[self.units_out]
        if self.units_out:
            append_str += '__degreesign__'
        #print(((str(tmin) + append_str ), (str(tmax) + append_str)))
        super().place_text(   ((str(tmin) + append_str ), (str(tmax) + append_str))    )
