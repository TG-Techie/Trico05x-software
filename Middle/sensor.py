#TODOS:
#fix 
from staging import sen_brd, mother_brd

###################################
#thermal cam api and data adjustvc
def thermal_cam_data():
   return sen_brd.amg.pixels

#####################################
#gps chip ad
def gps_set_frequency(new = 1000):
    mother_brd.gps_chip.send_command(b'PMTK220,1000')
    
#####################################

def voc_data():
    return sen_brd.ccs.tvoc

def eco_data():
    return sen_brd.ccs.eco2