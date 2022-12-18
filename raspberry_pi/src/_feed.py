import serial

def feed(weight, feeder: serial.Serial):
    feeder.write(f's{weight};'.encode()) # Send weight to esp32
    feeder.flush() # Flush the buffer
