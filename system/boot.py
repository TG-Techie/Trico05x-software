#not gui startup:
import gc
gc.enable()

#from tg_modules import tg_gui as gui
import time#, sys
from system import handler

handler.load_system_prog('bar')

launcher_name = 'launcher'
handler.load_system_prog(launcher_name)
handler.load('empty__prog')


print('loaded')
handler.unload('thermal__camera')
handler.load('thermal__camera')

print(handler.cur_cont)


def quit_prog():
    handler.current.clear()
    handler.system.launcher.place() 

last_sys_refresh = time.monotonic()


while 1:
    
    if (time.monotonic() - last_sys_refresh) >= 59.5:
        last_sys_refresh = time.monotonic()
        for prog in handler.system:
            try:
                prog.container.refresh()
            except:
                pass
    
    #poll for touch and inputs
    #eventually this will be replaced by interupts eventually
    
    #pass touch and commands to the current program
    

    try:
        if handler.cur_cont.prog_wants_refresh: # this is a variable stored in 
            handler.cur_cont.refresh()
    except:
        pass
    