


from staging.pin_port import uart_port

###########################################
#GPS MODULE
from adafruit import  adafruit_gps
gps_chip = adafruit_gps.GPS(uart_port, debug=False)
gps_chip.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')