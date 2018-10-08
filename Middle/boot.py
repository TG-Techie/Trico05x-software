import time
from gc import enable, collect as clean_mem
enable()
clean_mem()

from firmware_data import debug_boot, product_name, firmware_version

if debug_boot:
    print("booting...")#alert user over usb
    print("loading:")#alert user over usb


#-----get essentials form disp--------
from staging.disp import disp, backlite,color
#boot up graphics
disp.scroll(0,0,"booting...")
for i in range(0,8):
    disp.hline(0,i,disp.width,0)
#product name
disp.scroll(0,0,product_name)
#created by
disp.text(0,8,"""TG-Techie
firmware version: """ + firmware_version+
          """

Thanks To:)
Kathy Keough
Martin Yolles
Joseph Murphy
Adafruit & Ada-Discord""")
#wipe clean
for i in range(0,disp.height):
    disp.hline(0,i,disp.width,0)

if debug_boot:
    print("display..")


#---tasking---------
from tg_modules.tasking import thread_list
#--------------------------------
#############################################
#THE TASK SETUP !!!!!
trd = thread_list()
#############################################
#--------------------------------
clean_mem()
if debug_boot:
    print("tasking...")



#----screen graphics----
from staging import screen # contains 
clean_mem()
if debug_boot:
    print("screen..")


#----screen and thread init-----------------

screen.init(trd,disp,backlite)
if debug_boot:
    print("screen initialised")


#--wipe down end---

if debug_boot:
    for i in range(disp.height):
        disp.hline(0,i,disp.width,0)

disp.fill(0)
