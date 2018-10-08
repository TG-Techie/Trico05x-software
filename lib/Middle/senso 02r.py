from staging import sen_brd

def thermal_cam_data():
    return sen_brd.amg.pixels[::-1] # flipped x