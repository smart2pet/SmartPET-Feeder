import serial

def feed(weight, feeder: serial.Serial):
    feeder.write(f's{weight};'.encode())
