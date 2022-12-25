import serial

def feed(weight, feeder: serial.Serial):
    if feeder is not None:
        feeder.write(f's{weight};'.encode()) # Send weight to esp32
        feeder.flush() # Flush the buffer
