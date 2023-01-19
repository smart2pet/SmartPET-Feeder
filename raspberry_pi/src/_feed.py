# Warning: Not recommended to use! This is a low level interface.

import serial

def run_motor(laps, feeder: serial.Serial):
    """
    (Low level interface, ***don't use directly***.) Control the lower computer to control the motor turning the specific laps.
    :param laps: int, the number of laps to run.
    """
    if feeder is not None:
        feeder.write(f's{laps};'.encode()) # Send motor run request to esp32.
        feeder.flush() # Flush the buffer
