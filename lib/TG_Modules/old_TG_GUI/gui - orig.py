from tg_modules.tasking import task, thread_list
from TG_Modules.TG_GUI import io

class ject():

    def __init__(self,x,y, place_func, place_arg):
        self.x = x
        self.y = y
        
        
        self.place_list = thread_list(1)
        self.place_list.add_task(place_func, place_arg)
        
        del x,y, place_func, place_arg
        
    def place(self):
        self.place_list.chug(delete = False)

class _button(ject):
    
    def __init__ (self,x,y,place_func, place_arg,sel_func,sel_arg, task_funk, task_arg):
        super().__init__(x,y,place_func, place_arg)

        self.task = task(task_funk, task_arg)
        
        self.sel_list = thread_list(length = 1)
        self.sel_list.add_task(sel_func,sel_arg)

        self.selected = False
        
        del x,y, place_func, place_arg, sel_func, sel_arg, task_funk, task_arg

    def select(self):
        self.selected = True
        self.sel_list.chug(delete = False)

    def deselect(self):
        self.selected = False
        self.place()

    def press(self):
        if self.selected:
            self.deselect()
            self.select()
            self.task.perform()

class button(_button):
    
    def __init__(self,x,y,width,height,r,task_funk, task_arg, 
                 color = io.color(3,85,107),
                 color_sel = io.color(128,250,255)):
        
        super().__init__(x,y,io.round_rect,
                         (x,y,width,height,r,color),
                         io.round_rect,
                         (x,y,width,height,r,color_sel),
                         task_funk, task_arg)

        self.width  = width
        self.height = height
        
        del  x,y,width,height,r, task_funk, task_arg, color, color_sel

class text_button(button):

    def __init__(self,x,y,width,height,r,task_funk, task_arg, text, size =1,
                 color = io.color(3,85,107),
                 color_sel = io.color(128,250,255),
                 color_text = io.color(0,0,0)):
        
        super().__init__(x,y,width,height,r,task_funk, task_arg, color, color_sel)

        text_dim = io.text_dimension(self.x,self.y,text,size)
        print(text_dim)

        self.place_list.add_task(io.text, (self.x + int((self.width-text_dim[0])/2),
                                         self.y + int((self.height-text_dim[1])/2),
                                         text, color_text,
                                         color, size))
    
        self.sel_list.add_task(io.text, (self.x + int((self.width-text_dim[0])/2),
                                         self.y + int((self.height-text_dim[1])/2),
                                         text, color_text,
                                         color_sel, size))

        
        
'''class button(_button):
    
    def __init__(self,x,y,width,height,r,text,
                 color_text = 0,
                 color = io.color(3,85,107),
                 color_sel = io.color(128,250,255)):
        super().__init__(x,y,io.round_rect,
                         (x,y,width,height,r,color),
                         io.round_rect,
                         (x,y,width,height,r,color_sel))
        
        self.sel_list.add_task(io.text,())
       
        
        del  x,y,width,height,r,text,color_text, color, color_sel'''
