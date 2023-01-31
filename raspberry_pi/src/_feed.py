# Warning: Not recommended to use! This is a low level interface.

import serial

def run_motor(laps, feeder: serial.Serial):
    """
    (Low level interface. Only use if necessary.) Control the motor to run the specific laps.
    :param laps: int, the number of laps to run.
    """
    if feeder is not None:
        feeder.write(f's{laps};'.encode()) # Send motor run request to esp32.
        feeder.flush() # Flush the buffer
