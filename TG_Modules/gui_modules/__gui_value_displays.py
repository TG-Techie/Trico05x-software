#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18
from tg_modules.gui_components.gui import ego, io

class value_bar(ego):
    def __init__(self, x,y, width, height, maximum = 100, color = io.white,
                background = io.black, value_color = io.white, border = 1, gap = 1, place = 1 ):
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        
        self.color = color
        self.background = background
        self.value_color = value_color
        
        self.border = border
        self.gap = gap
        
        self.max = int(maximum)
        
        self.prog_width = width - 2*(gap+border) # the widthof the progress bar, pre calculated
        self.prog_height = height- 2*(gap+border) # the precalcualted height of the bar
        self.val = 0
        
        if place:
            self.place()
        
    def place(self):
        io.rect(self.x, self.y, self.width, self.height, self.color)
        io.rect(self.x + self.border, self.y+ self.border, self.width - self.border*2 ,
                self.height - self.border*2, self.background)
        #self.update()
    
    # make a property where you can update the
    # value to chagne the progress
    @property
    def value(self):
        return self.val
    
    @value.setter
    def value(self, new):
        self.val = new
        self.update()
    
    # lookat value and place two rectangles to 
    def update(self):
        #print('updated called')
        #print(self.val, self.max)
        prog_length = int((self.val/self.max)*self.prog_width ) #, self.max)
        #print(prog_length)
        if prog_length:
            io.rect(self.x + self.gap + self.border , self. y+ self.gap + self.border,
                    prog_length  , self.prog_height, self.value_color)
        
        if self.prog_width - prog_length:
            io.rect(self.x +prog_length + self.gap + self.border, 
                self.y  + self.gap + self.border,
                self.prog_width - prog_length  , self.prog_height, self.background) 

class grid_display():#gui_sensor):
    ''' Thermal display grid:   this is used for displaying information 
in a 2d grid. it scales the lowes anf highest numbers as the range of colors.

**** BALANCE THE BORDER AND WIDTH TO THE NUMBER OF PIXELS ******

USE:
INPUT: the input should be  a list full of lists (or tuples). then set the flip_x
    or flip_y to 0 or 1 accordingly.  ** these default to 0
    
COLOR: the input for the highlight color is three bits of rgb. so just red
as highlight would be 0b100, but for r and b the color input would be 0b101
'''
    
    def __init__(self, x,y,width, height, get_data_func, get_data_tup, color_mask = 4, border = 3,
                background = io.standard_color, clear_color = io.background_color, ave_val = 25, text_active = 1,
                text_size = 1, flip_x = 0, flip_y = 0, switch_x_y = 0, place = 1):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        #border around the data w/ its color
        self.border = border
        self.background = background
        
        #color used to earase the object
        self.clear_color = clear_color
        
        #how to get data
        self.get_data_func = get_data_func
        self.get_data_tup = get_data_tup
        
        #save how to change data from sensors
        self.flip_x = flip_x
        self.flip_Y = flip_y
        self.switch_x_y = switch_x_y
        
        #bit based color customization
        self.color_mask = color_mask
        
        #vals for the reset min / max values durring every refresh
        self.std_min_val = int(500*ave_val/25)
        self.std_max_val = int(-500*ave_val/25)
        
        text_dim  = io.text_dimensions(self.x, self.y + self.height, ''' 
 ''',  size = text_size)
        self.text_size = text_size
        self.text_active = text_active
        self.text_char_height = int(text_dim[1] / 2) + text_size
        self.text_char_width = text_dim[0]
        
        if place:
            self.place()
        
        
        
    def place(self):
        io.rect(self.x , self.y, self.width, self.height, self.background)
        #double refresh to remove max / min errors of init color changing
        if self.text_active:
            io.rect(self.x, self.y + self.height, self.width, self.text_char_height*2 + 1, self.clear_color)
        self.refresh()
        self.refresh()
        
        
    def refresh(self):
        data = self.get_data_func(*self.get_data_tup)
        
        #creadjust dat to looking correct
        if self.flip_x:
            data = data[::-1]
            
        if self.flip_Y:
            data = list(data)
            for i in range(len(data)):
                data[i] = data[i][::-1]
                
        if self.switch_x_y:
            next_data = []
            for smoop in data:
                pass
        
        #calcualte pixel dimensiosn
        pix_width = int((self.width - self.border*2)/ ((len(data))  ) )
        pix_height = int((self.height - self.border*2)/ ((len(data[0]))) ) 
        
        # bring saved previous min/max vals and calculate the range
        min_val = self.std_min_val
        max_val = self.std_max_val
        
        for col in data:
            col.sort()
            min_val = min(  min_val, col[0])
            max_val = max( max_val , col[-1])
        
        color_range = .5 + max_val-min_val
        
        # find (0,0) of data (top right)
        x_start = self.x + self.border
        y_start = self.y + self.border
        
        cur_x = 0 # col number, indexed
        for col in data:
            #print('----------')
            cur_y = 0 # row number, indexed
            for val in col:
                
                color = 10* int((25*(  ((val-min_val)**6)/((color_range)**6)   )))
                
                io.rect(x_start +  cur_x , y_start + cur_y,
                        pix_width , pix_height,  
                        io.color(int(255 - color*(not(self.color_mask&4)/4) ),
                        int(255 - color*(not(self.color_mask&2)/2) ),
                        int(255 - color*(not(self.color_mask&1)))    )        )
                    
                cur_y += pix_height
                
            cur_x += pix_width
        
        if self.text_active:
            self.place_text((min_val, max_val))

        return (min_val, max_val)
        
    def place_text(self, val_tup):
        
        out = """Min: """ + str(val_tup[0]) + '   '
        #clip length
        while len(out) -13 > self.width/self.text_char_width: # 13 is for the special charater
            out = out[0:-1]
        #place
        io.text(self.x, self.y + self.height, out, size = self.text_size)
        
        out = '''Max: ''' + str(val_tup[1]) + '   '
        #clip length
        while len(out) -13 > self.width/self.text_char_width: #13 if for the special character
            out = out[0:-1]
        #place
        io.text(self.x, self.y + self.height + self.text_char_height, out, size = self.text_size)
        
    def clear(self):
        io.rect(self.x , self.y, self.width, self.height, self.clear_color)
        if self.text_active:
            io.rect(self.x, self.y + self.height, self.width, self.text_char_height*2 + 1, self.clear_color)
        
        
