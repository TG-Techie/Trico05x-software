from middle import sensor
from tg_modules import screen_io as io

class thermal_graph():
    
    def __init__(self, x,y, width, border, border_color = io.standard_color
                    ,clear_color = io.background_color,
                    background = io.background_color,
                    update_func = sensor.thermal_cam_data,
                    update_arg = (), min_max = 28  ):
        self.x = x
        self.y = y
        
        self.border = border
        self.width = width
        
        self.border_color = border_color
        self.clear_color = clear_color
        self.background = background
        
        self.update_func = update_func
        self.update_arg = update_arg
        
        self.max_temp = 0
        self.min_temp = 0
        self.min_max = min_max
        
        data = self.data()
        
        self.data_width = len(data[0])
        self.data_height = len(data)
        for row in data:
            for val in row:
                self.max_temp = max(val,self.max_temp)
                self.min_temp = min(val, self.min_temp)
        
        self.place()
        
    def data(self):
        data = self.update_func(*self.update_arg)
        self.max_temp = self.min_max        
        return data
        
    def place(self):
        self.area_width = (self.border*2)+self.data_width*self.width
        self.area_height = (self.border*2)+self.data_height*self.width
        
        io.rect(self.x,self.y,
                self.area_width,
                self.area_height,
                self.border_color)
        
        io.rect(self.x,
                self.area_height + self.y,
                self.area_width,
                20,
                self.background)
                
        io.text(self.x, self.area_height + self.y, 'max:')
        io.text(self.x, self.area_height + self.y + 10, 'min:')
        
                
        self.update()
    
    def clear(self):
        pass
    
    def update(self):
        data = self.data()
        
        color_range = 25.4/((self.max_temp-self.min_temp)**6)
        
        next_max = -1
        next_min = 81
        
        for y in range(self.data_height):
            for x in range(self.data_width):
                
                temp = data[x][y]
                
                next_max = max(temp,next_max)
                next_min = min(temp,next_min)
                
                col255 = int((10*(round(((temp-self.min_temp)**6)*(color_range)))))
                
                io.rect(self.x + self.border + self.width*x ,
                        self.y + self.border + self.width*y,
                        self.width,self.width,
                        io.color(255,255-col255,255-col255))
        
        io.text(self.x + 25, self.area_height + self.y,str(next_max) + 'c__degreesign__ ')
        
        io.text(self.x + 25, self.area_height + self.y + 10,str(next_min) + 'c__degreesign__ ')
        
        self.max_temp = next_max + 1
        self.min_temp = next_min - 1