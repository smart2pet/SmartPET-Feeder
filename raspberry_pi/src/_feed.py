import serial

def feed(laps, feeder: serial.Serial):
    if feeder is not None:
        feeder.write(f's{laps};'.encode()) # Send weight to esp32
        feeder.flush() # Flush the buffer
