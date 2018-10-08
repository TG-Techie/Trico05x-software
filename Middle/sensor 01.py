from staging import sen_brd

class thermal_cam_class():
    
    def __init__(self):
        
         val = 0
         while val == 0:
             val = self.get_data()[4][4]
    
    def get_data(self):
        return sen_brd.amg.pixels
        
thermal_camera = thermal_cam_class()