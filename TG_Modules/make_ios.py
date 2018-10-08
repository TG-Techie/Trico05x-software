import digitalio, pulseio, analogio#, touchio #, audioio


def dio(pin, direction = None, init_val = None):
    io = digitalio.DigitalInOut(pin)
    if direction != None:
        if direction:
            io.direction = digitalio.Direction.INPUT
            #io.value = init_val
        else:
            io.direction = digitalio.Direction.OUTPUT
            io.value = init_val
    return(io)