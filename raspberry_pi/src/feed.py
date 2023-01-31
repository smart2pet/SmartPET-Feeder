import sqlite3
import time
import _feed
import serial
import sql
import tflite_runtime.interpreter as tflite
import log
from config import DB_PATH

try:
    feeder = serial.Serial("/dev/ttyUSB1", 115200) # Connect to the esp32
except:
    try:
        feeder = serial.Serial('/dev/ttyUSB0', 115200)
    except:
        print('[WARN] Using simulate feeding mode. ***No serial connection and real feeding.***')
        feeder = None
        # pass

# Load the model.
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
tflife_input_details = interpreter.get_input_details()
tflife_output_details = interpreter.get_output_details()


def feed(amount: int) -> None:
    """
    (High level interface. Recommend to use.) Feed the pet with the given weight.

    :param amount: The amount of the food.
    :type amount: int
    :return: None
    :rtype: None
    """
    if amount == 0: 
        return
    with sqlite3.Connection(DB_PATH) as conn: 
        interpreter.set_tensor(tflife_input_details[0]["index"], [[amount - 5]])
        interpreter.invoke()
        custom = interpreter.get_tensor(tflife_output_details[0]["index"])
        print(custom)
        # Start to feed
        _feed.run_motor(int(custom[0][0]), feeder)
        # Get the time
        now_time = time.localtime()
        hours = now_time.tm_hour
        minutes = now_time.tm_min
        year = now_time.tm_year
        month = now_time.tm_mon
        day = now_time.tm_mday
        # Store the feeding history.
        sql.add_to_history(hours, minutes, amount, year, month, day, cursor)
        conn.commit()
        # Log
        log.fed(amount)
