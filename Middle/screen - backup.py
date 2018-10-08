from gc import collect as clean_mem
from staging.disp import color
clean_mem()
from staging import sen_brd
clean_mem()

#construction spacing--------------------------------------------------
gap = 2

#----------------------------------------------------------------------
#colors:
text_color = color(255,255,255)
white = color(255,255,255)
black = 0
red = color(255,0,0)
green = color(0,255,0)
blue = color(0,0,255)

#---INIT INIT INIT INIT--------------------------------------

thread = None
disp = None
backlite = None

def init(thread_list, disp_in, backlite_in):
    thread = thread_list
    disp = disp_in
    backlite = backlite_in
    clean_mem()


#--------------------------------------------------------------------
###########: the thread_list to add stuff to

def text_task(x,y,str, priority = 3):
    thread.add_task(disp.text,(x,y,str),priority)
    del x,y,str
    clean_mem()

def rect_task(x,y,w,h,color,priority = 1):
    thread.add_task(disp.rect,(x,y, w ,h,color),priority)
    del x,y,w,h,color
    clean_mem()
  
#-----time stuff------------------------------------------------------------

def calc_time_string():
    time_string = ':'
    time_list = list(sensor.get_time()[3:5])
    clean_mem()
    #---section 1---------
    if time_list[0] >12: # format to NORMAL! human time
        time_list[0] += -12
    if time_list[0] < 10: # make sure is 2 digits 
        time_string = '0' + str(time_list[0]) + time_string
    else:
        time_string = str(time_list[0]) + time_string
    #---section 2------
    if time_list[1] < 10: # make sure is 2 digits 
        time_string +=  '0' + str(time_list[1]) 
    else:
        time_string += str(time_list[1])
    return time_string
    del time_string
    clean_mem()
        
    

global time_buf
time_buf = ''
def update_time():
    cur_time = calc_time_string()
    global time_buf
    if cur_time != time_buf:
        time_buf = cur_time
        rect_task(int(disp.width/2)  - int(5*6 /2),gap,6*5,8,black)
        text_task(int(disp.width/2)  - int(5*6 /2),gap,cur_time)
    del cur_time
    clean_mem()

#----------bat  stuff ---------------------------------------------------------

def str_bat(bat_per):
    bat_string = ''
    if bat_per < 100:
        bat_string += ' '
    if bat_per < 10:
        bat_string += ' '
    bat_string += str(bat_per) + '%__bata'
    if sensor.is_charging():
        bat_string += 'chrg__'
    else:
        bat_string += str(int((bat_per+10)*6/100)) + '__'
    return bat_string
    del bat_per
    clean_mem()

global but_buf
bat_buf = 0
def update_bat():
    cur_bat = sensor.bat_percent()
    global bat_buf
    bat_str = str_bat(cur_bat)
    if cur_bat != bat_buf:
        bat_buf = cur_bat
        rect_task(int(disp.width - gap - 6*(6)), gap, 6*len(bat_str),8,black)
        text_task(int(disp.width - gap - 6*(6)), gap, bat_str)
    del cur_bat,bat_str
    clean_mem()
    
    

def place_top_bar():
    rect_task(0,0,disp.width,10,black)
    text_task(0,gap,'Trico04c')
    update_time()
    update_bat()
    #add rect bar
    rect_task(0,8+2*gap, disp.width ,gap,white)
    clean_mem()


