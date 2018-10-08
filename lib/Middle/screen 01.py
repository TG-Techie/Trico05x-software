from middle import sensor
from staging import sen_brd
from tg_modules import screen_io as io
import math


class thermal_graph():
    
    def __init__(self, x,y, width, border, border_color = io.standard_color
                    ,clear_color = io.color(0,0,0), 
                    update_func = sensor.thermal_camera.get_data,
                    update_arg = ()  ):
                    
        
        self.x = x
        self.y = y
        
        self.border = border
        self.width = width
        
        self.border_color = border_color
        self.clear_color = clear_color
        
        self.update_func = update_func
        self.update_arg = update_arg
        
        self.max_temp = 0
        self.min_temp = 81
        
        self.place()
        
    def data(self):
        
        data = self.update_func(*self.update_arg)#sen_brd.amg.pixels
        
        self.data_width = len(data[0])
        self.data_height = len(data)
        
        self.max_temp = 28
        #self.min_temp = 0
        
        for row in data:
            for val in row:
                self.max_temp = max(val,self.max_temp)
                self.min_temp = min(val, self.min_temp)
        #print(self.max_temp, self.min_temp)
        
        return data
        
    def place(self):
        
        data = self.data()
        #print(data)
        
        
        io.rect(self.x,self.y,
                (self.border*2)+self.data_width*self.width,
                (self.border*2)+self.data_height*self.width,
                self.border_color)
                
        self.update()
    
    def update(self):
        
        data = self.data()
        
        color_range = 25.4/((self.max_temp-self.min_temp)**3)
        
        for x in range(self.data_width):
            for y in range(self.data_height):
                
                temp = data[x][y]
                #print(temp)
                try:
                    col255 = int((10*(round(((temp-self.min_temp)**3)*(color_range)))))
                except ZeroDivisionError:
                    col255 = 255
                
                io.rect(self.x + self.border + self.width*(self.data_width-x-1) ,
                        self.y + self.border + self.width*y,
                        self.width,self.width,
                        #io.color(col255,col255,col255))
                        io.color( col255 ,255 - col255,255 - col255))